import importlib
import time
from pyrogram import idle
from uvloop import install
from geezlibs import logging, BOT_VER, __version__ as gver
from Geez import LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR, BOTLOG_CHATID
from Geez.modules import ALL_MODULES
from Geez.modules.basic.heroku import geez_log


MSG_ON = """
**Arab Premium Userbot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**Arab Library Version - `{}`**
**Ketik** `{}Arab` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
©️2023 Arab|Premium Userbot
"""

async def main():
    await app.start()
    LOGGER("Arab").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Geez.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await logging(bot)
            await geez_log()
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
            except BaseException as a:
                LOGGER("Arab").warning(f"{a}")
            LOGGER("Arab").info("Startup Completed")
            LOGGER("Arab").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Arab").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Arab").info("Starting Arab Premium Userbot")
    install()
    LOOP.run_until_complete(main())
