@echo off
Title DESCARGANDO MÓDULOS
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python3 -m pip install -r requirements.txt
cls
Title DESCARGANDO MÓDULOS
echo python main.py >> start.bat
start start.bat