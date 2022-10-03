from telethon import TelegramClient,events
import base64
from time import sleep

@events.register(events.NewMessage(outgoing=True, pattern=r'\.b64'))
async def runb64(event):
    await event.edit("kutib turing...")
    options = event.message.raw_text.split()
    selectsecretmessage = await event.get_reply_message()
    try:
        if options[1] == "en":
            secretmessage = selectsecretmessage.message
            secretmessagebytes = secretmessage.encode("ascii")
            encodesecretmessage = base64.b64encode(secretmessagebytes)
            encodesecretmessagebytes = encodesecretmessage.decode("ascii")
            await event.edit("shifrlanmoqda...")
            sleep(2)
            await event.edit(f"{encodesecretmessagebytes}")
        elif options[1] == "de":
            secretkey = selectsecretmessage.message
            secretkeybytes = secretkey.encode("ascii")
            decodesecretkey = base64.b64decode(secretkeybytes)
            decodesecretkeybytes = decodesecretkey.decode("ascii")
            await event.edit("shifran chiqarilmoqda...")
            sleep(2)
            await event.edit(f"Shifrdan chiaarilgan habar: {decodesecretkeybytes}")
        else:
            await event.edit("notogri variant")
    except IndexError:
        await event.edit("encode yoki decode qilish kerak ekanini yozing misol: b64 en")
    except:
        await event.edit("Nimadir hato") 