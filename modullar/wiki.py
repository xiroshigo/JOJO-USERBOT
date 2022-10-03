
from telethon import TelegramClient, events 
from emoji import  emojize
import os
import modullar.client
import wikipedia
import time
import asyncio
client = modullar.client.client

@events.register(events.NewMessage(pattern=".wiki ?(.*)"))
async def wiki(e):
    srch = e.pattern_match.group(1)
    if not srch:
        return await e.edit("`wikipedia qidirish uchun text kiriting !`")
    msg = await e.edit(f"`qidirilmoqda {srch} wikipedia..`")
    try:
        mk = wikipedia.summary(srch)
        te = f"**Qidiruv sorovi :** {srch}\n\n**Natija :** {mk}"
        await msg.edit(te)
    except Exception as err:
        await msg.edit(f"**ERROR** : {str(err)}")