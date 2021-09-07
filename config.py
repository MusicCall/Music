import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "David Music Bot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/81f10f739947b05d02c4c.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/81f10f739947b05d02c4c.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/81f10f739947b05d02c4c.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/81f10f739947b05d02c4c.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicRioBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "xRioMusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "L9L9L")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "L9L9L")
OWNER_NAME = getenv("OWNER_NAME", "xRioMusic") 
DEV_NAME = getenv("DEV_NAME", "xRioMusic")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
