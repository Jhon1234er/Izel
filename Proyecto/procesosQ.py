class Quirurgicos:
    def __init__(self, descripcion, informe_Anes, fecha_P, lugar_P):
        self.__Descripcion = descripcion
        self.__Anestecia = informe_Anes
        self.__Fecha_P = fecha_P
        self.__Lugar_P = lugar_P
    
    def getDescripcion(self):
        return self.__Descripcion
    
    def setDescripcion(self, descripcion):
        self.__Descripcion = descripcion
    
    def getAnestecia(self):
        return self.__Anestecia
    
    def setAnestecia(self, informe_Anes):
        self.__Anestecia = informe_Anes
    
    def getFecha_P(self):
        return self.__Fecha_P
    
    def setFecha_P(self, fecha_P):
        self.__Fecha_P = fecha_P
    
    def getLugar_P(self):
        return self.__Lugar_P
    
    def setLugar_P(self, lugar_P):
        self.__Lugar_P = lugar_P
        