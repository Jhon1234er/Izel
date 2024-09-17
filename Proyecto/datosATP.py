class antropometricos:
    def __init__(self, talla,temperatura,imc,pulso, peso, frecuencia_R, presion_A):
        self.__Peso = peso
        self.__Temperatura = temperatura
        self.__Talla = talla
        self.__Imc = imc
        self.__Pulso = pulso
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
        return self.__Imc
    
    def setIMC(self, imc):
        self.__Imc = imc
        
    def getPulso(self):
        return self.__Pulso
    
    def setPulso(self, pulso):
        self.__Pulso = pulso
    
    def getFrecuencia_R(self):
        return self.__Frecuencia_R
    
    def setFrecuencia_R(self, frecuencia_R):
        self.__Frecuencia_R = frecuencia_R
    
    def getPresion_A(self):
        return self.__Presion_A
    
    def setPresion_A(self, presion_A):
        self.__Presion_A = presion_A
        