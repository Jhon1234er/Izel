from datetime import datetime
from paciente import *
from conecct import *
import threading
import time
from medico import *

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
                            pass
                case 3:
                    print(Us,'IZEL SE DESPIDE',Us)
                    break

def Menu_Doctor():
    print ("Hamilton")
    while True:
        print('Bienvenido a IZEL doctor, ¿En que trabajaremos hoy?')
        print('1. Ingresar a consulta')
        print('2. Gestionar mi consultorio')
        print('3. Cerrar Sesion')
        opcionP=int(input('¿Que accion desea consultar?: '))
        while True:
            match opcionP:
                case 1:
                    nro_doc =input('Ingrese el numero de documento del paciente: ')
                    print('1. Visualizar perfil del paciente')
                    print('2. Visualizar antecedentes del paciente')
                    print('3. Visualizar datos antropologicos')
                    print('4. Visualizar procesos quirurjicos')
                    print('5. Visualizaar historial de vacunacion')
                    print('6. Agregar datos a la consulta')
                    print('7. Agregar datos antropologicos a la consulta')
                    print('8. Ordenar una formula medica')
                    elecionConsulta=int(input('¿Que desea realizar?: '))
                    match elecionConsulta:
                        case 1:
                            pass
                        case 2:
                                personales = Datos_Antecedentes(Numero)
                                if personales:
                                    print(Us, "Antecedentes personales del paciente")
                                    for personal in personales:
                                        print(personal)
                                else :
                                    print("NO SIRVO")
                        case 3:
                                antro = Datos_Antropometricos(Numero)
                                if antro:
                                    print(Us, "Datos antropometricos del paciente")
                                    for antropo in antro:
                                        print(antropo)
                                else:
                                    print("NO SIRVO")
                        case 4:
                                proceso = Datos_Quirurgico(Numero)
                                if proceso:
                                    print(Us, "Procesos quirurjicos del paciente")
                                    for procesos in proceso:
                                        print(procesos)
                                else :
                                    print("NO SIRVO")
                        case 5:                     
                                vacunas = Datos_Vacunas(Numero)
                                if vacunas:
                                    print(Us, "Historial de vacunas del paciente")
                                    for vacuna in vacunas:
                                        print(vacuna)
                                    else :
                                        print("NO SIRVO")
                        case 6:
                            print()
                            print(Us,'Agregar datos de la consulta',Us)
                            print()
                            descripcion_E=input('Ingrese la descripcion de la enfermedad: ')
                            motivo_C=input('Motivo de la consulta: ')
                            diagnostico=input('Diagnostico: ')
                            plan_Terap=input('Plan terapeutico: ')
                            epicrisis=input('Epicrisis: ')                                
                            nombre_A=input('Nombre del acompañante (si aplica): ')
                            parentesco_A=input('Parentesco acompañante si aplica: ')
                            conclusiones=input('Conclusiones de la consulta: ')
                        
                            try:
                                consultaInsert= Consulta(descripcion_E,motivo_C,diagnostico,plan_Terap,epicrisis,nombre_A,parentesco_A,conclusiones)
                                agregarDatosConsulta(nro_doc,consultaInsert)
                                print('Exitoso')
                            except Exception as e:
                                print('Error al guardar la consulta',e)

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
                nombre1 = input("Primer Nombre: ")
                nombre2 = input("Segundo Nombre: ")                
                apellido1 = input("Primer Apellido: ")
                apellido2 = input("Segundo Apellido: ")
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
                
                paciente = Paciente(nombre1, nombre2, apellido1, apellido2, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps, Dirección)
                
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
        print("5-Llenar datos de empleados")
        print("6-Salir")
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
                print("10-VOLVER")
                dep=int(input())
                match dep:
                    case 1:
                        print()
                        print("MEDICOS DE ODONTOLOGIA")
                        print()
                    case 2:
                        print()
                        print("MEDICOS DE PEDIATRIA")
                        print()
                    case 3:
                        print()
                        print("MEDICOS DE DERMATOLOGIA")
                        print()
                    case 4:
                        print()
                        print("MEDICOS DE ORTOPEDIA")
                        print()
                    case 5:
                        print()
                        print("MEDICOS DE CIRUGIA")
                        print()
                    case 6:
                        print()
                        print("MEDICOS DE GINECOLOGIA")
                        print()
                    case 7:
                        print()
                        print("MEDICOS DE ORTOPEDIA Y TRAUMATOLOGIA")
                        print()
                    case 8:
                        print()
                        print("MEDICOS DE PSIQUIATRIA Y SALUD MENTAL")
                        print()
                    case 9: 
                        print()
                        print("MEDICOS DE RADIOLOGIA")
                        print()
                    case 10:
                        pass
            case 3:
                print()
                print("REGISTRO DE CUENTAS MEDICAS")
                print()
                print("A CONTINUACIÓN ESCRIBA EL CORREO Y CONTRASEÑA DE LAS CUENTAS DE LOS MEDICOS NUEVOS")
                correo = input("Correo Electrónico: ")
                contraseña = input("Contraseña: ")
                tipo = input("Ingrese la especialidad del doctor: ")
                registrar_Cuenta(correo, contraseña, tipo)
                print(Us,"CUENTA CREADA CON EXITO, NUEVO MEDICO EN LA BASE DE DATOS ",Us)
            case 4:
                print()
                print("REGISTRO DE CUENTAS AUXILIARES")
                print() 
                print("A CONTINUACION ESCRIBA EL CORREO Y CONTRASEÑA DE LAS CUENTAS DE LOS AUXILIARES NUEVOS")
                correo = input("Correo Electrónico: ")
                contraseña = input("Contraseña: ")
                tipo = ("Auxiliar")
                registrar_Cuenta(correo, contraseña, tipo)
                print(Us,"CUENTA CREADA CON EXITO, NUEVO AUXILIAR EN LA BASE DE DATOS ",Us)
            case 5:
                print()
                print("REGISTRO DE DATOS SOBRE LOS EMPLEADOS")
                print()
                print("1-Registrar datos personales")
                print("2-Registrar datos de contratacion")
                print("3-Si tiene capacitaciones")
                print("4-VOLVER")
                reg=int(input())
                match reg:
                    case 1:
                        print()
                        print(Us,"REGISTRO USUARIO",Us)
                        print()
                        nombre1 = input("Primer Nombre: ")
                        nombre2 = input("Segundo Nombre: ")                
                        apellido1 = input("Primer Apellido: ")
                        apellido2 = input("Segundo Apellido: ")
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
                        
                        paciente = Paciente(nombre1, nombre2, apellido1, apellido2, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps, Dirección)
                        
                        Registrar_Usuario(paciente)
                    case 2:
                        print()
                        print("REGISTRO DE CONTRATO")
                        print()
                        identifacion_E = int(input("Ingrese id de reconocimiento: "))
                        Fecha = input("Digite la fecha actual")
                        Posicion = int(input("Digite id la posicion a colocar"))
                        Persona = input ("Digite documento de la persona")
                        
                        contrato= Empleados(identifacion_E, Fecha, Posicion, Persona)
                        
                        Registrar_Contrato(contrato)
                    case 3:
                        print("PROXIMAMENTE")
                        
                    case 4: 
                        pass
            case 6:
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
                tipo = ("Usuario")
                registrar_Cuenta(correo, contraseña, tipo)
                print(Us,"Registro exitoso. Ahora puedes iniciar sesión.",Us)
            case 3:
                print(Us,"Gracias por usar IZEL",Us)
                break
                
                

    
