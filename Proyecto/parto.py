class parto:
    def __init__(self, fecha, hora, signos_Vit, aspecto_Gen, tamaño_F, numero_F, fetocardia): 
        self.__Fecha = fecha
        self.__Hora = hora
        self.__Signos_Vit = signos_Vit
        self.__Aspecto_Gen = aspecto_Gen
        self.__Tamaño_F = tamaño_F
        self.__Numero_F = numero_F
        self.__Fetocardia = fetocardia
    
    def getFecha(self):
        return self.__Fecha
    
    def setFecha(self, fecha):
        self.__Fecha = fecha
    
    def getHora(self):
        return self.__Hora
    
    def setHora(self, hora):
        self.__Hora = hora
    
    def getSignos_Vit(self):
        return self.__Signos_Vit
    
    def setSignos_Vit(self, signos_Vit):
        self.__Signos_Vit = signos_Vit
    
    def getAspecto_Gen(self):
        return self.__Aspecto_Gen
    
    def setAspecto_Gen(self, aspecto_Gen):
        self.__Aspecto_Gen = aspecto_Gen
    
    def getTamaño_F(self):
        return self.__Tamaño_F
    
    def setTamaño_F(self, tamaño_F):
        self.__Tamaño_F = tamaño_F
    
    def getNumero_F(self):
        return self.__Numero_F
    
    def setNumero_F(self, numero_F):
        self.__Numero_F = numero_F
    
    def getFetocardia(self):
        return self.__Fetocardia
    
    def setFetocardia(self, fetocardia):
        self.__Fetocardia = fetocardia
        