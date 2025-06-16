from django.db import models
import os, json
import logging
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Destinar una carpeta en el sistema de archivos para subir documentos
def user_directory_path(instance, filename):
    return f"usuario/{instance.id}_{filename}"


# Configuración del logger
logger = logging.getLogger(__name__)





# region Usuario 
class Usuario(AbstractUser):
    OPCIONES_TIPODOC = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería')
    ]
    tipo_doc = models.CharField(max_length=20, choices=OPCIONES_TIPODOC)
    num_doc = models.CharField(max_length=10, unique=True)  
    email = models.EmailField(unique=True, blank=False)
    OPCIONES_GENERO = [
        ('masculino', 'MASCULINO'),
        ('femenino', 'FEMENINO'),
        ('prefiero no decirlo', 'PREFIERO NO DECIRLO')
    ]
    genero = models.CharField(max_length=20, choices=OPCIONES_GENERO)
    OPCIONES_RH=[('A+','A+'),
                ('A-','A-'),
                ('B+','B+'),
                ('B-','B-'),
                ('AB+','AB+'),
                ('AB-','AB-'),
                ('O+','O+'),
                ('O-','O-')
    ]
    rh = models.CharField(max_length=3,choices=OPCIONES_RH)
    telefono = PhoneNumberField(null=True, blank=True)  # PhoneNumberField
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo_poblacion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=20)
    eps = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Imagen')

    def __str__(self):
        return self.username
    
    # Eliminar la imagen del servidor si el usuario se borra
    def delete(self,*args,**kwargs):
        if self.imagen and self.imagen.name:
            self.eliminar_imagen()
        super().delete(*args,**kwargs)

    def eliminar_imagen(self):
        try:
            # Se comprueba si hay una imagen y si hay ruta de acceso a ella en MEDIA_ROOT
            if self.imagen and self.imagen.name and os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
                logger.info(f"Imagen eliminada correctamente: {self.imagen.path}")
            else:
                logger.warning(f"La imagen no existe o no tiene un nombre válido: {self.imagen.path}")
        except Exception as e:
            logger.error(f"Error al eliminar la imagen {self.imagen.path}: {e}")


#endregion






# region Paciente
class Paciente(Usuario):
    OPCIONES_REGIMEN = [
        ('subcidiado', 'SUBSIDIADO'),
        ('contributivo', 'CONTRIBUTIVO'),
        ('otro', 'OTRO')
    ]
    regimen = models.CharField(max_length=30, choices=OPCIONES_REGIMEN )
    numero_seguro_social = models.CharField(max_length=15, unique=True)
#endregion






#region Administrador
class Administrador(Usuario):
    RUTA_AREAS = [
        ('Odontologia', 'Odontología'),
        ('Cirugia', 'Cirugía'),
        ('General', 'General'),
        ('Rayos_x', 'Rayos X'),
    ]

    rol_acceso = models.CharField(max_length=100)
    centro_administracion = models.CharField(max_length=255, choices=RUTA_AREAS)
    permisos = models.JSONField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.permisos:
            area = self.centro_administracion  # Ya viene validado por choices

            todos_los_permisos = {
                "Odontologia": {
                    "administrador": {
                        "ver_pacientes": True,
                        "editar_pacientes": True,
                        "ver_historia_clinica": True,
                        "gestion_usuarios": True
                    }
                },
                "Cirugia": {
                    "administrador": {
                        "ver_pacientes": True,
                        "realizar_cirugia": True,
                        "ver_historia_clinica": True,
                        "gestion_usuarios": True
                    }
                },
                "General": {
                    "administrador": {
                        "ver_pacientes": True,
                        "ver_historia_clinica": True,
                        "gestion_usuarios": True
                    }
                },
                "Rayos_x": {
                    "administrador": {
                        "ver_pacientes": True,
                        "ver_imagenes": True,
                        "realizar_imagenes": True,
                        "gestion_usuarios": True
                    }
                }
            }

            permisos_area = todos_los_permisos.get(area)
            if permisos_area:
                self.permisos = {area: permisos_area["administrador"]}
            else:
                self.permisos = {}

        super().save(*args, **kwargs)


#endregion




#region Medicos
class Medico(Usuario):
    AREAS = [
        ('Odontologia', 'Odontología'),
        ('Cirugia', 'Cirugía'),
        ('General', 'General'),
        ('Rayos_x', 'Rayos X'),
    ]
    
    especialidad = models.CharField(max_length=100, choices=AREAS)
    numero_registro_profesional = models.CharField(max_length=50)
    licencia_certificacion = models.BooleanField(default=False)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.first_name}"

        return f"{self.first_name} {self.last_name}"

