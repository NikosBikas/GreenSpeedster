@echo off
pushd %~dp0

:: Install Requirements
:install_requirements
shift
cd  env\Scripts\ && start /wait cmd /k "activate.bat && pip install -r requirements.txt && exit" 

::run_server
:run_server
start cmd /k "activate.bat && cd ../../ && python manage.py runserver" && echo Time out 10 seconds to open browser! && timeout 10 && start http://127.0.0.1:8000/

