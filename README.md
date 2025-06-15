<h1 align="center">Luchas de Sumobots V2</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/natemodelo82/Luchas-Sumobots-V2?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/natemodelo82/Luchas-Sumobots-V2?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/natemodelo82/Luchas-Sumobots-V2?color=56BEB8">
  <img alt="License" src="https://img.shields.io/github/license/natemodelo82/Luchas-Sumobots-V2?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-about">Acerca del proyecto</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Características</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Tecnologías</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requerimientos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Inicio</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://ctpo.info" target="_blank">CTP Oreamuno</a>
</p>

<br>

## :dart: Acerca del proyecto ##

Este proyecto pretende diseñar una implementación para habilitar a los Sumobots para una competencia de Luchas de Robots

## :sparkles: Características ##

:heavy_check_mark: 1- Diseño de armas adaptables en los Sumobots:\
Para las armas adaptables a los Sumobots se han diseñado inicialmente 2, una para usar con una cuerda y un peso y otra para usar como un martillo.\
\
__Cadena:__\
![cadena](https://github.com/user-attachments/assets/a1d2aff8-8465-49fd-8526-d9fbf55dbb37)\
\
\
__Martillo:__\
![martillo](https://github.com/user-attachments/assets/45f0744f-5cc6-453e-9ee2-9dcb7221b9e8)\
\
El arma de lucha se debe instalar en la parte trasera del Sumobot y ajustarse con gazas plásticas.\
![sumolucha2](https://github.com/user-attachments/assets/20fec52a-b542-4dfe-ae99-c59d87a886b8)\
\
__Circuito para el control:__\
![controlIB_bb](https://github.com/user-attachments/assets/56f93af5-e2bf-400e-9bea-a90b8079807b)
\
\
__Circuito para el Sumobot:__\
![sumo_lucha](https://github.com/user-attachments/assets/af9e9147-66fa-4b64-8432-643cde02e0bd)
\
\

:heavy_check_mark: 2- Diseño de reglas de competencia:\

\
:heavy_check_mark: 3- Codificación de un Luchas-Sumobots-V2 para manejar los sumobots:\
En cuanto al código, este fue programado en CircuitPython, utilizando la herramienta Thonny.\
Se crearon dos módulos principales, uno para el control remoto y otro para el Sumobot.\
\
__Código Control remoto:__
```
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
sumo1 = mac_z


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
```    
__Código Sumobot de lucha:__
```
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
            forward(velocidadLucha,tiempoAvanzaLucha)    
            
                
        elif ("abajo" in str(mensaje)):
            #color RGB
            ib.pixel = ABAJO
            #activar motores
            backward(velocidadLucha,tiempoAvanzaLucha)
                
        elif ("izquierda" in str(mensaje)):
            #color RGB
            ib.pixel = IZQUIERDA
            #activar motores
            left(velocidadLucha,tiempoGiroLucha)
                
        elif ("derecha" in str(mensaje)):
            #color RGB
            ib.pixel = DERECHA
            #activar motores
            right(velocidadLucha,tiempoGiroLucha)        
            
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






``` 

## :rocket: Tecnologías ##

The following tools were used in this project:

- [Circuit Python](https://circuitpython.org/)
- [Esp Now](https://randomnerdtutorials.com/esp-now-esp32-arduino-ide/)
- [Ideaboard](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki)
- [Sumobots Universidad Cenfotec](https://github.com/Universidad-Cenfotec/Sumobot)
- [Diseño de Luchas de Robots](#)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Circuit Python](https://circuitpython.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/natemodelo82/Luchas-Sumobots-V2

# Access
$ cd Luchas-Sumobots-V2

# Install dependencies
$ yarn

# Run the project
$ yarn start

# The server will initialize in the <http://localhost:3000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.


Made with :heart: by <a href="https://ctpo.info" target="_blank">Informática CTP Oreamuno, Cartago.</a>

&#xa0;

<a href="#top">Back to top</a>
