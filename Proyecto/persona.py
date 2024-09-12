class Persona:
    def __init__(self,nombres,apellidos,genero,rh,correo,telefono,tipo_doc,nro_doc,fecha_nacimiento,tipo_poblacion,ocupacion):
        
        self.__nombres=nombres
        self.__apellidos=apellidos
        self.__genero=genero
        self.__rh=rh
        self.__correo=correo
        self.__telefono=telefono
        self.__tipo_doc=tipo_doc
        self.__nro_doc=nro_doc
        self.__fecha_nacimiento=fecha_nacimiento
        self.__tipo_poblacion=tipo_poblacion
        self.__ocupacion=ocupacion
        
    def getNombres(self):
        return self.__nombres
    def setNombres(self,nombres):
        self.__nombres=nombres
    
    def getApellidos(self):
        return self.__apellidos
    def setApellidos(self,apellidos):
        self.__apellidos=apellidos
        
    def getGenero(self):
        return self.__genero
    def setGenero(self,genero):
        self.__genero=genero
        
    def getRH(self):
        return self.__rh
    def setRH(self,rh):
        self.__rh=rh
        
    def getCorreo(self):
        return self.__correo
    def setCorreo(self,correo):
        self.__correo=correo
        
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,telefono):
        self.__telefono=telefono
        
    def getTipo_doc(self):
        return self.__tipo_doc
    def setTipo_doc(self,tipo_doc):
        self.__tipo_doc=tipo_doc

    def getNro_doc(self):
        return self.__nro_doc
    def setNro_doc(self,nro_doc):
        self.__nro_doc=nro_doc
        
    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento
    def setFecha_nacimiento(self,fecha_nacimiento):
        self.__fecha_nacimiento=fecha_nacimiento
        
    def getTipo_poblacion(self):
        return self.__tipo_poblacion
    def setTipo_poblacion(self,tipo_poblacion):
        self.__tipo_poblacion=tipo_poblacion
        
    def getOcupacion(self):
        return self.__ocupacion
    def setOcupacion(self,ocupacion):
        self.__ocupacion=ocupacion