from registro import*
doctor=4321
usuario=5423
decoracion=' '*40
stop=0
import time
from datetime import datetime

def tiempo():
    while True:
        ahora=datetime.now().strftime("%H:%M:%S")
        print(f'\r Hora actural: {ahora}', end="")
        time.sleep(1)
        

inicio=0
def existencia(email, clave):
    with open('infinity/Proyecto/cuentas.txt', 'r') as info:
        for i in info:
            if i.strip() == f"{email} {clave}":
                return True
    return False
while inicio!=4:
        print(decoracion,'BIENVENIDO A INFINITY',decoracion)
        print('1. INICIAR SESION COMO USUARIO')
        print('2. INICIAR SESION COMO DOCTOR')
        print('3. REGISTRARSE')
        print('4. SALIR DEL PROGRAMA')
        inicio=int(input("Ingrese Opcion: "))
        match inicio:
            case 1:

                print(decoracion,'INICIO DE SESION USUARIO',decoracion)
                email=input('Ingrese su correo: ')
                clave=input('Ingrese su contraseña: ')
                if existencia(email,clave):
                    codigoUsuario=int(input('Ingrese el dodigo de verificacion: '))
                    if  codigoUsuario == usuario:
                        while True:
                            print(decoracion,'BIENVENIDO USUARIO A INFITY',decoracion)
                            tiempo()
                            
                            print('1.Ver Historia Clinica')
                            print('2.Cerrar Sesion')
                            opcion=int(input('¿Que quiere realizar: '))
                            match opcion:
                                case 1:
                                    with open('antecedentes.txt', 'datosATP.txt', 'procesosQ.txt','vacunacion.txt','r') as personal:
                                        ident=input('Digite su Numero de Identificacion')    
                                    for i in personal:
                                        numdoc,patologicos, quirurgicos, alegricos,ginecologicos,obstreticos, framalogicos, familiares= i.strip().split(':')
                                        if numdoc == ident:
                                            print(i.strip())  
                                    else:
                                        print(decoracion,'El Numero de Documento Ingresado No Se Encuentra.',decoracion)
                                case 2:
                                     print(decoracion,'CERRANDO SESION',decoracion)
                                     break
                    else:
                        print(decoracion,'Codigo incorrecto',decoracion)
                else:
                    print(decoracion,'Correo o contraseña incorrectos',decoracion)
            case 2:
                print(decoracion,'INICIO DE SESION DOCTOR',decoracion)
                email=input('Ingrese su correo: ')
                clave=input('Ingrese su contraseña: ')
                if existencia(email,clave):
                    codigoDoc=int(input('Ingrese el codigo de verificacion: '))
                    if codigoDoc == doctor:
                        while True:
                            print(decoracion,'BIENVENDO DOCTOR A INFINITY',decoracion)
                            print('1. Ingresar a consulta')
                            print('2. Gestionar mi consultorio')
                            print('3. Cerrar Sesion')
                            opcionP=int(input('¿Que accion desea consultar?: '))
                            while True:
                                match opcionP:
                                    case 1:
                                        numueroPac=int(input('Ingrese el numero de documento del paciente: '))
                                        print('1. Visualizar perfil del paciente')
                                        print('2. Visualizar antecedentes del paciente')
                                        print('3. Visualizar datos antropologicos')
                                        print('4. Visualizar procesos quirurjicos')
                                        print('5. Visualizaar historial de vacunacion')
                                        print('6. Agregar datos a la consulta')
                                        print('7. Agregar datos antropologicos a la consulta')
                                        print('8. Ordenar una formula medica')
                                        elecionConsulta=int(input('¿Que desea realizar?'))
                                        while True:
                                            match elecionConsulta:
                                                case 1:
                                                    with open('perfilpaciente.txt', 'r') as f:
                                                         contenido=f.readlines()
                                                         print(contenido)
                                                case 2:
                                                    with open('antecedentes.txt', 'r') as f:
                                                         contenido=f.readlines()
                                                         print(contenido)
                                                case 3:
                                                    with open('datosATP.txt', 'r') as f:
                                                     contenido=f.readlines()
                                                     print(contenido)
                                                case 4:
                                                    with open('procesosQ.txt', 'r') as f:
                                                     contenido=f.readlines()
                                                     print(contenido)
                                                case 5:
                                                     with open('vacunacion.txt', 'r') as f:
                                                         contenido=f.readlines()
                                                         print(contenido)
                                                case 6:
                                                    
                                                    descripcion_E=input('Descripcion de la consulta')
                                                    motivo_C=input('Motivo de la consulta')
                                                    diagnostico=input('Diagnostico de la consulta')
                                                    plan_Terap=input('Plan terapia de la consulta')
                                                    epicrisis=input('Epicrisis de la consulta')
                                                    nombre_A=input('Nombre del acompañante,si aplica')
                                                    parentesco_A=input('Parentesco del aompañante,si aplica')
                                                    consulciones=input('Conclusiones de la consulta')
                                                    consul= f'{descripcion_E} {motivo_C} {motivo_C} {plan_Terap} {epicrisis} {nombre_A} {parentesco_A} {consulciones}  \n'
                                                    with open('consulta.txt','a') as f:
                                                        f.write(f'{numueroPac}:{consul}\n')
                                                        print('Consulta agregada exitosamente')
                                                        
                                                case 7:
                                               
                                                    talla=input('Talla del paciente')
                                                    temperatura=input('Temperatura del paciente')
                                                    imc=input('IMC del paciente')
                                                    pluso=input('Pluso del paciente')
                                                    peso=input('Peso del paciente')
                                                    frecuencia_R=input('Frecuencia respiratoria del paciente')
                                                    presion_A=input('Presion arterial del paciente')
                                                    atp= f'{talla} {temperatura} {imc} {pluso} {peso} {frecuencia_R} {presion_A} \n'
                                                    with open('datosATP.txt','a') as f:
                                                        f.write(f'{numueroPac}:{atp}\n')
                                                        print('Datos antropologicos agregados exitosamente')

                                                case 8: 
                                                  
                                                    codigo_F=input('Codigo formula')
                                                    cantidad=input('Cantidad de la medicacion')
                                                    duracion=input('Duracion del tratamiento')
                                                    concentracion=input('Concentracion del medicamento')
                                                    medicamento=input('Nombre del medicamento')
                                                    indicaciones=input('Indicaciones del tratamiento')
                                                    via_Administracion=input('Via de administracion del tratamiento')
                                                    formula= f'{codigo_F} {cantidad} {duracion} {concentracion} {medicamento} {indicaciones} {via_Administracion} \n'
                                                    with open('formula.txt','a') as f:
                                                        f.write(f'{numueroPac}:{formula}\n')
                                                        print('Formula medica agregada exitosamente')
                                    case 2:
                                        print('1. Gestionar consultorio')
                                        print('2. Visualizar mi consultorio')
                                    case 3:
                                        print('Sesion cerrada exitomanete, hasta pronto')
                    else:
                        print(decoracion,'Codigo incorrecto',decoracion)
                else:
                    print(decoracion,'Correo o contraseña incorrectos',decoracion)
            case 3:
                print(decoracion,'REGISTRO DE CUENTA',decoracion)
                email=input('Ingrese su Correo: ')
                # numDoc=input('Ingrese su Numero de Documento: ')
                clave=input('Ingrese su contraseña: ')
                cuenta= Registro (email,clave)
                print(decoracion,'SU CUENTA HA SIDO CREADA CON EXITO',decoracion)
                info=f'{email} {clave}'
                with open("cuentas.txt", "a") as Datos:
                    Datos.write(f'{info}\n')

            case 4:
                print(decoracion,'GRACIAS POR USAR INFITY',decoracion)
                
