from pymongo import errors
from paciente import *
import pymongo


Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
Mydb = Myclient["Izel"]
Autenti = Mydb["Autentificacion"]
Vacunas = Mydb["Vacunas"]
Consulta =Mydb["Consulta"]
Quirurgico = Mydb["Quirurgicos"]
Antropo = Mydb["Antropometricos"]
Antecedentes = Mydb["Antecedentes"]
PersonaDB = Mydb["Persona"]

def verificar(Email,Pin):
        Autentificacion = {
            "Correo":Email,
            "Contraseña":Pin
        }
        
        usuario=Autenti.find_one(Autentificacion)
        
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
        Tip= {"Correo": correo}
        usuario = Autenti.find_one(Tip)
        
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
   



def Registrar_Usuario(p):
    
    if PersonaDB.find_one({"Numero_Documento": p.getNumeroDoc()}):
        print("El usuario ya tiene su registro completo.")
        return
    else:
        Nuevo_Registro = {
            "Nombre":p.getNombres(),
            "Apellido":p.getApellidos(),
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
