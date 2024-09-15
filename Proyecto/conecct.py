from pymongo import errors
from menu import*
import pymongo
def verificar(Email,Pin):
    try:
        Myclient=pymongo.MongoClient("mongodb://localhost:27017/")
        Mydb=Myclient["INFINITY"]
        Autenti=Mydb["Autentificacion"]
        Persona=Mydb["Persona"]
        
        query = {
            "Correo":Email,
            "Contraseña":Pin
        }
        
        usuario=Autenti.find_one(query)
        
        if usuario:
            persona = Persona.find_one({"correo": Email})
            if persona:
                print(f"Persona encontrada en collection_Persona: {persona}")                  
                
                nombre_objeto = persona.get("Nombre", {})
                print(f"Nombre objeto: {nombre_objeto}")  
                
                if isinstance(nombre_objeto, dict):
                    nombre1 = nombre_objeto.get("Nombre1", "Nombre no disponible")
                    print(f"Nombre1 encontrado: {nombre1}") 
                    return nombre1
        else:
            print("Cuenta no encontrada")
            return False
    except errors.ConnectionError as e:
        print(f"error de conexion:{e}")
        return False
    except errors.ConnectionError as e:
        print(f"Error en pymongo: {e}")
        return False
    
    finally:
        Myclient.close()