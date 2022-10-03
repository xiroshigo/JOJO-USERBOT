from telethon import TelegramClient, events
import modullar.client
client = modullar.client.client
@events.register(events.NewMessage(outgoing=True, pattern=r'\.banall'))
async def banall(event):
    await event.delete()
    messagelocation = event.to_id
    async for user in event.client.iter_participants(messagelocation):
        user_id = user.id
        try:
            await event.client.edit_permissions(messagelocation, user_id, view_messages=False)
        except:
            pass