from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


REPO = "**jaa na lode**"
HOME_TEXT = "💖 **Hi [{}](tg://user?id={})**,\n\njaa na lode**"
HELP = """**Join @The_HellBot and @Its_Fuckin_Hell to get more dick!!

🏷️ **Users Commands**:
\u2022 PCM files.
\u2022 `/pause`  -  Pause playing music.
\u2022 `/resume`  -  Resume playing music.
\u2022 `/mute`  -  Mute the VC Bot.
\u2022 `/unmute`  -  Unmute the VC Bot.




@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('📺 CHANNEL', url='https://t.me/The_HellBot'),
        InlineKeyboardButton('🏘️ Group', url='https://t.me/Its_Fuckin_Hell'),
    ],
    [
        InlineKeyboardButton('📑 GitHub', url='https://github.com/The-HellBot'),

    ],
    [
        InlineKeyboardButton('⚙️ HELP ⚙️', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


@Client.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(REPO, disable_web_page_preview=True)


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
