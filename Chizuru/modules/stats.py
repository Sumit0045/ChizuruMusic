from pyrogram import filters
from config import SUDO_USERS
from Chizuru import Chizuru
from Chizuru.core.mongo import *




# ------------------------------------------------------------------------------- #


@Chizuru.on_message(group=10)
async def chat_watcher_func(_, message):
    try:
        if message.from_user:
            us_in_db = await get_user(message.from_user.id)
            if not us_in_db:
                await add_user(message.from_user.id)

        chat_id = (message.chat.id if message.chat.id != message.from_user.id else None)

        if not chat_id:
            return

        in_db = await get_chat(chat_id)
        if not in_db:
            await add_chat(chat_id)
    except:
        pass
        


# --------------------------------------------------------------------------------- #


@Chizuru.on_message(filters.command("stats") & filters.user(SUDO_USERS))
async def stats(_, message):
    users = len(await get_users())
    chats = len(await get_chats())
    await message.reply_text(
        f"""**ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ** {(await _.get_me()).mention} :

➻ ᴄʜᴀᴛs : {chats}
➻ ᴜsᴇʀs : {users}
"""
    )
    
