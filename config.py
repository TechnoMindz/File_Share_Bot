import re
import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝗛𝗲𝗹𝗹𝗼 {first}\n\n𝗜 𝗖𝗮𝗻 𝗦𝘁𝗼𝗿𝗲 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗙𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗔𝗻𝗱 𝗢𝘁𝗵𝗲𝗿 𝗨𝘀𝗲𝗿𝘀 𝗖𝗮𝗻 𝗔𝗰𝗲𝘀𝘀 𝗜𝘁 𝗙𝗿𝗼𝗺 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗟𝗶𝗻𝗸\nAny Queries Ask Here @TechnoMindzChat\n\n𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗕𝘆 @TMMAINCHANNEL")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝗛𝗲𝗹𝗹𝗼 {first}\n\n𝗬𝗼𝘂 𝗡𝗲𝗲𝗱 𝗧𝗼 𝗝𝗼𝗶𝗻 𝗠𝗮𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲\n\n𝗞𝗶𝗻𝗱𝗹𝘆 𝗣𝗹𝗲𝗮𝘀𝗲 𝗝𝗼𝗶𝗻 𝗠𝗮𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹")



### Custom Caption ###
default_custom_caption = """
𝗙𝗶𝗹𝗲 : <code>{file_name}</code>

🔥💫  𝙁𝙞𝙧𝙨𝙩 𝙊𝙣 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢  🔥💫
𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙈𝙤𝙫𝙞𝙚𝙨 𝙃𝙚𝙧𝙚 𝙖𝙣𝙙 𝙂𝙚𝙩 𝙄𝙣 1 𝙈𝙞𝙣𝙪𝙩𝙚 100℅👇
https://t.me/technomoviescollection

🤭 𝗔𝗟𝗟 𝗠𝗢𝗩𝗜𝗘𝗦 𝗛𝗘𝗥𝗘 🥱

<a href="https://t.me/tmmainchannel">1☞𝙅𝙤𝙞𝙣 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡</a>

<a href="https://t.me/technomoviescollection">2☞ 𝙅𝙤𝙞𝙣 𝙈𝙤𝙫𝙞𝙚𝙨 𝙂𝙧𝙤𝙪𝙥</a>

<a href="https://t.me/technomindzchat">3☞ 𝙅𝙤𝙞𝙣 𝘾𝙝𝙖𝙩𝙩𝙞𝙣𝙜 𝙂𝙧𝙤𝙪𝙥</a>

<a href="https://t.me/technoseriescollection">4☞ 𝙅𝙤𝙞𝙣 Series Channel</a>

<a href="https://t.me/tmseriescollection">5☞ <b><i>Join Series Group</i></b></a>
"""
CUSTOM_CAPTION = os.environ.get('CUSTOM_CAPTION', default_custom_caption)




#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(2023126723)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
