from datetime import datetime
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

                            
                        case 7:
                            print()
                            print(Us,'Agregar datos antropologicos de la consulta',Us)
                            print()
                            peso=input('Peso del paciente: ')
                            talla=input('Talla del paciente: ')
                            imc=input('IMC del paciente: ')
                            temperatura=input('Temperatura del paciente: ')
                            pulso=input('Pluso del paciente: ')
                            frecuencia_R=input('Frecuencia respiratoria del paciente: ')
                            presion_A=input('Presion arterial del paciente: ')
                            try:
                                datosATPInsert=antropometricos(talla,temperatura,imc,pulso, peso, frecuencia_R, presion_A)
                                agregarDatosATP(nro_doc,datosATPInsert)
                                print('Exitoso')
                            except:
                                print('Error al insertar los datos')
                        case 8:
                            print()
                            print(Us,'Formula Médica',Us)
                            print()
                            codigo_F=input('Codigo formula: ')
                            medicamento=input('Nombre del medicamento: ')
                            cantidad=input('Cantidad de la medicacion: ')
                            duracion=input('Duracion del tratamiento: ')
                            concentracion=input('Concentracion del medicamento: ')
                            indicaciones=input('Indicaciones del tratamiento: ')
                            via_Administracion=input('Via de administracion del tratamiento: ') 

                            formulaInsert= FormulaMedica(codigo_F,cantidad,duracion,concentracion,medicamento,indicaciones,via_Administracion)
                            agregarFormula(nro_doc,formulaInsert)
                            try: 
                                print('Exitoso')
                            except:
                                print('Error al generar la formula')
                                                
                case 2:
                    print('1. Gestionar consultorio')
                    print('2. Visualizar mi consultorio')
                case 3:
                    print('Sesion cerrada exitomanete, hasta pronto')
                
            


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
                        

            case 2:
                print("Regístrate aquí:")
                correo = input("Correo Electrónico: ")
                contraseña = input("Contraseña: ")
                tipo = input("Tipo de Usuario (Usuario/Doctor): ")
                registrar_usuario(correo, contraseña, tipo)
                print("Registro exitoso. Ahora puedes iniciar sesión.")
            case 3:
                print("Gracias por usar IZEL. ¡Hasta luego!")
                break
                
                

    
