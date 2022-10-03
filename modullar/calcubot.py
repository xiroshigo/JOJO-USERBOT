from telethon import TelegramClient, events
import modullar.client
import os
client = modullar.client.client
@events.register(events.NewMessage(outgoing=True, pattern='\.calc'))
async def calcubot(event):
	       chat = await event.get_chat()
	       replied_msg = await event.get_reply_message()
	       await event.edit("Kutilmoqda...")
	       x = await replied_msg.forward_to('@CalcuBot')
	       #print(x)
	       async with client.conversation('@CalcuBot') as conv:
	       	xx = await conv.get_response(x.id)
	       	await client.send_read_acknowledge(conv.chat_id)
	       	await client.send_message(chat, xx)
	       	await event.message.delete()@events.register