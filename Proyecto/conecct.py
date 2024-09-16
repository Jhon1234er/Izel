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
Persona = Mydb["Persona"]

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
        
def registrar_Cuenta(correo, contraseña, tipo):
        if Autenti.find_one({"Correo": correo}):
            return print ("El correo electrónico ya está registrado.")
        else:
            nueva_Cuenta = {
                "Correo": correo,
                "Contraseña": contraseña,
                "Tipo": tipo
            }
        
        Autenti.insert_one(nueva_Cuenta)


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

# def Registrar_Usuario(Numero):
#         if Persona.find_one({"Numero_Documento": Numero}):
#             print("El usuario ya tiene su registro completo.")
#             return
#         else:
#             Nuevo_Registro = {
#                 "Nombre":{
#                     "Nombre1":
#                     "Nombre2":
#                     },
#                 "Apellido":{
#                     "Apellido1":
#                     "Apellido2":
#                     },
#                 "Genero":
#                 "Rh":
#                 "Correo":
#                 "Teléfono":
#                 "Tipo_Documento":
#                 "Numero_Documento":
#                 "Fecha_Nacimiento":
#                 "Tipo_Poblacion":
#                 "Ocupación":
#                 "Eps":
#                 "Direcció":{
#                     "Tipo_Via":
#                     "Nombre_Via":
#                     "Numero_Via":
#                     },
#                 }
                
#         Persona.insert_one(Nuevo_Registro)
