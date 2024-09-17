from datetime import datetime
from paciente import *
from conecct import *
import threading
import time


# def tiempo():
#     while True:
#         ahora=datetime.now().strftime("%H:%M:%S")
#         print(f'\r Hora actural: {ahora}', end="")
#         time.sleep(1)

def Menu_Usuarios():
    while True:
            print()
            print(Us,"HOLA USUARIO SOY IZEL!",Us)
            print()
            print("VER DATOS DEL PREFIL")
            print("VER HISTORIAL CLINICO")
            print("CERRAR SESION")
            ELEGIDO=int(input())
            match ELEGIDO:
                case 1:
                    print(Us,"PREFIL",Us)
                case 2:
                    print()
                    print(Us,"¿QUE RESULTADO DESEA SABER?",Us)
                    print()
                    print("1. Mis Vacunas")
                    print("2. Mis Consultas")
                    print("3. Resultados Quirurgicos")
                    print("4. Ver Mis Datos Antropometricos")
                    print("5. Ver Mis Antecedentes Personales")
                    print("VOLVER")
                    RESULTADOS=int(input())
                    match RESULTADOS:
                        case 1:
                            Numero = input("DIGITE SU NUMERO DE DOCUMENTO: ")
                            vacunas = Datos_Vacunas(Numero)
                            if vacunas:
                                print(Us, "MIS VACUNAS")
                                for vacuna in vacunas:
                                    print(vacuna)
                            else :
                                print("NO SIRVO")  
                        case 2:
                            Numero = input("DIGITE SU NUMERO DE DOCUMENTO: ")
                            consulta = Datos_Consulta(Numero)
                            if consulta:
                                print(Us, "MIS CONSULTAS")
                                for consultas in consulta:
                                    print(consultas)
                            else :
                                print("NO SIRVO")
                        case 3:
                            Numero = input("DIGITE SU NUMERO DE DOCUMENTO: ")
                            proceso = Datos_Quirurgico(Numero)
                            if proceso:
                                print(Us, "RESULTADOS QUIRURGICOS")
                                for procesos in proceso:
                                    print(procesos)
                            else :
                                print("NO SIRVO")
                        case 4:
                            Numero = input("DIGITE SU NUMERO DE DOCUMENTO: ")
                            antro = Datos_Antropometricos(Numero)
                            if antro:
                                print(Us, "DATOS ANTROPOMETRICOS")
                                for antropo in antro:
                                    print(antropo)
                            else :
                                print("NO SIRVO")
                        case 5:
                            Numero = input("DIGITE SU NUMERO DE DOCUMENTO: ")
                            personales = Datos_Antecedentes(Numero)
                            if personales:
                                print(Us, "MIS ANTECEDENTES")
                                for personal in personales:
                                    print(personal)
                            else :
                                print("NO SIRVO")
                        case 6:
                            print("PONGA UNA SALIDA HP PEREZOSO")
                case 3:
                    print(Us,'IZEL SE DESPIDE',Us)
                    break
def Menu_Doctor():
    print ("hamilton")

def Menu_Auxiliar():
    while True:
        print()
        print(Us,"BIENVENIDO AUXILIAR, ¿EN QUE TE AYUDARE HOY?")
        print()
        print("1-Registro Datos De Usuario")
        print("2-PROXIMAMENTE")
        print("3-Salir")
        Aux=int(input())
        match Aux :
            case 1:
                print()
                print(Us,"REGISTRO USUARIO",Us)
                print()
                nombres = input("Nombres: ")
                apellidos = input("Apellidos: ")
                genero = input("Genero: ")
                rh = input("RH: ")
                correo = input("Correo Electrónico: ")
                telefono = input("Teléfono: ")
                tipo_doc = input("Tipo de Documento: ")
                nro_doc = input("Número de Documento: ")
                fecha_nacimiento = input("Fecha de Nacimiento (AÑO-MES-DIA): ")
                tipo_poblacion = input("Tipo de Población: ")
                ocupacion = input("Ocupación: ")
                eps = input("EPS: ")
                Dirección = input("Dirección: ")
                
                paciente = Paciente(nombres, apellidos, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps, Dirección)
                
                Registrar_Usuario(paciente)
            case 2:
                print("OYE DEJAME TRABAJAR ESPERATE HASTA LA PROXIMA ACTUALIZACIÓN!!! ATT: IZEL")
            case 3:
                print(Us,"HOY FUE UN DIA CANSADO, NOS VEMOS MAÑANA :) ",Us)
                break
            
            
def Menu_Administrador():
    while True:
        print()
        print(Us,"BIENVENIDO SOY IZEL, ¿ERES DIOS?")
        print()
        print("1-Registrar Turnos")
        print("2-Ver Departamentos")
        print("3-Registrar a Medicos")
        print("4-Registrar Auxiliares")
        print("5-Salir")
        Admin=int(input())
        match Admin:
            case 1:
                print()
                print("MENU TURNOS")
                print()
            case 2:
                print()
                print("MIRE JEFE LOS DEPARTEMENTOS ACTIVOS")
                print()
                print("1-ODONTOLOGIA")
                print("2-PEDIATRIA")
                print("3-DERMATOLOGIA")
                print("4-ORTOPEDIA")
                print("5-CIRUGIA")
                print("6-GINECOLOGIA")
                print("7-ORTOPEDIA Y TRAUMATOLOGIA")
                print("8-PSIQUIATRIA Y SALUD MENTAL")
                print("9-RADIOLOGIA")
            case 3:
                print()
                print("REGISTRO DE CUENTAS MEDICAS")
                print()
            case 4:
                print()
                print("REGISTRO DE CUENTAS AUXILIARES")
                print() 
            case 5:
                print("HASTA LA VISTA BEIBI >:c ")
                break
            
            
            
            
Us= "-"*40
Imp= " "*40
Dec= " "*26
Pan= " "*28
Pon= " "*26
Inicio = 0 

while Inicio != 3:
        print()
        print(Imp, "BIENVENIDO A IZEL")
        print()
        print(Imp, "1. INICIAR SESION")
        print(Imp, "2. REGISTRARSE")
        print(Imp, "3. SALIR")
        Iniciar = int(input())
        match Iniciar:
            case 1:
                print()
                print(Imp," INICIAR SESION")
                print()
                print(Dec,"Correo Electronico")
                Email=input(Pon)
                print(Pan,"Contraseña")
                Pin=input(Pon)

                        
                if verificar(Email,Pin):
                    Tipo=tipo_usuario(Email)
                    if Tipo=="Usuario":
                        Menu_Usuarios()
                    elif Tipo=="Doctor":
                        Menu_Doctor()
                    elif Tipo=="Auxiliar":
                        Menu_Auxiliar()
                    elif Tipo=="Administrador":
                        Menu_Administrador()

            case 2: 
                print("Regístrate aquí:")
                correo = input("Correo Electrónico: ")
                contraseña = input("Contraseña: ")
                tipo = input("Tipo de Usuario (Usuario/Doctor): ")
                registrar_Cuenta(correo, contraseña, tipo)
                print(Us,"Registro exitoso. Ahora puedes iniciar sesión.",Us)
            case 3:
                print(Us,"Gracias por usar IZEL",Us)
                break
                
                

    
