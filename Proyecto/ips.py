class Ips:
    def __init__(self,codSggs,nit,razonSocial,sede,categorizacion,telefono,direccion,redes):
        self.__codSggs=codSggs
        self.__nit=nit
        self.__razonSocial=razonSocial
        self.__sede=sede
        self.__categorizacion=categorizacion
        self.__telefono=telefono
        self.__direccion=direccion
        self.__redes=redes
    
    def getcodSggs(self):
        return self.__codSggs
    def set(self,codSggs):
        self.__codSggs=codSggs

    def getNit(self):
        return self.__nit
    def setNit(self,nit):
        self.__nit=nit

    def getRazonSocial(self):
        return self.__razonSocial
    def setRazonSocial(self,razonSocial):
        self.__razonSocial=razonSocial

    def getSede(self):
        return self.__sede
    def setSede(self,sede):
        self.__=sede

    def getCategorizacion(self):
        return self.__categorizacion
    def setCategorizacion(self,categorizacion):
        self.__categorizacion=categorizacion

    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,telefono):
        self.__telefono=telefono

    def getDireccion(self):
        return self.__direccion
    def setDireccion(self,direccion):
        self.__direccion=direccion

    def getRedes(self):
        return self.__redes
    def setRedes(self,redes):
        self.__redes=redes