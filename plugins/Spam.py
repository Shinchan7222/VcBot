from telethon import TelegramClient, events
from telethon.tl.functions.messages import ChatInviteRequest as Get
import asyncio

API_HASH = 
API_ID = 
token = 

client = TelegramClient("bspam", API_ID, API_HASH).start(BOT_TOKEN=token)

@client.on(events.NewMessage(incoming=True))
async def start(event):
  getid = "send chat id"
  if event.text == "/start" :
    await event.reply(getid)
    chatid = await event.text.get_response()
    await event.reply(chatid)
  
  
client.run_until_disconnected()
