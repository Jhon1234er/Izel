class vacunas:
    def __init__(self, descripcion, fecha_Vacuna, dosis, numero_vacuna, 
                  refuerzos, via_aplicacion, eventos_adversos, intervalo):
         self.__Descripcion = descripcion
         self.__Fecha_Vacuna = fecha_Vacuna
         self.__Dosis = dosis
         self.__Numero_Vacuna = numero_vacuna
         self.__Refuerzos = refuerzos
         self.__Via_Aplicacion = via_aplicacion
         self.__Eventos_Adversos = eventos_adversos
         self.__Intervalo = intervalo

    def getDescipción(self):
        return self.__Descripcion
    
    def setDescipción(self,descripcion):
        self.__Descripcion = descripcion
    
    def getFecha_Vacuna(self):
        return self.__Fecha_Vacuna
    
    def setFecha_Vacuna(self, fecha_Vacuna):
        self.__Fecha_Vacuna = fecha_Vacuna
        
    def getDosis(self):
        return self.__Dosis
    
    def setDosis(self, dosis):
        self.__Dosis = dosis
        
    def getNumero_Vacuna(self):
        return self.__Numero_Vacuna
    
    def setNumero_Vacuna(self, numero_vacuna):
        self.__Numero_Vacuna = numero_vacuna
        
    def getRefuerzos(self):
        return self.__Refuerzos
    
    def setRefuerzos(self, refuerzos):
        self.__Refuerzos = refuerzos
    
    def getVia_Aplicacion(self):
        return self.__Via_Aplicacion
    
    def setVia_Aplicacion(self, via_aplicacion):
        self.__Via_Aplicacion = via_aplicacion
        
    def getEventos_adversos(self):
        return self.__Eventos_Adversos
    
    def setEventos_Adversos(self, eventos_adversos):
        self.__Eventos_Adversos = eventos_adversos
        
    def getIntervalo(self):
        return self.__Intervalo
    
    def setIntervalo(self, intervalo):
        self.__Intervalo = intervalo
        
        