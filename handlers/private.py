from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an Telegram Groups Music bot 🎶, I let you play music in your group's voice chat.

The commands I currently support are:

 Im Group Music Player Bot 🎵

 Hello 👋 there! I can play music in voice chats of Telegeam Groups.
I have a lot of cool feature that will amaze you! Made By [Pawan Theekshana](t.me/Pawan_Theekshana)

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/MizuSupport_Official"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/MizuUpdates"
                    )
                ]
            ]
        )
    )
