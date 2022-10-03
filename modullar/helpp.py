from telethon import TelegramClient, events, sync, functions, types, Button

import modullar.client
client = modullar.client.client
botClient = modullar.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
				if query.text == "help":
								result = query.builder.article('Help', text = """
🛠 **Umumiy modullar**: 22
⚒ **Berkitilgan modullar**:  0

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
🏙 **Guruhdagi azoni kick qilish uchun**: kick. <reply>
🏙 **Mute qilish uchun**: mute. <vaqt> <m, h, d>
🏙 **Calculator**: ccr. <misol>
🏙 **Spamni tekshirish**: spm. 
🏙 **User haqida malumot olish**: .userinfo <reply>

🛠 ~~JOJO USERBOT~~ 					
								""", buttons= [
								[Button.inline("INFORMATION", data=b"1")],
								[Button.url("Tg channel", url="https://t.me/jojo_userbot")]
								
								])
								await query.answer([result])
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
				
				if event.data==b'1':
								await event.answer("JOJO | USERBOT - 1.0.1.2v \nHavfsiz Userbot\nserverga ulangamagan juda oddiy yuserbot\nha 4 kun ichida yangilanib turadi\ndasturchi: @red_uzbek\nmaqsad: Insonlarga telegramda oz boʻlsa da yordam berish", alert=True)

@events.register(events.NewMessage(pattern=".help"))
async def help(event):
				results = await client.inline_query("@jojo_user_bot", "help")
				await results[0].click(event.chat_id)
				await event.message.delete()