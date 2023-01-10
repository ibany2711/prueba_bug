import tgcrypto
from pyrogram import Client , filters
from pyrogram.types import Message

api_id = 16356512
api_hash = "3be954be110a796e8c0b18f3604a5f2c"
bot_token = "5887975865:AAF8bnF51ZkdHVBlKef3BYSNRs8QaBau8Ew"
bot = Client("session",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

@bot.on_message(filters.media)
async def handler(client: Client, message: Message):	
	await message.reply("__**Recopilando información**__")
	await client.download_media(message)
	await message.reply("Descarga exitosa")

print("started")
bot.start()
bot.loop.run_forever()
