from pymongo import errors
import pymongo


Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
Mydb = Myclient["Izel"]
Autenti = Mydb["Autentificacion"]
Vacunas = Mydb["Vacunas"]
Consulta =Mydb["Consulta"]
Quirurgico = Mydb["Quirurgicos"]
Antropo = Mydb["Antropometricos"]
Antecedentes = Mydb["Antecedentes"]
Formula= Mydb ["FormulaMedica"]

def verificar(Email,Pin):
        query = {
            "Correo":Email,
            "Contraseña":Pin
        }
        
        usuario=Autenti.find_one(query)
        
        if usuario:
            return True
        else:
            print("Cuenta no encontrada")
            return False
        
def registrar_usuario(correo, contraseña, tipo):
        if Autenti.find_one({"Correo": correo}):
            print("El correo electrónico ya está registrado.")
            return
        
        nuevo_usuario = {
            "Correo": correo,
            "Contraseña": contraseña,
            "Tipo": tipo
        }
        
        Autenti.insert_one(nuevo_usuario)


def tipo_usuario(correo):
        query = {"Correo": correo}
        usuario = Autenti.find_one(query)
        
        if usuario:
            return usuario.get("Tipo")
        else:
            print("Usuario no encontrado")
            return None

def Datos_Vacunas(Numero):
    resultados = Vacunas.find({"Usuario_id": Numero})
    vacunas = [x for x in resultados]
    return vacunas

def Datos_Consulta(Numero):
    resultados = Consulta.find({"Usuario_id": Numero})
    consulta = [x for x in resultados]
    return consulta

def Datos_Quirurgico (Numero):
    resultados = Quirurgico.find({"Usuario_id": Numero})
    quirur = [x for x in resultados]
    return quirur 

def Datos_Antropometricos(Numero):
    resultados = Antropo.find({"Usuario_id": Numero})
    date = [x for x in resultados]
    return date

def Datos_Antecedentes(Numero):
    resultados = Antecedentes.find({"Usuario_id": Numero})
    antes = [x for x in resultados]
    return antes

def agregarDatosConsulta(Numero,descripcion,motivo,diagnostico,planTerapeutico,epicrisis,nombreAcompañante,parentescoAcompañante,conclusiones):
    nuevaConsulta={
         "Usuario_id":Numero,
         "Descripcion_Enfermedad":descripcion,
         "Motivo_Consulta":motivo,
         "Diagnostico":diagnostico,
         "Plan_Terapeutico":planTerapeutico,
         "Epicrisis":epicrisis,
         "Nombre_Acompañante":nombreAcompañante,
         "Parentesco_Acompañante":parentescoAcompañante,
         "Conclusiones":conclusiones
    }
    Consulta.insert_one(nuevaConsulta)

def agregarDatosATP(Numero,peso,talla,imc,temperatura,pulso,frecuencia_R,presion_A):
    nuevoDatosATP={
          'Usuario_id': Numero,
          'Peso': peso,
          'Talla': talla,
          'IMS': imc,
          'Temperatura': temperatura,
          'Pulso': pulso,
          'Frecuencia_Respiratoria': frecuencia_R,
          'Presion_Arterial': presion_A
     }
    Antropo.insert_one(nuevoDatosATP)

def agregarFormula(codigo_F,cantidad,duracion,concentracion,medicamento,indicaciones,via_Administracion):
    nuevaFormula={
         "CodigoFormula":codigo_F,
         "NombreMedicamento":medicamento,
         "CantidadMedicamento":cantidad,
         "DuracionMedicamento":duracion,
         "Concentracion":concentracion,
         "Indicaciones":indicaciones,
         "ViaAdministracion":via_Administracion
    }
    Formula.insert_one(nuevaFormula)
