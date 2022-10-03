from telethon import TelegramClient, events
import modullar.client
import os
client = modullar.client.client
@events.register(events.NewMessage(outgoing=True, pattern='\.mq'))
async def mq(event):
	       chat = await event.get_chat()
	       replied_msg = await event.get_reply_message()
	       await event.edit("Kutilmoqda...")
	       x = await replied_msg.forward_to('@memocyteBot')
	       #print(x)
	       async with client.conversation('@memocyteBot') as conv:
	       	xx = await conv.get_response(x.id)
	       	await client.send_read_acknowledge(conv.chat_id)
	       	await client.send_message(chat, xx)
	       	await event.message.delete()
