from paciente import *
from conecct import *
from medico import *


Email = None

def Menu_Usuarios():
    global Email
    while True:
            print()
            print(Us,"HOLA USUARIO SOY IZEL!",Us)
            print()
            print("1- VER DATOS DEL PREFIL")
            print("2- VER HISTORIAL CLINICO")
            print("3- CERRAR SESION")
            ELEGIDO=int(input())
            match ELEGIDO:
                case 1:
                    perfil =Datos_Perfil(Email)
                    if perfil:
                        print(Us,"PERFIL",Us)
                        print(perfil)
                    else:
                        print(Us,"Perdon no pude encontrar lo que pedias",Us)
                case 2:
                    print()
                    print(Us,"¿QUE RESULTADO DESEA SABER?",Us)
                    print()
                    print("1- Mis Vacunas")
                    print("2- Mis Consultas")
                    print("3- Resultados Quirurgicos")
                    print("4- Ver Mis Datos Antropometricos")
                    print("5- Ver Mis Antecedentes Personales")
                    print("VOLVER")
                    RESULTADOS=int(input())
                    match RESULTADOS:
                        case 1:
                            vacunas = Datos_Vacunas(Email)
                            if vacunas:
                                print(Us,"MIS VACUNAS",Us)
                                for vacuna in vacunas:
                                    print(vacuna)
                            else :
                                print(Us,"Perdon no pude encontrar lo que pedias",Us)  
                        case 2:
                            consulta = Datos_Consulta(Email)
                            if consulta:
                                print(Us,"MIS CONSULTAS",Us)
                                for consultas in consulta:
                                    print(consultas)
                            else :
                                print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case 3:
                            proceso = Datos_Quirurgico(Email)
                            if proceso:
                                print(Us,"RESULTADOS QUIRURGICOS",Us)
                                for procesos in proceso:
                                    print(procesos)
                            else :
                                print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case 4:
                            antro = Datos_Antropometricos(Email)
                            if antro:
                                print(Us,"DATOS ANTROPOMETRICOS",Us)
                                for antropo in antro:
                                    print(antropo)
                            else :
                                print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case 5:
                            personales = Datos_Antecedentes(Email)
                            if personales:
                                print(Us,"MIS ANTECEDENTES",Us)
                                for personal in personales:
                                    print(personal)
                            else :
                                print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case _:
                            pass
                case 3:
                    print(Us,'IZEL SE DESPIDE',Us)
                    break

def Menu_Doctor():
    while True:
        print(Us,'Bienvenido a IZEL doctor, ¿En que trabajaremos hoy?',Us)
        print('1- Ingresar a consulta')
        print('2- Cerrar Sesion')
        opcionP=int(input('¿Que accion desea consultar?: '))
        match opcionP:
                case 1:
                    nro_doc =input('Ingrese el numero de documento del paciente: ')
                    print('1- Visualizar perfil del paciente')
                    print('2- Visualizar antecedentes del paciente')
                    print('3- Visualizar datos antropologicos')
                    print('4- Visualizar procesos quirurjicos')
                    print('5- Visualizaar historial de vacunacion')
                    print('6- Agregar datos a la consulta')
                    print('7- Agregar datos antropologicos a la consulta')
                    print('8- Ordenar una formula medica')
                    elecionConsulta=int(input('¿Que desea realizar?: '))
                    match elecionConsulta:
                        case 1:
                            perfil =Doctor_Paciente(nro_doc)
                            if perfil:
                                print(Us,"PERFIL PACIENTE",Us)
                                print(perfil)
                            else:
                                print(Us,"Perdon no pude encontrar lo que pedias",Us)                            
                        case 2:
                                personales = Datos_Antecedentes(nro_doc)
                                if personales:
                                    print(Us,"Antecedentes personales del paciente",Us)
                                    for personal in personales:
                                        print(personal)
                                else :
                                    print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case 3:
                                antro = Datos_Antropometricos(nro_doc)
                                if antro:
                                    print(Us,"Datos antropometricos del paciente",Us)
                                    for antropo in antro:
                                        print(antropo)
                                else:
                                    print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case 4:
                                proceso = Datos_Quirurgico(nro_doc)
                                if proceso:
                                    print(Us,"Procesos quirurjicos del paciente",Us)
                                    for procesos in proceso:
                                        print(procesos)
                                else :
                                    print(Us,"Perdon no pude encontrar lo que pedias",Us)
                        case 5:                     
                                vacunas = Datos_Vacunas(nro_doc)
                                if vacunas:
                                    print(Us,"Historial de vacunas del paciente",Us)
                                    for vacuna in vacunas:
                                        print(vacuna)
                                    else :
                                        print(Us,"Perdon no pude encontrar lo que pedias",Us)
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
                case 2:
                    print(Us,"FUE UN PLACER TRABAJAR CON USTED DOCTOR",Us)
                    break