#endregion



#region Consulta
class Consulta(models.Model):
    especialidad = models.CharField(max_length=100, null=False, blank=True)
    tratamiento = models.TextField(max_length=200)
    diagnostico_principal = models.TextField(max_length=255, null=False)
    diagnostico_relacionado = models.TextField(max_length=255, null=False)    
    motivo_consulta = models.TextField(max_length=200)
    fecha_consulta = models.DateField(auto_now_add=True) 
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_consulta')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')

    def __str__(self):
        return f"{self.paciente} - {self.fecha_consulta}"

    class Meta:
        ordering = ['-fecha_consulta']

#endregion






#region PerfilPaciente
class PerfilPaciente(models.Model):
    tratamiento = models.TextField(max_length=200, null=True)
    opcion_vida_sexual = [
        ('activo', 'ACTIVO'),
        ('no activo', 'NO ACTIVO')
    ]
    vida_sexual = models.CharField(max_length=50, choices=opcion_vida_sexual)
    ciclo_mestrual = models.TextField(max_length=200, null=True)
    sustancias_psicotivas = models.BooleanField(default=False)  
    consumo_alcohol = models.BooleanField(default=False)  
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name='perfiles')

    def __str__(self):
        return f"Perfil de {self.consulta.paciente}"

# Modelo nuevo: hábitos alimenticios
class HabitoAlimenticio(models.Model):
    descripcion = models.TextField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='habitos_alimenticios')

    def __str__(self):
        return f"Hábito de {self.paciente} en {self.fecha}"

#endregion







#region Antecedente
class Antecedente(models.Model):
    descripcion = models.TextField(max_length=200, null=True)
    tipo_antecedente = models.TextField(max_length=200, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='antecedentes')
#endregion






#region Vacuna
class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=150)
    fecha_aplicacion = models.DateField()
    dosis = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='vacunas')

    def __str__(self):
        return f"{self.nombre_vacuna} - {self.fecha_aplicacion} - {self.paciente}"

    class Meta:
        ordering = ['-fecha_aplicacion']
#endregion






#region DatoQuirurgico
class DatoQuirurgico(models.Model):
    tipo_cirugia = models.CharField(max_length=150, null=False)
    fecha_cirugia = models.DateField(null=False)
    complicaciones = models.TextField(max_length=200, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='datos_quirurgicos')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_datos_quirurjicos')

#endregion






#region HistoriaClinicas
class RegistroClinico(models.Model):
    ultima_atencion = models.DateField()
    tratamiento = models.TextField()
    notas = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro clínico de {self.paciente} - {self.ultima_atencion}"

    class Meta:
        ordering = ['-ultima_atencion']

#endregion







#region DatoAntropometrico
class DatoAntropometrico(models.Model):
    altura_decimal = models.DecimalField(max_digits=20, decimal_places=2)
    peso = models.DecimalField(max_digits=20, decimal_places=2)
    indice_masa_corporal = models.DecimalField(max_digits=20, decimal_places=2)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='datos_antropometricos')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_dato_antropometrico')

#endregion






#region Contratacion
class Contratacion(models.Model):
    fecha_contratacion = models.DateField(null=False)
    hoja_vida = models.FileField(upload_to='hojas_vida/', null=True, blank=True)
    contrato = models.FileField(upload_to='contratos/', null=True, blank=True)

    def agregar_documentos(self, empleado, hoja_vida, contrato):
        empleado.hoja_vida = hoja_vida  
        empleado.contrato = contrato
        empleado.save()
        return empleado

    def __str__(self):
        return f"Contratación en {self.fecha_contratacion}"

#endregion





#region Horario medico
class HorarioMedico(models.Model):
    OPCIONES_DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo')
    ]

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=OPCIONES_DIAS_SEMANA, default='lunes')  # No es necesario null=False cuando usas choices
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
#endregion

#region Agenda
class AgendaMedica(models.Model):
    medico=models.ForeignKey(Medico,on_delete=models.CASCADE,related_name='medico_agenda')
    hora=models.TimeField()
    paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,related_name='paciente_cita')
    motivo=models.CharField(max_length=200,null=False)
#endregion


