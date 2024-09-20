from pymongo import *
from paciente import *
from Empleados import *
import pymongo
from medico import *


Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
Mydb = Myclient["Izel"]
AutentiDB = Mydb["Autentificacion"]
VacunasDB = Mydb["Vacunas"]
ConsultaDB =Mydb["Consulta"]
QuirurgicoDB = Mydb["Quirurgicos"]
AntropoDB = Mydb["Antropometricos"]
AntecedentesDB = Mydb["Antecedentes"]
FormulaDB= Mydb ["FormulaMedica"]
PersonaDB= Mydb ['Persona']
EmpleadoDB= Mydb ['Empleados']

def verificar(Email,Pin):
        Autentificacion = {
            "Correo":Email,
            "Contraseña":Pin
        }
        
        usuario=AutentiDB.find_one(Autentificacion)
        
        if usuario:
            return True
        else:
            print("Cuenta no encontrada")
            return False
        
def registrar_Cuenta(correo, contraseña, tipo):
        if AutentiDB.find_one({"Correo": correo}):
            return print ("El correo electrónico ya está registrado.")
        else:
            nueva_Cuenta = {
                "Correo": correo,
                "Contraseña": contraseña,
                "Tipo": tipo
            }
        
        AutentiDB.insert_one(nueva_Cuenta)


def tipo_usuario(correo):
        Tip= {"Correo": correo}
        usuario = AutentiDB.find_one(Tip)
        
        if usuario:
            return usuario.get("Tipo")
        else:
            print("Usuario no encontrado")
            return None


def Datos_Perfil(Email):
    Perfil=PersonaDB.find_one({"Correo":Email},
                       {"Nombre.Nombre1":1,
                        "Apellido.Apellido1":1,
                        "Genero":1,
                        "Tipo_Documento":1,
                        "Numero_Documento":1,
                        "Ocupación":1,
                        "Eps":1,
                        "_id":0
                        }
                       )
    return Perfil


def Datos_Vacunas(Email):
    prefil=({"Correo":Email})
    Num=PersonaDB.find_one(prefil)
    if Num:
        resultados = VacunasDB.find({"Usuario_id": Num.get("Numero_Documento") })
        vacunas = [x for x in resultados]
    return vacunas

def Datos_Consulta(Email):
    prefil=({"Correo":Email})
    Num=PersonaDB.find_one(prefil)
    if Num:
        resultados = ConsultaDB.find({"Usuario_id": Num.get("Numero_Documento")})
        consulta = [x for x in resultados]
    return consulta

def Datos_Quirurgico (Email):
    prefil=({"Correo":Email})
    Num=PersonaDB.find_one(prefil)
    if Num:
        resultados = QuirurgicoDB.find({"Usuario_id":Num.get("Numero_Documento")})
        quirur = [x for x in resultados]
    return quirur 

def Datos_Antropometricos(Email):
    prefil=({"Correo":Email})
    Num=PersonaDB.find_one(prefil)
    if Num:
        resultados = AntropoDB.find({"Usuario_id":Num.get("Numero_Documento")})
        date = [x for x in resultados]
    return date

def Datos_Antecedentes(Email):
    prefil=({"Correo":Email})
    Num=PersonaDB.find_one(prefil)
    if Num:
        resultados = AntecedentesDB.find({"Usuario_id":Num.get("Numero_Documento")})
        antes = [x for x in resultados]
    return antes
   

def Doctor_Paciente (nro_doc):
    Perfil=PersonaDB.find_one({"Numero_Documento":nro_doc},
                       {"Nombre.Nombre1":1,
                        "Apellido.Apellido1":1,
                        "Genero":1,
                        "Tipo_Documento":1,
                        "Numero_Documento":1,
                        "Ocupación":1,
                        "Eps":1,
                        "_id":0
                        }
                       )
    return Perfil

