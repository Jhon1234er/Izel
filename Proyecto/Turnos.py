from Empleados import*

class Turnos (Empleados):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, Id, Fecha_Contratacion, Posicion_Id, Persona_Id,Turnos_id,Fecha_Inicio,Fecha_Fin):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, Id, Fecha_Contratacion, Posicion_Id, Persona_Id)
        self.__Turnos=Turnos_id
        self.__Fecha_I=Fecha_Inicio
        self.__Fecha_F=Fecha_Fin
        
    def getTurno (self):
        return self.__Turnos
    
    def getInicio (self):
        return self.__Fecha_I
    
    def getFin (self):
        return self.__Fecha_F