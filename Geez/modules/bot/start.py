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
import random
from Geez import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = OWNER_ID
    message = "saya ingin bertanya kak"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

geezlogo = [
    "https://telegra.ph//file/0781e2b14dbd936b96295.jpg",
    "https://telegra.ph//file/0781e2b14dbd936b96295.jpg",
    "https://telegra.ph//file/0781e2b14dbd936b96295.jpg",
    "https://telegra.ph//file/0781e2b14dbd936b96295.jpg"
]

alive_logo = random.choice(geezlogo)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Yoo, saya Arab Premium Assistant, gada yang spesial dari saya\ntapi boong..."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/SiArab_Store"),
            InlineKeyboardButton("Repo", url="https://github.com/"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
