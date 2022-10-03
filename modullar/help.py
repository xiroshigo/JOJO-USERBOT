from telethon import TelegramClient, events
import modullar.client
client = modullar.client.client

@events.register(events.NewMessage(pattern=".hjelp"))
async def help(event):
	await event.edit("""
🛠 **Umumiy modullar**: 16
⚒ **Berkitilgan modullar**:  3

🏙 **Tezlik**: ping.
🏙 **Birdaniga hammani ban qilish**: banall.
🏙 **Spamm habar**: spam. <soniya> <takrorlanish> <habar>
🏙 **Textni emojiga aylantiradi**: emoji. <Text>
🏙 **Guruh malumotlarini scanerlaydi**: chatinfo.
🏙 **Chatlaringiz sonini hisoblaydi**: count.
🏙 **Base64 da shifrlaydi**: b64. <en> <reply>
🏙 **Base64 shifrdan yechadi**: b64. <de> <reply>
🏙 **Memli sticker**: mq. <reply>
🏙 **Text sticker**: qq. <reply>
🏙 **Text image**: nq. <reply>
🏙 **Qr code yaratadi**: qrc. <create> <reply>
🏙 **Textni teskari ogiradi**: rev. <reply>
🏙 **Guruh azolarini chaqiradi**: tagall. 
🏙 **Nickname ozgartiradi**: rename. <Nickname>
🏙 **Wiki qidiruv**: wiki. <qidirish uchun soʻz>

🛠 ~~JOJO USERBOT~~ : @JOJO_USERBOT


""")