from pymongo import errors
import pymongo
from menu import*

Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
Mydb = Myclient["INFINITY"]
Autenti = Mydb["Autentificacion"]
Vacunas = Mydb["Vacunas"]
Consulta =Mydb["Consulta"]
Quirurgico = Mydb["Quirurgicos"]
Antropo = Mydb["Antropometricos"]
Antecedentes = Mydb["Antecedentes"]

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

