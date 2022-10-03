from telethon import TelegramClient, events 
import requests
import os
import subprocess
from datetime import datetime
from gtts import gTTS
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
import modullar.client

client = modullar.client.client
@events.register(events.NewMessage(pattern=r".rename (.*)", outgoing=True))
async def rename(event):
    ok = await event.edit("NIKINGIZ UZGARTIRILDi...")
    names = event.pattern_match.group(1).strip() 
    first_name = names
    last_name = ""
    if "//" in names:
        first_name, last_name = names.split("//", 1)
    try:
        await event.client(
            UpdateProfileRequest(
                first_name=first_name,
                last_name=last_name,
            ),
        )
       
    except Exception as ex:
        await event.edit(ok, "\n`{}`".format(str(ex)))