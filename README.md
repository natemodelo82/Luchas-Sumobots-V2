# Luchas-Sumobots-V2

##########################################################################################################
#                                                                                                        #
#                                                                                                        #
#                                                                                                        #
#                                             ______                                                     #
#                                            /   \  @@  \                                                #
#                                           /       \ %# @  \                                            #
#                                          /    (_)    \ % @   \                                         #
#                                         /         (_)   \ _____                                        #
#                                        /                /      |                                       #
#                                        \               /       |                                       #
#                                          \            /     __ |                                       #
#                                              \       /     /  |                                        #
#                                                 \   /-  - -\__/                                        #
#                                                                                                        #
#                               ___                       __         ___________                         #
#                             / ___|| | | |  \/  |/ _ \ | __ )  / _ \__   __/ ___|                       #
#                             \___ \| | | | |\/| | | | ||  _ \ | | | | | |  \___ \                       #
#                              ___) | |_| | |  | | |_| || |_) || |_| | | |   ___) |                      #
#                             |____/ \___/|_|  |_|\___/ |____/  \__ /  | |  |____/                       #                                                #
#                                                                                                        #
#                                                                                                        #
#   Código para el sumobot controlable por ESPNOW, basado en el proyecto  Sumobot Universidad Cenfotec   #
#                  https://github.com/Universidad-Cenfotec/Sumobot                                       #
#                                                                                                        #
#                                                                                                        #
#                          Colegio Técnico Profesional de Oreamuno                                       #
#                                    Informática Empresarial                                             #
#                                    Cibersegurdad                                                       #
#                                    Informática en Desarrollo Móvil                                     #
#                                                                                                        #
#                               Integrantes:                                                             #
#                                                                                                        #
#                                  - Montenegro Araya Manfred                                            #
#                                  - Mora Torres Jazmín                                                  #
#                                  - Ramírez Guzmán Celeste                                              #
#                                  - Vega Camacho María José                                             #
#                                  - Guerrero Zelaya Fabian                                              #
#                                  - Cedeño Guillen Sebastián                                            #                             
#                                  - Aguilar Aguilar Dereck                                              #
#                                  - Gómez Garita Nathaly Teresita                                       # 
#                                  - Segura Alvarado Daniel                                              #
#                                  - Hidalgo Arce Joshua                                                 #
#                                                                                                        #  
#                               Profesor Tutor:                                                          #
#                                    Ronald Fallas Rojas                                                 #
#                                                                                                        #
#                                        Año: 2025                                                       #
#                                      Versión: 1.0                                                      #
#                                                                                                        #
#                                                                                                        #
##########################################################################################################


El código fue creado con el fin de poder controlar un sumobot por medio del protocolo ESP NOW.
Las tarjetas que se utilizaron para el proyecto corresponden con IdeaBoards de CRCibernética.
Toda la codificación fue hecha en CircuitPython.

Al utilizar el protocolo ESP NOW, se pueden controlar hasta 10 tarjetas Ideaboard por medio de otra tarjeta Ideaboard que funciona como Servidor.
Esta conexión se hace por medio de las direcciones MAC de las tarjetas Clientes.

Para saber cuál es la dirección MAC de las tarjetas se utilizó el siguiente código:

#    Código para obtener la Mac Address del IdeaBoard                                               
import wifi
mac_address = wifi.radio.mac_address
print("MAC Address:", mac_address)

Una vez se tiene la dirección MAC de la tarjeta cliente, se puede agregar al código del Servidor (control)

from ideaboard import IdeaBoard
from time import sleep
import board
import sys
import espnow #libreria para comunicarse con otro IdeaBoard
import keypad

mac_x = b'\x08:\x8d\x8e3\xc0'
mac_z = b'\x80do\x110<'


mac_a = b'\x08:\x8d\x8e4h'
mac_b = b'\x80do\x10\xf6\xc0'
sumo1 = mac_z  #cambiar por la dirección MAC del dispositivo que se quiere controlar


tiempoEspera = 0.1
tiempoInicio = 1

ib = IdeaBoard()
e = espnow.ESPNow()
sumobot = espnow.Peer(mac=sumo1)
e.peers.append(sumobot)

#botones            Golpe          derecha     abajo      izquierda     arriba
keys = keypad.Keys((board.IO27, board.IO33, board.IO32, board.IO25, board.IO26,), value_when_pressed=False, pull=True)

#
#Envia un mensaje al otro Ideaboard usando el protocolo espnow
def enviarMensajeSumobot(mensaje):
    e.send(mensaje)

sleep(tiempoInicio)

while True:
    
    event = keys.events.get()
    if event:
        if event.pressed:
            if (event.key_number == 4):
                print("Arriba")
                enviarMensajeSumobot("arriba")
            if (event.key_number == 2):
                print("Abajo")
                enviarMensajeSumobot("abajo")
            if (event.key_number == 3):
                print("Izquierda")
                enviarMensajeSumobot("izquierda")
            if (event.key_number == 1):
                print("Derecha")
                enviarMensajeSumobot("derecha")
            if (event.key_number == 0):
                print("Rojo")
                enviarMensajeSumobot("rojo")
                
            print(event)

    sleep(tiempoEspera)


Luego de configurar el código del Servidor con la dirección MAC del Cliente, se puede proceder a subirlo a la Tarjeta Ideaboard que trabajará como control.

Ahora se puede proceder a subir el código en el sumobot, que en este caso funcionará como cliente.

Este código no requiere de cambios para funcionar.

El orden de encendido recomendado es primero encender el cliente y luego el Servidor (control).

Dependiendo del botón que se presione en el IdeaBoard Servidor, se iluminará el LED en el IdeaBoard cliente, siguiendo el siguiente patrón:
     #DERECHA amarillo, IZQUIERDA violeta, ABAJO turquesa, ARRIBA azul, ROJO ataque
     
Además de encender las luces, los botones activan las funciones de movimiento en el Sumobot.

Para poder ver los motores funcionar, es necesario que se conecte una fuente de poder externa además del cable USB para pasar datos.
    
