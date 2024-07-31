import re
from os import getenv
from os import environ
import logging

# Set up logging configuration
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt'),
        logging.StreamHandler()
    ],
    level=logging.INFO
)

# Regex pattern for IDs
id_pattern = re.compile(r'^\d+$')

def is_enabled(value, default):
    """Check if the provided value enables a feature based on common true/false indicators."""
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg').split()
PRIME_LOGO = environ.get('PRIME_LOGO', 'https://i.ibb.co/VSLt4Xs/Whats-App-Image-2024-07-30-at-14-16-01-5055b0b2.jpg')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://dabbukarki:eiXlC27PtzEO4lRc@kobramovies.hrrze8l.mongodb.net/?retryWrites=true&w=majority&appName=kobramovies")
DATABASE_NAME = environ.get('DATABASE_NAME', "kobramovies")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# LOG CHANNELS
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
LAZY_GROUP_LOGS = int(environ.get('LAZY_GROUP_LOGS', 0))
REQ_CHANNEL = int(environ.get('REQ_CHANNEL'))
PRIME_MEMBERS_LOGS = int(environ.get('PRIME_MEMBERS_LOGS'))

# PREMIUM ACCESS
lazydownloaders = [int(lazydownloaders) if id_pattern.search(lazydownloaders) else lazydownloaders for lazydownloaders in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_USERS = lazydownloaders if lazydownloaders else []  # Users who can download files without URL shortener
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = lazy_renamers + ADMINS if lazy_renamers else []  # Add user IDs for file renaming features
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', '5965340120').split()]

# New Configuration
MAX_B_TN = int(environ.get('MAX_B_TN', 100))
MAX_BTN = int(environ.get('MAX_BTN', 10))

QR_CODE_IMG = environ.get('QR_CODE_IMG', 'https://telegra.ph/file/342a2e9bd3ef5100c4c0e.jpg')  # URL link of QR code for receiving money
UPI_ID = environ.get('UPI_ID', '8607706913@kotak')  # Your UPI ID

# Others
TUTORIAL = environ.get('TUTORIAL', '#')  # Tutorial video link for opening shortlink website
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'LazyDeveloper')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "False"), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Kobra Movies™](https://t.me/kobraoldmovies)</b>⚡\n\n📂<b>File Name:</b> ⪧ {file_caption} \n <b>Size: </b>{file_size}\n\n❤")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌🎁Support: @kobramovies 🎁\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ We are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️ Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "True"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "False"), False)

# LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE"))  # Enable file renaming feature

# Requested Content template variables
ADMIN_USRNM = environ.get('ADMIN_USRNM', 'kobraseries')  # WITHOUT @
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM', 'kobraseries')  # WITHOUT @
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM', 'kobraseries')  # WITHOUT @
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE', 'kobraseries')  # WITHOUT @ (Add only handle, not full URL)
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "kobrachatgroup")  # WITHOUT @

# URL Shortner
URL_MODE = is_enabled(environ.get("URL_MODE", "True"), False)  # Enable URL shortener in groups or PM
URL_SHORTENER_WEBSITE = environ.get('URL_SHORTENER_WEBSITE', 'atglinks.com')  # Use website URL from API section
URL_SHORTENER_WEBSITE_API = environ.get('URL_SHORTENER_WEBSITE_API', '83463cceb867a14dca0832e2fdeacfba75079dd8002b8956c6da67f21289ddcdf006726cd6e4e6af393ad7bf790f09d1')
lazy_groups = environ.get('LAZY_GROUPS', '')
LAZY_GROUPS = [int(lazy_groups) for lazy_groups in lazy_groups.split()] if lazy_groups else None  # Add group IDs
my_users = [int(my_users) for my_users in environ.get('MY_USERS', '').split() if my_users.isdigit()]  # Add user IDs to perform operations

# Don't touch below
PLUGINS_DIR = environ.get("PLUGINS_DIR", "plugins")


