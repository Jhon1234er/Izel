class antecedentes:
    def __init__(self, patologicos, quirurgicos, alegricos,ginecologicos, obstreticos, framalogicos, familiares):
        self.__Patologicos = patologicos
        self.__Quirurgicos = quirurgicos
        self.__Alegricos = alegricos
        self.__Ginecologicos = ginecologicos
        self.__Obstreticos = obstreticos
        self.__Framalogicos = framalogicos
        self.__Familiares = familiares
    
    def getPatologicos(self):
        return self.__Patologicos
    
    def setPatologicos(self, patologicos):
        self.__Patologicos = patologicos
    
    def getQuirurgicos(self):
        return self.__Quirurgicos
    
    def setQuirurgicos(self, quirurgicos):
        self.__Quirurgicos = quirurgicos
    
    def getAlegricos(self):
        return self.__Alegricos
    
    def setAlegricos(self, alegricos):
        self.__Alegricos = alegricos
    
    def getGinecologicos(self):
        return self.__Ginecologicos
    
    def setGinecologicos(self, ginecologicos):
        self.__Ginecologicos = ginecologicos
    
    def getObstreticos(self):
        return self.__Obstreticos
    
    def setObstreticos(self, obstreticos):
        self.__Obstreticos = obstreticos
    
    def getFramalogicos(self):
        return self.__Framalogicos
    
    def setFramalogicos(self, framalogicos):
        self.__Framalogicos = framalogicos
    
    def getFamiliares(self):
        return self.__Familiares
    
    def setFamiliares(self, familiares):
        self.__Familiares = familiares
        