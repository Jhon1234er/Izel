from persona import *

class Paciente(Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps,direccion):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
        self.__eps=eps
        self.__Dirección=direccion
        self.__nro_doc = nro_doc 
        self.__nombres= nombres
        self.__apellidos= apellidos
        self.__genero= genero
        self.__rh= rh
        self.__correo= correo
        self.__telefono= telefono
        self.__tipo_doc= tipo_doc
        self.__fecha_nacimiento= fecha_nacimiento
        self.__tipo_poblacion= tipo_poblacion
        self.__ocupacion= ocupacion
        self.__eps=eps
        
    def getNombres(self):
        return self.__nombres.split()[0] 

    # def getNombre2(self):
    #     return self.__nombres.split()[1] if len(self.nombres.split()) > 1 else None
    
    def getApellidos(self):
        return self.__apellidos.split()[0] 

    # def getApellido2(self):
    #     return self.__apellidos.split()[1] if len(self.apellidos.split()) > 1 else None
    
    def getGenero(self):
        return self.__genero

    def getRh(self):
        return self.__rh

    def getCorreo(self):
        return self.__correo

    def getTelefono(self):
        return self.__telefono

    def getTipoDoc(self):
        return self.__tipo_doc

    def getNumeroDoc(self):
        return self.__nro_doc

    def getFechaNacimiento(self):
        return self.__fecha_nacimiento

    def getTipoPoblacion(self):
        return self.__tipo_poblacion

    def getOcupacion(self):
        return self.__ocupacion
    
    def getEPS(self):
        return self.__eps

    def getDirección(self):
        return self.__Dirección
    


    
