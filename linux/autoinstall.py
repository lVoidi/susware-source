from colorama import Style
from os import system as command
from distro import id as distro

print(Style.BRIGHT)

if distro() == 'arch':
     print("Se empezará a instalar las dependencias del proyecto")
     command('yes | LC_ALL=en_US.UTF-8 sudo pacman -S tk flameshot feh')
     command('curl https://i.ytimg.com/vi/7cw0ZCi-QPo/maxresdefault.jpg -o src/wallpaper.jpg')
     command('curl https://cdn.discordapp.com/attachments/846521077081178162/853127367602077696/y2mate.com_-_Among_Us_Drip_Theme_Song_Original_Among_Us_Trap_Remix_Amogus_Meme_Music.mp3 -o src/amogus.mp3')
     
else:
     print("Se empezará a instalar las dependencias del proyecto")
     command('sudo apt update')
     command('sudo apt install python3-pip flameshot python3-tk ffmpeg libavcodec-extra -y')
     command('curl https://i.ytimg.com/vi/7cw0ZCi-QPo/maxresdefault.jpg -o src/wallpaper.jpg')
     command('curl https://cdn.discordapp.com/attachments/846521077081178162/853127367602077696/y2mate.com_-_Among_Us_Drip_Theme_Song_Original_Among_Us_Trap_Remix_Amogus_Meme_Music.mp3 -o src/amogus.mp3')

command('python -m pip install -r requirements.txt')
