class consulta:
    def __init__(self, descripcion_E, motivo_C, diagnostico, plan_Terap,
                 epicrisis, nombre_A, parentesco_A, consulciones):
        self.__Descripcion = descripcion_E
        self.__Motivo = motivo_C
        self.__Diagnostico = diagnostico
        self.__PlanTerapia = plan_Terap
        self.__Epicrisis = epicrisis
        self.__Nombre_A = nombre_A
        self.__Parentesco_A = parentesco_A
        self.__Consultas = consulciones
    
    def getDescripcion(self):
        return self.__Descripcion
    
    def setDescripcion(self, descripcion_E):
        self.__Descripcion = descripcion_E 
    
    def getMotivo(self):
        return self.__Motivo
    
    def setMotivo(self, motivo_C):
        self.__Motivo = motivo_C
    
    def getDiagnostico(self):
        return self.__Diagnostico
    
    def setDiagnostico(self, diagnostico):
        self.__Diagnostico = diagnostico
    
    def getPlanTerapia(self):
        return self.__PlanTerapia
    
    def setPlanTerapia(self, plan_Terap):
        self.__PlanTerapia = plan_Terap
    
    def getEpicrisis(self):
        return self.__Epicrisis
    
    def setEpicrisis(self, epicrisis):
        self.__Epicrisis = epicrisis
    
    def getNombre_A(self):
        return self.__Nombre_A
    
    def setNombre_A(self, nombre_A):
        self.__Nombre_A = nombre_A
    
    def getParentesco_A(self):
        return self.__Parentesco_A
    
    def setParentesco_A(self, parentesco_A):
        self.__Parentesco_A = parentesco_A
    
    def getConsultas(self):
        return self.__Consultas
    
    def setConsultas(self, consulciones):
        self.__Consultas = consulciones
        