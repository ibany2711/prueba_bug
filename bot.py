from telethon import TelegramClient as Client
from telethon import events

bot = Client('bot',api_id=19961504,api_hash="28de3a8f4b68b388bfe47bf84d1b124b").start(bot_token="5639088541:AAH4ldwbj71Ma0yZa4kBYqBN-xglpxy4vOg")

@bot.on(events.NewMessage)
async def messages(event):
    username = event.message.chat.username
    if event.message.media:	
        await bot.send_message(username,"Comenzando descarga")
        await bot.download_media(event.message.media)
        await bot.send_message(username,"Completada")
if __name__ == "__main__":
	bot.run_until_disconnected()




