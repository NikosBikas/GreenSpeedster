# INSTALL

* This is for __new installation only__

## Windows Install

1. Make sure you have python3 and gitbash installed!
2. The Python installers for Windows include pip. You can make sure that pip is up-to-date by running:
   py -m pip install --upgrade pip
3. Install virtualenv by running:
   py -m pip install --user virtualenv
4. Create a virtual environment inside the projects root folder by running:
   py -m venv env
5. Use gitbash to activate the virtual environment ~/env/Scripts/activate:
   source env/Scripts/activate)
6. Install all the required packages for the project:
   pip install -r requirements.txt
7. Run the project using python: 
   python manage.py runserver

## Linux/MacOS Install

1. Make sure you have python3 pip3 and gitbash installed!
2. Debian and most other distributions include a python-pip package; if you want to use the Linux distribution-provided versions of pip, see Installing        pip/setuptools/wheel with Linux Package Managers.   
   You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
   python3 -m pip install --user --upgrade pip
3. Install virtualenv by running:
   python3 -m pip install --user virtualenv
4. Create a virtual environment inside the projects root folder by running:
   python3 -m venv env
5. Use bash to activate the virtual environment ~/env/bin/activate:
   source env/Scripts/activate)
6. Install all the required packages for the project:
   pip3 install -r requirements.txt
7. Run the project using python: 
   python manage.py runserver
