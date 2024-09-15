from datetime import datetime
from conecct import *
from registro import*
import threading
import time



# def tiempo():
#     while True:
#         ahora=datetime.now().strftime("%H:%M:%S")
#         print(f'\r Hora actural: {ahora}', end="")
#         time.sleep(1)

Imp= " "*40
Dec= " "*26
Pan= " "*28
Pon= "-"*26
Inicio = 0 
while Inicio!=4:
        print(Imp,"BIENVENIDO A IZEL")
        print(Imp," INICIAR SESION")
        print()
        print(Dec,"Correo Electronico")
        Email=input(Pon)
        print(Pan,"Contraseña")
        Pin=input(Pon)
        
        print("estoy bien", Email,Pin)

        nombre1 = verificar (Email,Pin)

        print("yo tambien", nombre1)
                
        if nombre1:
            print(f"IZEL TE DA LA BIENVENIDA, {nombre1}! ")
            
match Inicio:
            case 1:
                pass
            case 2:
               pass
            case 3:
                pass
            case 4:
                print(decoracion,'GRACIAS POR USAR INFITY',decoracion)
                
