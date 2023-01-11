import tgcrypto
from pyrogram import Client , filters
from pyrogram.types import Message
from random import randint
api_id = 16356512
api_hash = "3be954be110a796e8c0b18f3604a5f2c"
bot_token = "5887975865:AAF8bnF51ZkdHVBlKef3BYSNRs8QaBau8Ew"
bot = Client("session",api_id=api_id,api_hash=api_hash,bot_token=bot_token,workers=6 )

@bot.on_message(filters.media)
def handler(client: Client, message: Message):
  #if message.video or message.sticker or message.document or message.animation or message.audio or message.photo:  
  msg = message.reply("**Recopilando información**")
  filename = str(randint(11111,999999))+".mp4"
  message.download()
  message.reply("Descarga exitosa")
print("started")
bot.run()




