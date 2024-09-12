from persona import *

class Medico(Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion,cod_medico,especialidad):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
        self.__cod_medico=cod_medico
        self.__especialidad=especialidad
        
    def getCod_medico(self):
        return self.__cod_medico
    def setCod_medico(self,cod_medico):
        self.__cod_medico=cod_medico
        
    def getEspecialidad(self):
        return self.__especialidad
    def setEspecialidad(self,especialidad):
        self.__=especialidad