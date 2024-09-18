from persona import*
from experiencia import*
from ips import *
from Posiciones import *
from estudios import *

class Empleados(Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion,Id,Fecha_Contratacion,Posicion_Id,Persona_Id):
      super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
      self.__ID=Id
      self.__Fecha_Contratacion=Fecha_Contratacion
      self.__Posicion=Posicion_Id
      self.__Persona=Persona_Id
      self.__nro_doc=nro_doc
    
    def getID(self):
        return self.__ID

    def getFecha_Contratacion(self):
        return self.__Fecha_Contratacion

    def getPosicion(self):
        return self.__Posicion

    def getPersona(self):
        return self.__Persona
    
    def getNumeroDoc (self):
        return self.__nro_doc