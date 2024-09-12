from persona import *

class Paciente(Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps,regimen):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
        self.__eps=eps
        self.__regimen=regimen
        
        
    def getEPS(self):
        return self.__eps
    def setEPS(self,eps):
        self.__eps=eps
        
    def getRegimen(self):
        return self.__regimen
    def setRegimen(self,regimen):
        self.__regimen=regimen