#region Citas
class Cita(models.Model):
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()

    OPCIONES_ESTADO_CITA = [
        ('DP', 'Disponible'),
        ('agendada', 'Agendada'),
        ('atendida', 'Atendida'),
        ('cancelada', 'Cancelada'),
        ('NA', 'No atendida')
    ]

    estado_cita = models.CharField(max_length=10, choices=OPCIONES_ESTADO_CITA, default='agendada')
    especialidad = models.CharField(max_length=100, blank=True)

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_citas')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_agenda_cita')

    disponibilidad = models.ForeignKey(
        'Disponibilidad',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='citas_asociadas'
    )

    def __str__(self):
        return f"{self.fecha_cita} {self.hora_cita} - {self.paciente} con {self.medico}"

    class Meta:
        ordering = ['-fecha_cita', 'hora_cita']

#endregion






#region CertificadoIncapacidad
class CertificadoIncapacidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_incapacidad_medica')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_incapacidad_medica')

    dias_incapacidad = models.CharField(max_length=4)
    motivo_incapacidad = models.CharField(max_length=255)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(null=True, blank=True)

    diagnostico_principal = models.TextField(max_length=255)
    diagnostico_relacionado = models.TextField(max_length=255)
    observaciones = models.CharField(max_length=255)

    def __str__(self):
        return f"Incapacidad de {self.paciente} ({self.fecha_inicio} - {self.fecha_fin})"

    class Meta:
        ordering = ['-fecha_inicio']

#endregion






#region RecetasMedicas
class RecetaMedica(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_receta_medica')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_receta_medica')

    medicamento = models.CharField(max_length=100)
    concentracion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    via_administracion = models.CharField(max_length=20)

    diagnostico_principal = models.TextField(max_length=255)
    diagnostico_relacionado = models.TextField(max_length=255)
    intervalo = models.CharField(max_length=20)

    recomendaciones = models.CharField(max_length=255)
    indicaciones = models.CharField(max_length=255)
    fecha_medicado = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Receta: {self.medicamento} para {self.paciente} - {self.fecha_medicado}"

    class Meta:
        ordering = ['-fecha_medicado']

#endregion


#region  OrdenesMedicas
class OrdenMedica(models.Model):
    cups = models.CharField(max_length=10, unique=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_orden_medica')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente_orden_medica')

    especialidad_referido = models.CharField(max_length=255)
    cantidad = models.CharField(max_length=4)

    diagnostico_principal = models.TextField(max_length=255)
    diagnostico_relacionado = models.TextField(max_length=255)
    motivo = models.CharField(max_length=255)

    fecha_ordenado = models.DateField(default=timezone.now)
    vigencia = models.DateField()

    ESTADO_CITA = [
        ('VIG', 'Vigente'),
        ('VEN', 'Vencida'),
        ('AG', 'Agendada'),
        ('PA', 'Por autorizar'),
        ('AUT', 'Autorizada')
    ]
    estado = models.CharField(max_length=15, choices=ESTADO_CITA)

    def __str__(self):
        return f"Orden CUPS {self.cups} para {self.paciente} - {self.estado}"

    class Meta:
        ordering = ['-fecha_ordenado']

#endregion





#region Disponibilidad 
class Disponibilidad(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('cancelado', 'Cancelado'),
    ]

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tipo_cita = models.CharField(max_length=50, choices=[('general', 'General'), ('odontologia', 'Odontología')])
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    max_pacientes = models.PositiveIntegerField(default=1)
    duracion = models.PositiveIntegerField(default=30)  # minutos

    def __str__(self):
        return f"{self.medico} - {self.fecha} de {self.hora_inicio} a {self.hora_fin}"

    class Meta:
        ordering = ['-fecha', 'hora_inicio']

#endregion



class TablaReferenciaCIE10(models.Model):
    tabla=models.CharField(max_length=5,null=False)
    codigo=models.CharField(max_length=5,unique=True)
    nombre=models.CharField(max_length=250,null=False)
    descripcion=models.CharField(max_length=250,null=False)
    habilitado=models.CharField(max_length=2,null=False)
    extra_i_aplica_a_sexo=models.CharField(max_length=10,null=False)
    extra_ii_edad_minima=models.CharField(max_length=3,null=False)
    extra_iii_edad_maxima=models.CharField(max_length=3,null=False)
    extra_iv_grupo_mortalidad=models.CharField(max_length=10,null=False)
    extra_v=models.CharField(max_length=255,null=False)
    extra_vi_capitulo=models.CharField(max_length=3,null=False)
    extra_x=models.CharField(max_length=1,null=False)
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"
