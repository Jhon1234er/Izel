class Registro:
    def __init__(self, email, clave):
        self.__Correo=email
        # self.__NumeroDoc=numDoc
        self.__Contraseña=clave
    
    def getCorreo (self):
        return self.__Correo
    def setCorreo (self,email):
        self.__Correo=email
    
    # def getNumeroDoc (self):
    #     return self.__NumeroDoc
    # def setNumeroDoc (self,numDoc):
    #     self.__NumeroDoc=numDoc
    
    def getContraseña (self):
        return self.__Contraseña
    def setContraseña (self,clave):
        self.__Contraseña=clave