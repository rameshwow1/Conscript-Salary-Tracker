import os
os.system('python3.12 -m venv ./venv')
os.system('source venv/bin/activate')
os.system('pip3 install flask, flask_login, flask_sqlalchemy, pymongo')
os.system('pip3 uninstall werkzeug')
os.system('pip3 install werkzeug==2.3.0')
