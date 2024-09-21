from persona import*
from ips import *
from Posiciones import *


class Empleados():
    def __init__(self,Id,Fecha_Contratacion,Posicion_Id,Persona_Id):
      self.__Id=Id
      self.__Fecha_Contratacion=Fecha_Contratacion
      self.__Posicion=Posicion_Id
      self.__Persona=Persona_Id
    
    def getID(self):
        return self.__Id

    def getFecha_Contratacion(self):
        return self.__Fecha_Contratacion

    def getPosicion(self):
        return self.__Posicion

    def getIdPersona(self):
        return self.__Persona
    