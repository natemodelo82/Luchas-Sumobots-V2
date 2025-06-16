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
#                             |____/ \___/|_|  |_|\___/ |____/  \__ /  | |  |____/                       #
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
#                                  - Soto Torres Jazmín                                                  #
#                                  - Ramírez Guzmán Celeste                                              #
#                                  - Vega Camacho María José                                             #
#                                  - Aguilar Fonseca Hilary                                              #
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


import board #Librerías para accesar a I/O de la placa
from ideaboard import IdeaBoard # Librería de funciones varias del ideaboard
from time import sleep # Para utilizar función que detiene el código
from pwmio import PWMOut
from adafruit_motor import servo
import espnow

DERECHA = (255,255,0) #amarillo
IZQUIERDA = (255,0,255) #violeta
ABAJO = (0,255,255) #turquesa
ARRIBA = (0,0,255) #azul
VERDE = (0,255,0)
ROJO = (255,0,0)

APAGADO = (0,0,0)

e = espnow.ESPNow()

#Variables para modo lucha
velocidadLucha = 0.2
tiempoAvanzaLucha = 0.2
tiempoGiroLucha = 0.2

#Variables para servo motores de lucha
pwm = PWMOut(board.IO4, duty_cycle=0, frequency=50)
golpeMotor = servo.Servo(pwm, min_pulse=500, max_pulse=2500)
tiempoGolpe = 0.5
golpeMotor.angle = 0


#variable para cambiar polaridad de los motores
adMotor1 = 1;
adMotor2 = 1;

ib = IdeaBoard() # Instanciación I/O y funcione sdel Ideboard


def golpe():
    golpeMotor.angle = 45
    sleep(tiempoGolpe)
    golpeMotor.angle = 0

def wiggle(t,n,speed):
# Hace que el robot se mueva izquierda y derecha
# por tiempo t, a velocidad speed = [0,1]
#lo hace n veces
    for i in range(n):
        ib.pixel = (0,0,255)
        ib.motor_1.throttle = -speed * adMotor1
        ib.motor_2.throttle = speed * adMotor2
        sleep(t)
        ib.motor_1.throttle = speed * adMotor1
        ib.motor_2.throttle = -speed * adMotor2
        sleep(t)
        stop()
        sleep(t)
        ib.pixel = (0,0,255)
        ib.motor_1.throttle = speed * adMotor1
        ib.motor_2.throttle = -speed * adMotor2
        sleep(t)
        ib.motor_1.throttle = -speed * adMotor1
        ib.motor_2.throttle = speed * adMotor2
        sleep(t)
        
def forward(t,speed):
    # Mueve el robot hacia adelante
    # por tiempo t, a velocidad speed = [0,1]
    ib.pixel = (0,255,0)
    ib.motor_1.throttle = speed * adMotor1
    ib.motor_2.throttle = speed * adMotor2
    sleep(t)
    
def backward(t,speed):
    # Mueve el robot hacia atrás
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (150,255,0)
    ib.motor_1.throttle = -speed * adMotor1
    ib.motor_2.throttle = -speed * adMotor2
    sleep(t)
    
def left(t,speed):
    # Mueve el robot hacia la izquierda
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = -speed * adMotor1
    ib.motor_2.throttle = speed * adMotor2
    sleep(t)
    
def right(t,speed):
    # Mueve el robot hacia la derecha
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = speed * adMotor1
    ib.motor_2.throttle = -speed * adMotor2
    sleep(t)

def stop():
    # detiene los motores
    ib.pixel = (0,0,0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    
def randomTurn(t,speed):
    #Escoge izq o der al azar y rota
    # por tiempo t, a velocidad speed = [0,1]
    dir = random.choice([-1,1])
    ib.pixel = (255,0,0)
    ib.motor_1.throttle = dir*-speed
    ib.motor_2.throttle = dir*speed
    sleep(t)
    

def rondaLucha():
    if e: #evento recibido desde el control
        mensaje = e.read()
        print("Señal recibida...")
        print(mensaje)
        if ("arriba" in str(mensaje)):
            #color RGB
            ib.pixel = ARRIBA
            #activar motores
            forward(tiempoAvanzaLucha,velocidadLucha)    
            
                
        elif ("abajo" in str(mensaje)):
            #color RGB
            ib.pixel = ABAJO
            #activar motores
            backward(tiempoAvanzaLucha,velocidadLucha)
                
        elif ("izquierda" in str(mensaje)):
            #color RGB
            ib.pixel = IZQUIERDA
            #activar motores
            left(tiempoGiroLucha,velocidadLucha)
                
        elif ("derecha" in str(mensaje)):
            #color RGB
            ib.pixel = DERECHA
            #activar motores
            right(tiempoGiroLucha,velocidadLucha)        
            
        elif ("rojo" in str(mensaje)):
            #color RGB
            ib.pixel = ROJO
            #activar motores
            golpe()
                
        elif ("verde" in str(mensaje)):
            #color RGB
            ib.pixel = VERDE
            #activar motores
    #apagar led
    ib.pixel = APAGADO
    stop()
        
###### CODIGO PRINCIPAL   #######


while True:
    #DERECHA amarillo, IZQUIERDA violeta, ABAJO turquesa, ARRIBA azul, ROJO ataque
    rondaLucha()





