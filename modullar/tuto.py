from telethon import TelegramClient, events
import modullar.client
#from handlers.lovestory import Lovestory
import time
#
client = modullar.client.client
@events.register(events.NewMessage(pattern='\.chatscan'))
async def chatscan(event):
		async for dailog in client.iter_dialogs():
			await event.reply(dailog.name + "chats id:" + str(dailog.id))
			await event.delete()