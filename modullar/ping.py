from telethon import TelegramClient, events
import modullar.client
import time 
from datetime import datetime 

client = modullar.client.client


@events.register(events.NewMessage(pattern='\.ping'))
async def pingHandler(event):
	   start = datetime.now()
	   msg = await event.edit("Pong!")
	   end = datetime.now()
	   ms = (end - start).microseconds / 1000
	   await msg.edit(f"**Pong!!**\n `{ms} ms`")