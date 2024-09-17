from pymongo import errors
import pymongo
from medico import *


Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
Mydb = Myclient["Izel"]
Autenti = Mydb["Autentificacion"]
Vacunas = Mydb["Vacunas"]
ConsultaDB =Mydb["Consulta"]
Quirurgico = Mydb["Quirurgicos"]
AntropoDB = Mydb["Antropometricos"]
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
    Formula.insert_one(nuevaFormula)
