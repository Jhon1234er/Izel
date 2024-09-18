from Empleados import*

class Capacitaciones(Empleados):
    def __init__(self, nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, Id, Fecha_Contratacion, Posicion_Id, Persona_Id,Titulo,Descripcion,Fecha,Empleado_id):
        super().__init__(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, Id, Fecha_Contratacion, Posicion_Id, Persona_Id)
        self.__id=Id
        self.__Titulo=Titulo
        self.__Descripcion=Descripcion
        self.__Fecha=Fecha
        self.__Empleado=Empleado_id
    
    def getid (self):
        return self.__id
    
    def getTitulo (self):
        return self.__Titulo
    
    def getDescripcion (self):
        return self.__Descripcion
    
    def getFecha (self):
        return self.__Fecha
    
    def getEmpleado (self):
        return self.__Empleado
    