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
START_MSG = os.environ.get("START_MESSAGE", """𝙷𝙴𝙻𝙻𝙾 👋 {first},
 𝗜 𝗖𝗮𝗻 𝗦𝘁𝗼𝗿𝗲 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗙𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗔𝗻𝗱 𝗢𝘁𝗵𝗲𝗿 𝗨𝘀𝗲𝗿𝘀 𝗖𝗮𝗻 𝗔𝗰𝗲𝘀𝘀 𝗜𝘁 𝗙𝗿𝗼𝗺 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗟𝗶𝗻𝗸\n\n𝐌𝐘 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 👇👇👇\n<a href=https://t.me/Technomindzyt><b>༒☬𝓡𝓐𝓥𝓘𝓝𝓐𝓝𝓓𝓐𝓝☬༒</b></a> \n\nℕ𝕖𝕖𝕕 𝕋𝕠 𝔻𝕖𝕡𝕝𝕠𝕪 𝕐𝕠𝕦𝕣 𝕆𝕨𝕟 ?\nℂ𝕠𝕟𝕥𝕒𝕔𝕥 ℍ𝕖𝕣𝕖 @TechnoMindzChat\n\n𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗕𝘆 @TmMainChannel""")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {first}\n\nYᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ")

#set your Custom Caption here, Keep None for Disable Custom Caption
default_custom_caption = """
📁 ➜ <code>{file_name}</code>

⚡️𝗔𝗟𝗟 𝗠𝗢𝗩𝗜𝗘𝗦 𝗛𝗘𝗥𝗘⚡️

❤️‍🔥 𝙁𝙞𝙧𝙨𝙩 𝙊𝙣 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 ❤️‍🔥

𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙈𝙤𝙫𝙞𝙚𝙨 𝙃𝙚𝙧𝙚 𝙖𝙣𝙙 𝙂𝙚𝙩 𝙄𝙣 1 𝙈𝙞𝙣𝙪𝙩𝙚 100℅👇
@TechnoMoviesCollection

𝕊𝕌𝔹𝕊ℂℝ𝕀𝔹𝔼 𝕆𝕌ℝ 𝕐𝕆𝕌𝕋𝕌𝔹𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 🥰 👇
https://www.youtube.com/c/TechnoMindz

🔗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞 ☞
@TmMainchannel

╔══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╗
<a href="https://t.me/tmmainchannel">1☞𝙅𝙤𝙞𝙣 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡</a>

<a href="https://t.me/technomoviescollection">2☞ 𝙅𝙤𝙞𝙣 𝙈𝙤𝙫𝙞𝙚𝙨 𝙂𝙧𝙤𝙪𝙥</a>

<a href="https://t.me/technomindzchat">3☞ 𝙅𝙤𝙞𝙣 𝘾𝙝𝙖𝙩𝙩𝙞𝙣𝙜 𝙂𝙧𝙤𝙪𝙥</a>
╚══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╝

♥️ 𝗧𝗲𝗮𝗺 ➜ @TmMainChannel

✯ ━━━━━ ✧ ━━━━━ ✯
"""
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", default_custom_caption)

#set True if you want to prevent users from forwarding files from bot
if os.environ.get("PROTECT_CONTENT", None) == 'True':
    PROTECT_CONTENT = True
else:
    PROTECT_CONTENT = False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5038784553)

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
