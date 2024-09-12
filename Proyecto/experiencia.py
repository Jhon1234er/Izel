class Experiencia_Laboral:
    def __init__(self,nombreEmpresa,sector,cargo,soporte,email,celular,fechaInicial,fechaFinal):
        self.__nombreEmpresa=nombreEmpresa
        self.__sector=sector
        self.__cargo=cargo
        self.__soporte=soporte
        self.__email=email
        self.__celular=celular
        self.__fechaInicial=fechaInicial
        self.__fechaFinal=fechaFinal
        
    def getNombreEmpresa(self):
        return self.__nombreEmpresa
    def setNombreEmpresa(self,nombreEmpresa):
        self.__=nombreEmpresa
        
    def getSector(self):
        return self.__sector
    def setSector(self,sector):
        self.__=sector
        
    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo
    
    def getSoporte(self):
        return self.__soporte
    def setSoporte(self,soporte):
        self.__soporte=soporte

    def getEmail(self):
        return self.__email
    def setEmail(self,email):
        self.__email=email
        
    def getCelular(self):
        return self.__celular
    def setCelular(self,celular):
        self.__celular=celular
        
    def getFechaInicial(self):
        return self.__fechaInicial
    def setFechaInicial(self,fechaInicial):
        self.__fechaInicial=fechaInicial
        
    def getFechaFinal(self):
        return self.__fechaFinal
    def setFechaFinal(self,fechaFinal):
        self.__=fechaFinal