def Registrar_Usuario(p):
    
    if PersonaDB.find_one({"Numero_Documento": p.getNumeroDoc()}):
        print("El usuario ya tiene su registro completo.")
        return
    else:
        Nuevo_Registro = {
            "Nombre":{
                "Nombre1":p.getNombre1(),
                "Nombre2":p.getNombre2(),
            },
            "Apellido":{
                "Apellido1":p.getApellido1(),                              
                "Apellido2":p.getApellido2(),
            },
            "Genero": p.getGenero(),
            "Rh": p.getRh(),
            "Correo": p.getCorreo(),
            "Teléfono": p.getTelefono(),
            "Tipo_Documento": p.getTipoDoc(),
            "Numero_Documento": p.getNumeroDoc(),
            "Fecha_Nacimiento": p.getFechaNacimiento(),
            "Tipo_Poblacion": p.getTipoPoblacion(),
            "Ocupación": p.getOcupacion(),
            "Eps": p.getEPS(),
            "Dirección": p.getDirección()
            }
                
        PersonaDB.insert_one(Nuevo_Registro)
        
def Registrar_Contrato (c):
    if EmpleadoDB.find_one({"Empleado_id": c.getID()}):
        print("ESTE EMPLEADO YA EXISTE ")
        return
    else:
        Nuevo_contrato={
            "Empleado_id":c.getID(),
            "Fecha_Contratacion":c.getFecha_Contratacion(),
            "Posicion_Id":c.getPosicion(),
            "Persona_Id":c.getIdPersona()
        }
    
    EmpleadoDB.insert_one(Nuevo_contrato)
    print("CONTRATO REGISTRADO")
    
    
def agregarDatosConsulta(nro_doc,p):
    nuevaConsulta={
         "Usuario_id":nro_doc,
         "Descripcion_Enfermedad":p.getDescripcion(),
         "Motivo_Consulta":p.getMotivo(),
         "Diagnostico":p.getDiagnostico(),
         "Plan_Terapeutico":p.getPlanTerapia(),
         "Epicrisis":p.getEpicrisis(),
         "Nombre_Acompañante":p.getNombre_A(),
         "Parentesco_Acompañante":p.getParentesco_A(),
         "Conclusiones":p.getConclusiones()
    }
    ConsultaDB.insert_one(nuevaConsulta)

def agregarDatosATP(nro_doc,p):
    nuevoDatosATP={
          'Usuario_id':nro_doc,
          'Peso': p.getPeso(),
          'Talla': p.getTalla(),
          'IMS': p.getIMC(),
          'Temperatura':p.getTemperatura() ,
          'Pulso': p.getPulso(),
          'Frecuencia_Respiratoria':p.getFrecuencia_R(),
          'Presion_Arterial':p.getPresion_A()
     }
    AntropoDB.insert_one(nuevoDatosATP)

def agregarFormula(nro_doc,p):
    nuevaFormula={
         'Usuario_id':nro_doc,
         "CodigoFormula":p.getCodigoF(),
         "NombreMedicamento":p.getMedicamento(),
         "CantidadMedicamento":p.getCantidad(),
         "DuracionMedicamento":p.getDuracion(),
         "Concentracion":p.getConcentracion(),
         "Indicaciones":p.getIndicaciones(),
         "ViaAdministracion":p.getViaAdministracion()
    }
    FormulaDB.insert_one(nuevaFormula)

def Visualizar_Departamentos(posicionId):
    resultados = EmpleadoDB.find({"Posicion_Id": posicionId})

    empleados_info = []
    for empleado in resultados:
        persona = PersonaDB.find_one({"Numero_Documento": empleado["Persona_Id"]})
        if persona:
            empleado_info = {
                "Empleado_id": empleado["Empleado_id"],
                "Nombre": persona["Nombre"]["Nombre1"] + " " + persona["Nombre"].get("Nombre2", ""),
                "Apellido": persona["Apellido"]["Apellido1"] + " " + persona["Apellido"].get("Apellido2", ""),
                "Genero": persona["Genero"],
                "Correo": persona["Correo"],
                "Telefono": persona["Teléfono"],
                "Tipo_Documento": persona["Tipo_Documento"],
                "Numero_Documento": persona["Numero_Documento"],
                "Fecha_Nacimiento": persona["Fecha_Nacimiento"],
            }
            empleados_info.append(empleado_info)

    return empleados_info

    
    

    