from persona import *

class Paciente(Persona):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps,direccion):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion)
        self.__eps=eps
        self.__Dirección=direccion
        
    def getEPS(self):
        return self.__eps

    def getDirección(self):
        return self.__Dirección
    
    def getNombre1(self):
        return self.nombres.split()[0] 

    def getNombre2(self):
        return self.nombres.split()[1] if len(self.nombres.split()) > 1 else None

    def getApellido1(self):
        return self.apellidos.split()[0] 

    def getApellido2(self):
        return self.apellidos.split()[1] if len(self.apellidos.split()) > 1 else None

    def getGenero(self):
        return self.genero

    def getRh(self):
        return self.rh

    def getCorreo(self):
        return self.correo

    def getTelefono(self):
        return self.telefono

    def getTipoDoc(self):
        return self.tipo_doc

    def getNumeroDoc(self):
        return self.nro_doc

    def getFechaNacimiento(self):
        return self.fecha_nacimiento

    def getTipoPoblacion(self):
        return self.tipo_poblacion

    def getOcupacion(self):
        return self.ocupacion