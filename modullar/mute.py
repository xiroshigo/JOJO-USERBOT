from telethon import TelegramClient, events, sync
import asyncio
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User
import datetime
import modullar.client
client = modullar.client.client

@events.register(events.NewMessage(pattern=r'.mute', outgoing=True))
async def mute(event: events.NewMessage.Event):
    chat = await event.get_chat()
    reply_to_message = await event.get_reply_message()

    if not reply_to_message:
        await event.delete()
        return

    time_flags_dict = {
        "m": [60, "минут"],
        "h": [3600, "часов"],
        "d": [86400, "дней"]
        }

    try:
        #m or h or d
        time_type = event.message.text[-1]

        #get number
        count = int(event.message.text.split()[1][:-1])

        #convert to seconds
        count_seconds = count * time_flags_dict[time_type][0]

        rights = ChatBannedRights(
            until_date=datetime.datetime.utcnow() + datetime.timedelta(seconds=count_seconds),
            send_messages=True
        )

        await client(EditBannedRequest(chat.id, reply_to_message.sender_id, rights))
        await event.edit(f'Заглушен на {count} {time_flags_dict[time_type][1]}')

    except Exception as e:
        print(e)