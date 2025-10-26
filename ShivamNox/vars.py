# (c) ShivamNox
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '28405636'))
    API_HASH = str(getenv('API_HASH', '52b6dfbaeea988407006cefbea7c2e04'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '7902407945:AAFCJidyZ1ELUnQuR41iv6QJkslc8j9SzRI'))
    name = str(getenv('name', 'FileStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002044705664'))
    PORT = int(getenv('PORT', '3000'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6713397633").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'shivamnox'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '0.0.0.0:3000')) if not ON_HEROKU or getenv('FQDN', '0.0.0.0:3000') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://846hz7-3000.csb.app/".format(FQDN)
    else:
        URL = "https://846hz7-3000.csb.app/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://daxonultra:QPRXnQLz9sCr1K8l@cluster0.3mqoc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'hivajoyweb'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
