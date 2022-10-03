from telethon import events

@events.register(events.NewMessage(outgoing=True, pattern=r'\.spm'))
async def spaminfos(event):
    startbot = "/start"
    messagelocation = event.to_id
    await event.edit("kuting...")
    spambot = "@SpamBot"
    async with event.client.conversation(spambot) as startconversation:
        await startconversation.send_message(startbot)
        message = await startconversation.get_response(1)
        await event.delete()
        await event.client.send_message(messagelocation, message)