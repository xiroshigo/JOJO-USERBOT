from telethon import TelegramClient, events
import modullar.client
from modullar.magic import Magic
import time
magic = Magic()
client = modullar.client.client
@events.register(events.NewMessage)
async def magichandler(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)