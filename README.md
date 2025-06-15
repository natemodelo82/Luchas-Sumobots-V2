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
Cadena:\
![cadena](https://github.com/user-attachments/assets/a1d2aff8-8465-49fd-8526-d9fbf55dbb37)\
\
\
Martillo:\
![martillo](https://github.com/user-attachments/assets/45f0744f-5cc6-453e-9ee2-9dcb7221b9e8)\
\
El arma de lucha se debe instalar en la parte trasera del Sumobot y ajustarse con gazas plásticas.\
![sumolucha2](https://github.com/user-attachments/assets/20fec52a-b542-4dfe-ae99-c59d87a886b8)\
\
:heavy_check_mark: 2- Diseño de reglas de competencia:\

\
:heavy_check_mark: 3- Codificación de un Luchas-Sumobots-V2 para manejar los sumobots:\
En cuanto al código, este fue programado en CircuitPython, utilizando la herramienta Thonny.\
Se crearon dos módulos principales, uno para el control remoto y otro para el Sumobot.\
\
##Código Control remoto:
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
