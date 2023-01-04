# import os
# import sys
# from time import sleep
# import time
# import requests
# import asyncio
# import random
# import string
# import webbrowser
# from threading import Thread
# from colorama import Fore

# from utilidades.config.actu import busca_actu
from utilidades.config.librerias import *
from utilidades.config.comun1 import *


os.system('cls')
w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX


print(f"""
{Fore.LIGHTBLUE_EX}.%%..%%...%%%%...%%..%%...%%%%....%%%%...%%..%%..%%..%%.
{Fore.GREEN}.%%%.%%..%%..%%..%%..%%..%%..%%..%%......%%..%%..%%%.%%.
{Fore.LIGHTBLUE_EX}.%%.%%%..%%..%%..%%..%%..%%%%%%...%%%%...%%..%%..%%.%%%.
{Fore.GREEN}.%%..%%..%%..%%...%%%%...%%..%%......%%..%%..%%..%%..%%.
{Fore.LIGHTBLUE_EX}.%%..%%...%%%%.....%%....%%..%%...%%%%....%%%%...%%..%%.
{Fore.RED}........................................................
""")
setTitle(f"Proxies    |    ")
choice = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Quieres usar proxies? [Y/N]: {Fore.RESET}")
if choice.lower() == 'y' or choice.lower() == 'yes':
        if os.path.basename(sys.argv[0]).endswith("exe"):
            with open(getTempDir()+"\\nova_proxies", 'w'): pass
            clear()
            proxy_scrape()
            sleep(0.3)
        try:
            assert sys.version_info >= (3,9)
        except AssertionError:
            print(f"{Fore.RED}Tu version de python no es soportada: ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), Por favor descarga v3.9+ to use NovaSun!{Fore.RESET}")
            sleep(5)
            print("[\x1b[95m1\x1b[95m\x1B[37m] Saliendo!")
            sleep(1.5)
            os._exit(0)
        else:
            with open(getTempDir()+"\\nova_proxies", 'w'): pass
            clear()
            proxy_scrape()
            sleep(0.3)
        finally:
            Fore.RESET
if choice.lower() == 'n' or choice.lower() == 'no':
    pass
def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)
global cls
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def main():
    global threads
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
                        {Fore.LIGHTBLUE_EX}.%%..%%...%%%%...%%..%%...%%%%....%%%%...%%..%%..%%..%%.
                        {Fore.GREEN}.%%%.%%..%%..%%..%%..%%..%%..%%..%%......%%..%%..%%%.%%.
                        {Fore.LIGHTBLUE_EX}.%%.%%%..%%..%%..%%..%%..%%%%%%...%%%%...%%..%%..%%.%%%.
                        {Fore.GREEN}.%%..%%..%%..%%...%%%%...%%..%%......%%..%%..%%..%%..%%.
                        {Fore.LIGHTBLUE_EX}.%%..%%...%%%%.....%%....%%..%%...%%%%....%%%%...%%..%%.
                        {Fore.RED}........................................................
