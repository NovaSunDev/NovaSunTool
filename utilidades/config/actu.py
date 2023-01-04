import os
import re
import sys
import shutil
import requests
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup

from comun1 import *
from librerias import *
from actu import actu

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

def busca_actu():
    clear()
    setTitle('Nueva actualización encontrada')
    r = requests.get("") # github
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if ESTA_VERSION not in result_string:
        print('''
         █████╗  ██████╗████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗  ██████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
███████║██║        ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██║     ██║██║   ██║██╔██╗ ██║
██╔══██║██║        ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██║     ██║██║   ██║██║╚██╗██║
██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║╚██████╗██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                   
        
        
        ''')
        soup = BeautifulSoup(requests.get("").text, 'html.parser') # github
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        print('Te gustaría actualizar a la versión más reciente?')
        choice = input(f"{c} yes or no")
        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f'\n [{g}{w}] actualizando')
            if os.path.basename(sys.argv[0]).endswith('exe'):
                with open('novasuntool.zip', 'wb') as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile('novasuntool.zip', 'r') as filezip:
                    filezip.extractall()
                os.remove('novasuntool.zip')
                cwd = os.getcwd()+'\\novasuntool\\'
                shutil.copyfile(cwd+'changelog.md', 'changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'novasun.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'readme.md', 'readme.md')
                shutil.rmtree('novasuntool')
                input(f'{g}[!] {w}Actualizado correctamente')
                os.startfile('novasun.exe')
                os._exit(0)
            else:
                new_version_source = requests.get("")
                with open('novasuntool.zip', 'wb') as zipfile:
                    zipfile.write(new_version_source)
                with ZipFile('novasuntool.zip', 'r') as filezip:
                    filezip.extractall()
                os.remove('novasuntool.zip')
                cwd = os.getcwd()+'\\novasuntool\\'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                input(f' Actualización completada ')
                input(f' Presiona ENTER para ver la nueva actu ')
                if os.path.exists(os.getcwd()+'install.bat'):
                    os.startfile('install.bat')
                elif os.path.exists(os.getcwd() + 'start.bat'):
                    os.startfile('start.bat')
                os._exit(0)