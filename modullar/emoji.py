from telethon import TelegramClient, events 
from emoji import  emojize
import os
import modullar.client
from modullar import emojify
import time
import asyncio
client = modullar.client.client


@events.register(events.NewMessage(pattern=".emoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "Matn bn yozing..."
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.offman[emojify.oofman.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)
    