def Menu_Auxiliar():
    while True:
        print()
        print(Us,"BIENVENIDO AUXILIAR, ¿EN QUE TE AYUDARE HOY?",Us)
        print()
        print("1- Registro Datos De Usuario")
        print("2- Salir")
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
                print(Us,"HOY FUE UN DIA CANSADO, NOS VEMOS MAÑANA :) ",Us)
                break
            
            
def Menu_Administrador():
    while True:
        print()
        print(Us,"BIENVENIDO SOY IZEL, ¿ERES DIOS?",Us)
        print()
        print("1- Ver Departamentos")
        print("2- Registrar a Medicos")
        print("3- Registrar Auxiliares")
        print("4- Llenar datos de empleados")
        print("5- Salir")
        Admin=int(input())
        match Admin:
            case 1:
                print()
                print(Us,"MIRE JEFE LOS DEPARTEMENTOS ACTIVOS",Us)
                print()
                print("1- ODONTOLOGIA")
                print("2- PEDIATRIA")
                print("3- DERMATOLOGIA")
                print("4- ORTOPEDIA Y TRAUMATOLOGIA")
                print("5- CIRUGIA")
                print("6- GINECOLOGIA")
                print("7- PSIQUIATRIA Y SALUD MENTAL")
                print("8- RADIOLOGIA")
                print("9- VOLVER")
                dep=int(input())
                match dep:
                    case 1:
                        print()
                        print(Us,"MEDICOS DE ODONTOLOGIA",Us)
                        print()
                        posicionId = 1122 
                        odontologos = Visualizar_Departamentos(posicionId)
                        if odontologos:
                                for odontologo in odontologos:
                                    print(f"Empleado_id: {odontologo['Empleado_id']}")
                                    print(f"Nombre: {odontologo['Nombre']}")
                                    print(f"Apellido: {odontologo['Apellido']}")
                                    print(f"Género: {odontologo['Genero']}")
                                    print(f"Correo: {odontologo['Correo']}")
                                    print(f"Teléfono: {odontologo['Telefono']}")
                                    print(f"Tipo de Documento: {odontologo['Tipo_Documento']}")
                                    print(f"Número de Documento: {odontologo['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {odontologo['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron odontólogos.",Us)                        
                    case 2:
                        print()
                        print(Us,"MEDICOS DE PEDIATRIA",Us)
                        print()
                        posicionId = 111 
                        pediatras = Visualizar_Departamentos(posicionId)
                        if pediatras:
                                for pediatra in pediatras:
                                    print(f"Empleado_id: {pediatra['Empleado_id']}")
                                    print(f"Nombre: {pediatra['Nombre']}")
                                    print(f"Apellido: {pediatra['Apellido']}")
                                    print(f"Género: {pediatra['Genero']}")
                                    print(f"Correo: {pediatra['Correo']}")
                                    print(f"Teléfono: {pediatra['Telefono']}")
                                    print(f"Tipo de Documento: {pediatra['Tipo_Documento']}")
                                    print(f"Número de Documento: {pediatra['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {pediatra['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Pediatras.",Us) 
                    case 3:
                        print()
                        print(Us,"MEDICOS DE DERMATOLOGIA",Us)
                        print()
                        posicionId = 112 
                        dermatologos = Visualizar_Departamentos(posicionId)
                        if dermatologos:
                                for dermatologo in dermatologos:
                                    print(f"Empleado_id: {dermatologo['Empleado_id']}")
                                    print(f"Nombre: {dermatologo['Nombre']}")
                                    print(f"Apellido: {dermatologo['Apellido']}")
                                    print(f"Género: {dermatologo['Genero']}")
                                    print(f"Correo: {dermatologo['Correo']}")
                                    print(f"Teléfono: {dermatologo['Telefono']}")
                                    print(f"Tipo de Documento: {dermatologo['Tipo_Documento']}")
                                    print(f"Número de Documento: {dermatologo['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {dermatologo['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Dermatologos.",Us)                         
                    case 4:
                        print()
                        print(Us,"MEDICOS DE ORTOPEDIA Y TRAUMATOLOGIA",Us)
                        print()
                        posicionId = 116
                        traumatologia = Visualizar_Departamentos(posicionId)
                        if traumatologia:
                                for ortopedia in traumatologia:
                                    print(f"Empleado_id: {ortopedia['Empleado_id']}")
                                    print(f"Nombre: {ortopedia['Nombre']}")
                                    print(f"Apellido: {ortopedia['Apellido']}")
                                    print(f"Género: {ortopedia['Genero']}")
                                    print(f"Correo: {ortopedia['Correo']}")
                                    print(f"Teléfono: {ortopedia['Telefono']}")
                                    print(f"Tipo de Documento: {ortopedia['Tipo_Documento']}")
                                    print(f"Número de Documento: {ortopedia['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {ortopedia['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Ortopedistas y Traumatologicos.",Us)
                    case 5:
                        print()
                        print(Us,"MEDICOS DE CIRUGIA",Us)
                        print()
                        posicionId = 114 
                        cirujanos = Visualizar_Departamentos(posicionId)
                        if cirujanos:
                                for cirujia in cirujanos:
                                    print(f"Empleado_id: {cirujia['Empleado_id']}")
                                    print(f"Nombre: {cirujia['Nombre']}")
                                    print(f"Apellido: {cirujia['Apellido']}")
                                    print(f"Género: {cirujia['Genero']}")
                                    print(f"Correo: {cirujia['Correo']}")
                                    print(f"Teléfono: {cirujia['Telefono']}")
                                    print(f"Tipo de Documento: {cirujia['Tipo_Documento']}")
                                    print(f"Número de Documento: {cirujia['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {cirujia['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Cirujanos.",Us)
                    case 6:
                        print()
                        print(Us,"MEDICOS DE GINECOLOGIA",Us)
                        print()
                        posicionId = 115
                        ginecologos = Visualizar_Departamentos(posicionId)
                        if ginecologos:
                                for ginecologia in ginecologos:
                                    print(f"Empleado_id: {ginecologia['Empleado_id']}")
                                    print(f"Nombre: {ginecologia['Nombre']}")
                                    print(f"Apellido: {ginecologia['Apellido']}")
                                    print(f"Género: {ginecologia['Genero']}")
                                    print(f"Correo: {ginecologia['Correo']}")
                                    print(f"Teléfono: {ginecologia['Telefono']}")
                                    print(f"Tipo de Documento: {ginecologia['Tipo_Documento']}")
                                    print(f"Número de Documento: {ginecologia['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {ginecologia['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Ginecologos.",Us)
                    case 7:
                        print()
                        print(Us,"MEDICOS DE PSIQUIATRIA Y SALUD MENTAL",Us)
                        print()
                        posicionId = 117
                        Psiquiatra = Visualizar_Departamentos(posicionId)
                        if Psiquiatra:
                                for mental in Psiquiatra:
                                    print(f"Empleado_id: {mental['Empleado_id']}")
                                    print(f"Nombre: {mental['Nombre']}")
                                    print(f"Apellido: {mental['Apellido']}")
                                    print(f"Género: {mental['Genero']}")
                                    print(f"Correo: {mental['Correo']}")
                                    print(f"Teléfono: {mental['Telefono']}")
                                    print(f"Tipo de Documento: {mental['Tipo_Documento']}")
                                    print(f"Número de Documento: {mental['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {mental['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Psiquiatras.",Us)
                    case 8: 
                        print()
                        print(Us,"MEDICOS DE RADIOLOGIA",Us)
                        print()
                        posicionId = 118 
                        radiologias = Visualizar_Departamentos(posicionId)
                        if radiologias:
                                for radiologia in radiologias:
                                    print(f"Empleado_id: {radiologia['Empleado_id']}")
                                    print(f"Nombre: {radiologia['Nombre']}")
                                    print(f"Apellido: {radiologia['Apellido']}")
                                    print(f"Género: {radiologia['Genero']}")
                                    print(f"Correo: {radiologia['Correo']}")
                                    print(f"Teléfono: {radiologia['Telefono']}")
                                    print(f"Tipo de Documento: {radiologia['Tipo_Documento']}")
                                    print(f"Número de Documento: {radiologia['Numero_Documento']}")
                                    print(f"Fecha de Nacimiento: {radiologia['Fecha_Nacimiento']}")
                                    print(Us)  
                        else:
                            print(Us,"No se encontraron Radiologos.",Us)
                    case 9:
                        pass
            case 2:
                print()
                print(Us,"REGISTRO DE CUENTAS MEDICAS",Us)
                print()
                print(Pon,"A CONTINUACIÓN ESCRIBA EL CORREO Y CONTRASEÑA DE LAS CUENTAS DE LOS MEDICOS NUEVOS",Pon)
                correo = input("Correo Electrónico: ")
                contraseña = input("Contraseña: ")
                tipo = input("Ingrese la especialidad del doctor: ")
                registrar_Cuenta(correo, contraseña, tipo)
                print(Us,"CUENTA CREADA CON EXITO, NUEVO MEDICO EN LA BASE DE DATOS ",Us)
            case 3:
                print()
                print(Us,"REGISTRO DE CUENTAS AUXILIARES",Us)
                print() 
                print(Pon,"A CONTINUACION ESCRIBA EL CORREO Y CONTRASEÑA DE LAS CUENTAS DE LOS AUXILIARES NUEVOS",Pon)
                correo = input("Correo Electrónico: ")
                contraseña = input("Contraseña: ")
                tipo = ("Auxiliar")
                registrar_Cuenta(correo, contraseña, tipo)
                print(Us,"CUENTA CREADA CON EXITO, NUEVO AUXILIAR EN LA BASE DE DATOS ",Us)
            case 4:
                print()
                print(Us,"REGISTRO DE DATOS SOBRE LOS EMPLEADOS",Us)
                print()
                print("1- Registrar datos personales")
                print("2- Registrar datos de contratacion")
                print("3- VOLVER")
                reg=int(input())
                match reg:
                    case 1:
                        print()
                        print(Us,"REGISTRO EMPLEADOS",Us)
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
                        try:
                            paciente = Paciente(nombre1, nombre2, apellido1, apellido2, genero, rh, correo, telefono, tipo_doc, nro_doc, fecha_nacimiento, tipo_poblacion, ocupacion, eps, Dirección)
                            Registrar_Usuario(paciente)
                            print('Registro exitoso')
                        except Exception as e:
                            print('Error al registrar',e)
                    case 2:
                        print()
                        print(Us,"REGISTRO DE CONTRATO",Us)
                        print()
                        Id = int(input("Ingrese id de reconocimiento: "))
                        Fecha_Contratacion = input("Digite la fecha actual: ")
                        Posicion_Id = int(input("Digite id la posicion a colocar: "))
                        Persona_Id = input ("Digite documento de la persona: ")
                        try:
                            contrato= Empleados(Id, Fecha_Contratacion, Posicion_Id, Persona_Id)
                            Registrar_Contrato(contrato)
                        except Exception as e:
                            print('Error al registrar',e)
                    case 3:
                        pass
            case 5:
                print(Us,"HASTA LA VISTA BEIBI >:c ",Us)
                break
            
            
            
            
Us= "-"*40
Imp= " "*40
Dec= " "*26
Pan= " "*28
Pon= " "*26
Inicio = 0 

while Inicio != 3:
        print()
        print(Imp,"BIENVENIDO A IZEL",Imp)
        print()
        print(Imp, "1. INICIAR SESION")
        print(Imp, "2. REGISTRARSE")
        print(Imp, "3. SALIR")
        Iniciar = int(input())
        match Iniciar:
            case 1:
                print()
                print(Imp," INICIAR SESION",Imp)
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
