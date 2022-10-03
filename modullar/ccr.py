from telethon import events

@events.register(events.NewMessage(outgoing=True, pattern=r'\.ccr'))
async def ccr(event):
    await event.delete()
    messagelocation = event.to_id
    userquestion = event.message.raw_text.split()
    try:
        await event.client.send_message(messagelocation, f"Natija: {eval(userquestion[1])}")
    except:
        pass