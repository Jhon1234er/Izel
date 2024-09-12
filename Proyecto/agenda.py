class Agenda:
    def __init__(self,medico,tipo_cita,hora,fecha):
        self.__medico=medico
        self.__tipo_cita=tipo_cita
        self.__hora=hora
        self.__fecha=fecha
    
    def getMedico(self):
        return self.__medico
    def setMedico(self,medico):
        self.__medico=medico

    def getTipo_cita(self):
        return self.__tipo_cita
    def setTipo_cita(self,tipo_cita):
        self.__tipo_cita=tipo_cita

    def getHora(self):
        return self.__hora
    def setHora(self,hora):
        self.__hora=hora

    def getFecha(self):
        return self.__fecha
    def setFecha(self,fecha):
        self.__fecha=fecha
