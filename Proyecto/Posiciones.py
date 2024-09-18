from Departamento import *

class Posiones (Departamentos):
    def __init__(self, id, nombre,Posicion_id,Nombre_P):
        super().__init__(id, nombre)
        self.__posicion_id=Posicion_id
        self.__nombre_P=Nombre_P
    
    def getPosicion (self):
        return self.__posicion_id
    
    def getNombre (self):
        return self.__nombre_P
    
    