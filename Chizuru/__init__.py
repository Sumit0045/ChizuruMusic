import asyncio
import logging
from pytgcalls import PyTgCalls
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING


loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



Chizuru = Client(
    ":Chizuru:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

userbot = Client(
    ":userbot:",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

pytgcalls = PyTgCalls(userbot)



async def chizuru_music():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await Chizuru.start()
    await userbot.start()
    await pytgcalls.start()
    getme = await Chizuru.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(chizuru_music())


