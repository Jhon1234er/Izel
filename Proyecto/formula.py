class medica:
    def __init__(self, codigo_F, cantidad, duracion, concentracion, medicamento, indicaciones, via_Administracion):
        self.__CodigoF = codigo_F
        self.__Cantidad = cantidad
        self.__Duracion = duracion
        self.__Concentracion = concentracion
        self.__Medicamento = medicamento
        self.__Indicaciones = indicaciones
        self.__ViaAdministracion = via_Administracion
    
    def getCodigoF(self):
        return self.__CodigoF
    
    def setCodigoF(self, codigo_F):
        self.__CodigoF = codigo_F
    
    def getCantidad(self):
        return self.__Cantidad
    
    def setCantidad(self, cantidad):
        self.__Cantidad = cantidad
    
    def getDuracion(self):
        return self.__Duracion
    
    def setDuracion(self, duracion):
        self.__Duracion = duracion
    
    def getConcentracion(self):
        return self.__Concentracion
    
    def setConcentracion(self, concentracion):
        self.__Concentracion = concentracion
    
    def getMedicamento(self):
        return self.__Medicamento
    
    def setMedicamento(self, medicamento):
        self.__Medicamento = medicamento
    
    def getIndicaciones(self):
        return self.__Indicaciones
    
    def setIndicaciones(self, indicaciones):
        self.__Indicaciones = indicaciones
    
    def getViaAdministracion(self):
        return self.__ViaAdministracion
    
    def setViaAdministracion(self, via_administracion):
        self.__ViaAdministracion = via_administracion
        
        
        