.......................................................................................................................     
        [>] Versión: {ESTA_VERSION}
        [>] Discord: Soon
        [>] Web: Soon
        [>] Github: Soon
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Roblox gen
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Joiner
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Leaver
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Checker
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Webhook Spammer
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Info server
{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Generador de nitro
{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Scrapper de IDS
{m}[{w}9{Fore.RESET}{m}]{Fore.RESET} MassDM
{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} Token Gen
{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} Acerca de
{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} NOTAS
    
    ''')
    choice = input(f'{m}[-]{w} Elección?: ')

    if choice == '1':
        Spinner()
        gh = input("""
        Roblox gen es de la versión de pago (No disponible aún)

        [1] Visitar web
        [2] Salir al menú principal
        
        
        """)

        if gh == ['01', '1']:
            webbrowser.open('https://google.com')
        elif gh in ['02','2']:
            exit = main()
        else:
            print('')
    
    if choice == '2':
        Spinner()
        sv = input('No disponible')
        exit = main()
    
    if choice == '3':
        Spinner()
        setTitle(f'Server Leaver    |')
        token = open('tokens.txt', 'r').read().splitlines()
        ID = input(f'\nID DEL SERVIDOR: ')
        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                requests.delete(apilink, headers=headers)
            print(f'{y} [!] {w}Listo')
        time.sleep(1)
        exit = input('PRESIONA ENTER: ')
        exit = clear()
        exit = main()
    if choice == '4':
        Spinner()
        setTitle(f'Token Checker    |')
        print(f'\n{y}CARGANDO TOKENS:\n')
        time.sleep(0.5)
        def success(text): lock.acquire(); print(f'[{g}>{Fore.RESET}] {g}VÁLIDA {Fore.RESET}{text}'); lock.release();
        def invalid(text): lock.acquire(); print(f'[{lr}X{Fore.RESET}] {lr} NO VÁLIDA {Fore.RESET}{text}'); lock.release();
        with open('tokens.txt', 'r') as f: tokens = f.read().splitlines()
        def guardar_tokens():
            with open('tokens.txt', 'w') as f: f.write("")
            for token in tokens:
                with open('tokens.txt', 'a') as f: f.write(token + '\n')
        def quitar_duplicados(file):
            lines_seen = set()
            with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
        def chequeo_token(token:str):
            respuesta = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
            if respuesta.status_code == 200: success(f'| {token}')
            else: tokens.remove(token); invalid(f"| {token}")
        def chequeo_tokens():
            threads = []
            for token in tokens:
                try: threads.append(threading.Thread(target=chequeo_token, args=(token,)))
                except Exception as e: pass
            for thread in threads: thread.start()
            for thread in threads: thread.join()
        def start():
            quitar_duplicados('tokens.txt')
            chequeo_tokens()
            guardar_tokens()
        
        start()
        print('Todas las tokens han sido checkeadas (tokens.txt actualizado)')
        time.sleep(1)
        exit = input('Presiona ENTER: ')
        exit = clear()
        exit = main()
    if choice == '5':
        Spinner()
        setTitle(f'WEBHOOK SPAMMER  |')
        session = requests.Session()
        webhook = input(f'[-] Webhook URL: ')
        message = input(f'[-] Mensaje: ')
        username = input(f'[-] Usuario del Webhook: ')

        def nova():
            session.post(webhook,json = {'content':message,'username':username})

            while True:
                for i in range(15):
                    threading.Thread(target=nova).start()
        nova()
    if choice == '6':
        Spinner()
        setTitle('Información del servidor  |')
        print('No disponible')
        exit = clear()
        exit = main()
    if choice == '7':
        Spinner()
        setTitle(f"Nitro Generator    |    ")
        
        webhooklink = str(input(f"\n[-] Webhook URL: "))
        
        count = 0

        webhook = "~~WEBHOOK_URL~~""".replace("~~WEBHOOK_URL~~", webhooklink)

        while True:
            try:
                code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
                post = {"content":"https://discord.com/billing/promotions/"+code}
                head = {

                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                        'content-type' : 'application/json'
                    }
                count += 1
                print(f'[{g}>{Fore.RESET}] Nitro generado | [{count}]')
                s = requests.post(webhook, json=post, headers=head)
            except:
                print(f"[!{Fore.RESET}] ERROR!")
                break
    if choice == '8':
        Spinner()
        setTitle('Scrapper  |')
        tukan = input('[-] Token: ')
        guildd = input('[-] Server ID: ')
        chann = input('[-] Channel ID: ')
        bot = discum.Client(token=tukan)

        def closefetching(resp,guildid):
             if bot.gateway.finishedMemberFetching(guildid):
                lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                print(str(lenmembersfetched))
                bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                bot.gateway.close()

        def getmembers(guildid,channelid):
                 bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                 bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                 bot.gateway.run()
                 bot.gateway.resetSession()
                 return bot.gateway.session.guild(guildid).members

        members = getmembers(guildd, chann)
        memberids = []

        for memberId in members:
            memberids.append(memberId)

        cls()

        with open('datos/massdm_ids.txt','w') as ids:
            for element in memberids:
                    ids.write(element + '\n')    
        
        print(f'{lr}[!] Finalizado el scraping, he scrapeado {len(memberids)} miembros (Recordatorio se han guardado en el archivo massdm_ids, carpeta datos)')
        time.sleep(1)
        exit = input('\nPresiona ENTER: ')
        exit = clear()
        exit = main()
    if choice == '9':
        Spinner()
        setTitle(f'Server MASSDM    |')
        # print('[!] MassDM no esta disponible en este momento')
        # time.sleep(2.5)
        # exit = input(f'[!] Presiona ENTER')
        # exit = clear()
        # exit = main()
        mensaje = input('[-] Mensaje a enviar: ')
        with open('datos/massdm_ids', 'r+') as f:
            for element in memberids:
                f.send(mensaje)
    if choice == '10':
        Spinner()
        cantidad = int(input('[-] Cuantas tokens genero?: '))
        char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_"
        for i in range(cantidad):
            primera = "".join((random.choice(char) for i in range(38)))
            segunda = "".join((random.choice(char) for i in range(6)))
            tercera = "".join((random.choice(char) for i in range(38)))

            resultado = primera + "." + segunda + "." + tercera
            output = open('tokens.txt', 'a')
            output.write(resultado + "\n")

            print(f"" + resultado)
        print(f'He generado {cantidad}')
        exit = input('[-] Presiona ENTER: ')
        exit = clear()
        exit = main()

    if choice == '11':
        Spinner()
        SlowPrint('\nHola gracias por usar NovaSun Tool\nSi necesitas ayuda contacte con NovaSun#8175!')
        time.sleep(1)
        exit = input('\n[-] Presiona ENTER: ')
        exit = clear()
        exit = main()
    if choice == '12':
        Spinner()
        setTitle(f'Notas    |')
        SlowPrint('\nNOTAS ACTUALIZADAS:\n')
        print(f'[-] Scraper (DESACTUALIZADO)\n[-] MassDM (DESACTUALIZADO)')
        time.sleep(1)
        exit = input('[-] Presiona ENTER: ')
        exit = clear()
        exit = main()








    


if __name__ == '__main__':
    import sys
    os.system("""Si no existe './chromedriver.exe' echo [+] Descargando drivers""")
    os.system("""if not exist './chromedriver.exe' curl -#fkLo "chromedriver.exe" "https://github.com/NovaSunDev/chromedriver.git" """)
    if os.path.basename(sys.argv[0]).endswith('exe'):
        busca_actu()
        if not os.path.exists(getTempDir()+"\\nova_proxies"):
                        proxy_scrape()
        clear()
    else:
        if not os.path.exists(getTempDir()+"\\nova_proxies"):
                        proxy_scrape()
        busca_actu()
        clear()
        main()






