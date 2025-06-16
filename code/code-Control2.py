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
#                                                                                                        #
#                Código para obtener la Mac Address del IdeaBoard                                        #
#                     import wifi                                                                        #
#                     mac_address = wifi.radio.mac_address                                               #
#                     print("MAC Address:", mac_address)                                                 #
#                                                                                                        #
#                                                                                                        #
#                                                                                                        #
##########################################################################################################


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
sumo1 = mac_z #reemplazar con la MAC address del sumobot.


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
    





