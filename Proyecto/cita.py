class cita :
    def __init__(self, codigo_Cita, descripcion, sede_Atencion, recomendaciones):
        self.__Codigo_Cita = codigo_Cita
        self.__Descripcion = descripcion
        self.__Sede_Atencion = sede_Atencion
        self.__Recomendaciones = recomendaciones
    
    def get_codigo_Cita(self):
        return self.__Codigo_Cita
    
    def set_codigo_Cita(self, codigo_Cita):
        self.__Codigo_Cita = codigo_Cita
    
    def get_descripcion(self):
        return self.__Descripcion
    
    def set_descripcion(self, descripcion):
        self.__Descripcion = descripcion
    
    def get_sede_Atencion(self):
        return self.__Sede_Atencion
    
    def set_sede_Atencion(self, sede_Atencion):
        self.__Sede_Atencion = sede_Atencion
    
    def get_recomendaciones(self):
        return self.__Recomendaciones
    
    def set_recomendaciones(self, recomendaciones):
        self.__Recomendaciones = recomendaciones