from telethon import TelegramClient, events, sync, functions, types, Button

import modullar.client
client = modullar.client.client
botClient = modullar.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
				if query.text == "ahelp":
								result = query.builder.article('Ahelp', text = """
🪄 Umumiy animatsialar: 3
🪄 Berkitilgan animatsialar: 0

💙 Police: police. - sirena animatsiasi
🧠 Brain: brain. - qovoqmiyya
❤️ Magic: - yurklar animatsiasi

🗞 JOJO | USERBOT

					
								""", buttons= [
								[Button.inline("INFORMATION", data=b"1")],
								[Button.url("Tg channel", url="https://t.me/jojo_userbot")]
								
								])
								await query.answer([result])
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
				
				if event.data==b'1':
								await event.answer("JOJO | USERBOT - 1.0.1.2v \nHavfsiz Userbot\nserverga ulangamagan juda oddiy yuserbot\nhar 4 kun ichida yangilanib turadi\ndasturchi: @red_uzbek\nmaqsad: Insonlarga telegramda oz boʻlsa da yordam berish", alert=True)

@events.register(events.NewMessage(pattern=".ahelp"))
async def ahelp(event):
				results = await client.inline_query("@jojo_user_bot", "ahelp")
				await results[0].click(event.chat_id)
				await event.message.delete()