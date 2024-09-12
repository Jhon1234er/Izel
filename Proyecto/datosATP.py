class antropometricos:
    def __init__(self, talla,temperatura,imc,pluso, peso, frecuencia_R, presion_A):
        self.__Peso = peso
        self.__Temperatura = temperatura
        self.__Talla = talla
        self.__IMC = imc
        self.__Pluso = pluso
        self.__Frecuencia_R = frecuencia_R
        self.__Presion_A = presion_A
    
    def getPeso(self):
        return self.__Peso
    
    def setPeso(self, peso):
        self.__Peso = peso
    
    def getTemperatura(self):
        return self.__Temperatura
    
    def setTemperatura(self, temperatura):
        self.__Temperatura = temperatura
    
    def getTalla(self):
        return self.__Talla
    
    def setTalla(self, talla):
        self.__Talla = talla
    
    def getIMC(self):
        return self.__IMC
    
    def setIMC(self, IMC):
        self.__IMC = IMC
        
    def getPluso(self):
        return self.__Pluso
    
    def setPluso(self, pluso):
        self.__Pluso = pluso
    
    def getFrecuencia_R(self):
        return self.__Frecuencia_R
    
    def setFrecuencia_R(self, frecuencia_R):
        self.__Frecuencia_R = frecuencia_R
    
    def getPresion_A(self):
        return self.__Presion_A
    
    def setPresion_A(self, presion_A):
        self.__Presion_A = presion_A
        