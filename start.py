#(Β©)Judson-web
#(Β©)Judson-web

import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages
from database.support import users_info
from database.sql import add_user, query_msg


#=====================================================================================##



WAIT_MSG = """"<b>πΏπππππππππ...ππ»ββ</b>"""

REPLY_ERROR = """<code>πππ ππππ π²ππππππ π°π π ππππππ’ ππ π°ππ’ ππππππππ πΌππππππ πππππΎππ π°ππ’ ππππππ.</code>"""


#=====================================================================================##


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    await add_user(id, user_name)
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("πΏπππππ π πππ...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Sα΄α΄α΄α΄ΚΙͺΙ΄Ι’ α΄‘α΄Ι΄α΄ α΄‘Κα΄Ι΄Ι’..π")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π AΚα΄α΄α΄ Mα΄", callback_data = "about"),
                    InlineKeyboardButton("CΚα΄sα΄ π", callback_data = "close")
                ],
                [
                    InlineKeyboardButton("β»οΈ α΄α΄ΙͺΙ΄ α΄α΄Κα΄Ι’Κα΄α΄ Ι’Κα΄α΄α΄ β»οΈ", url="https://t.me/storytym")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Jα΄ΙͺΙ΄ CΚα΄Ι΄Ι΄α΄Κ",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'π° TΚΚ AΙ’α΄ΙͺΙ΄ π°',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.private & filters.command('users'))
async def subscribers_count(bot, m: Message):
    id = m.from_user.id
    if id not in ADMINS:
        return
    msg = await m.reply_text(WAIT_MSG)
    messages = await users_info(bot)
    active = messages[0]
    blocked = messages[1]
    await m.delete()
    await msg.edit(USERS_LIST.format(active, blocked))


@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>BΚα΄α΄α΄α΄α΄sα΄ΙͺΙ΄Ι’ Mα΄ssα΄Ι’α΄.. TΚΙͺs α΄‘ΙͺΚΚ Tα΄α΄α΄ Sα΄α΄α΄ TΙͺα΄α΄ π₯±</i>")
        for row in query:
            chat_id = int(row[0])
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>BΚα΄α΄α΄α΄α΄sα΄ Cα΄α΄α΄Κα΄α΄α΄α΄ βοΈ</u>

Tα΄α΄α΄Κ Usα΄Κs ππΏββοΈ: <code>{total}</code>
Sα΄α΄α΄α΄ss?α΄Κ β: <code>{successful}</code>
BΚα΄α΄α΄α΄α΄ Usα΄Κs β: <code>{blocked}</code>
Dα΄Κα΄α΄α΄α΄ Aα΄α΄α΄α΄Ι΄α΄s β οΈ: <code>{deleted}</code>
UΙ΄sα΄α΄α΄α΄ss?α΄Κ π₯Ί: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
