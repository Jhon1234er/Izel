from persona import *

class Paciente(Persona):
    def __init__(self, nombre1, nombre2, apellido1, apellido2, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps,direccion):
        super().__init__(nombre1, apellido1, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
        self.__eps=eps
        self.__Dirección=direccion
        self.__nro_doc = nro_doc 
        self.__Primer_N= nombre1
        self.__Segundo_N=nombre2
        self.__Primer_A= apellido1
        self.__Segundo_A=apellido2
        self.__genero= genero
        self.__rh= rh
        self.__correo= correo
        self.__telefono= telefono
        self.__tipo_doc= tipo_doc
        self.__fecha_nacimiento= fecha_nacimiento
        self.__tipo_poblacion= tipo_poblacion
        self.__ocupacion= ocupacion
        self.__eps=eps
        
    def getNombre1(self):
        return self.__Primer_N 

    def getNombre2(self):
         return self.__Segundo_N
    
    def getApellido1(self):
        return self.__Primer_A 

    def getApellido2(self):
         return self.__Segundo_A
    
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
    


    
