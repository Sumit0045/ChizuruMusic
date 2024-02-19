from Chizuru import Chizuru
import time, os
from pyrogram import filters, __version__
from pytgcalls import __version__ as version



ping_txt = """
**PING PONG 🎉**

⌬ **Time taken** - `{}`ms
⌬ **Pyrogram** - `{}`
⌬ **Pytgcalls** - `{}`
"""

@Chizuru.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    start_time = time.time()
    a = await message.reply("Pinging...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)    
    await a.edit_text(ping_txt.format(ping_time,__version__, version))

@Chizuru.on_message(filters.command(["cleanup"]))
async def cleanup(_, message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **ᴄʟᴇᴀɴᴇᴅ**")
    else:
        await message.reply_text("✅ **ᴀʟʀᴇᴀᴅʏ ᴄʟᴇᴀɴᴇᴅ**")

