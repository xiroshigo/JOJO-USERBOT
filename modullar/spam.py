from telethon import TelegramClient, events
import modullar.client
import os
import time
import asyncio
client = modullar.client.client

@events.register(events.NewMessage(pattern=".spam ?(.*)"))
async def delayspam(e):
    try:
        args = e.text.split(" ", 3)
        dark = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit(f"**ishlatish :** {HNDLR}spam <dark time> <count> <msg>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(dark)
    except Exception as u:
        await e.respond(f"**Hatolik :** `{u}`")