from pyrogram import Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from os.path import exists
from json import loads,dumps
from pathlib import Path
from os import mkdir
from os import unlink
from time import localtime
from datetime import timedelta
from random import randint
from re import findall
from yarl import URL
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.parse import quote_plus
from time import time
from datetime import datetime
import shutil
import asyncio
import tgcrypto
import aiohttp
import aiohttp_socks
import yt_dlp
import os
import aiohttp
from time import time
import re
from pathlib import Path
from multivolumefile import MultiVolume
from io import BufferedReader
from py7zr import SevenZipFile
from py7zr import FILTER_COPY
from time import time
from os import unlink
from urllib.parse import unquote_plus

api_id = 16356512
api_hash = "3be954be110a796e8c0b18f3604a5f2c"
bot_token = "5887975865:AAF8bnF51ZkdHVBlKef3BYSNRs8QaBau8Ew"

Channel_Id = -1001896483022
bot = Client("uu1",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

boss = ['Yama_Tsukami','Orisha91',"UltraFastSuport"]#usuarios supremos
Configs = {"globaltoken":'', "globalproxy":'', "status":"On", 'Yama_Tsukami': {'z': 900,"m":"e","a":"a"}, 'Orisha91': {'z': 900,"m":"e","a":"a"}, 'UltraFastSuport': {'z': 900,"m":"e","a":"a"}}
Urls = {}

@bot.on_message()
async def hand(client: Client, message: Message):
	username = message.from_user.username
	finame = message.from_user.first_name
	usid = message.from_user.id
	msg = message.text

	
	try:
		await get_messages()
	except:
		#if username in boss:
			#update(username)
			await send_config()
	
	try:
		Urls[username]
	except:
		Urls[username] = []
	
	if len(Urls[username]) >= 10 and msg !="/deletelinks" and username not in boss and Configs[username]["m"]=="e":
		await client.send_message(username,'⛔️ El limite de links fue pasado , utilize **/deletelinks** para continuar')
		return
	else:pass
	
	if msg != "/start" and username not in boss and Configs["status"] == "Off":
		await client.send_message(username,'⛔ Bot Apagado ')
		return
	else:  
		pass	
	
	if username in Configs or username in boss:			
		if exists('downloads/'+str(username)+'/'):pass
		else:os.makedirs('downloads/'+str(username)+'/')	
	else:
		await client.send_message(username,'⛔ No tiene acceso')
		return
	
	if message.audio or message.document or message.animation or message.sticker or message.photo or message.video:
			
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count < 10 or username in boss:pass
		else:
			await client.send_message(username,'🛑Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return		
		
		msg = await message.reply("__**Recopilando información**__")
		try:
			filename = str(message).split('"file_name": ')[1].split(",")[0].replace('"',"")
			filesize = int(str(message).split('"file_size":')[1].split(",")[0])
		except:
			filename = str(randint(11111,999999))+".mp4"
			filesize = int(str(message).split('"file_size":')[1].split(",")[0])
		
		start = time()		
		await bot.download_media(message,file_name="downloads/"+str(username)+'/'+filename,progress=downloadmessage_progres,progress_args=(filename,start,msg))
		if Path("downloads/"+str(username)+'/'+filename).stat().st_size == filesize:
			await msg.edit("Descarga exitosa")
			if Configs[username]["m"] == "u":
				upload = await uploadfile("downloads/"+str(username)+'/'+filename,usid,msg,username)
			elif Configs[username]["m"] == "e":
				upload = await uploadfileapi("downloads/"+str(username)+'/'+filename,usid,msg,username)
			else:
				upload = await upload_repo("downloads/"+str(username)+'/'+filename,usid,msg,username)
	
	if message.text.startswith("/start"):
		proxy = Configs["globalproxy"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
		session = aiohttp.ClientSession(connector=connector)
		url = len(Urls[username])
		urltotal = 0
		for us in Urls:
			urltotal+=len(Urls[us])
		zipps = str(Configs[username]["z"])
		total = shutil.disk_usage(os.getcwd())[0]
		used = shutil.disk_usage(os.getcwd())[1]
		free = shutil.disk_usage(os.getcwd())[2]
		startoken = Configs["globaltoken"]
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
			#print(initial_count)

		a = await client.send_message(username,'**🔎 Buscando Datos**')
		try:
			async with session.get("https://educa.uho.edu.cu/",timeout=6) as resp:
				await resp.text()
				statused = "✔️"
		except: statused = "🔴"
		
		try:
			async with session.get("https://moodle.uclv.edu.cu/",timeout=6) as resp:
				await resp.text()
				statusuc = "✔️"
		except:statusuc = "🔴"
		
		try:
			async with session.get("https://repotematico.uo.edu.cu/",timeout=6) as resp:
				await resp.text()
				statusre = "✔️"
		except:statusre = "🔴"
		msg = f"**𝔅𝔦𝔢𝔫𝔳𝔢𝔫𝔦𝔡𝔬** {finame}\n\n"
		
		msg += f"✧ 𝕮𝖔𝖓𝖋𝖎𝖌𝖚𝖗𝖆𝖈𝖎𝖔𝖓:\n"
		msg += f"➣𝘡𝘪𝘱𝘴 𝘤𝘰𝘯𝘧𝘪𝘨𝘶𝘳𝘢𝘥𝘰𝘴 𝘢: **{zipps}MB**\n"
		if initial_count > 10:	
			msg += f"➣𝘙𝘰𝘰𝘵: 𝐎𝐜𝐮𝐩𝐚𝐝𝐨. 𝐄𝐥𝐢𝐦𝐢𝐧𝐞 𝐩𝐚𝐫𝐚 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐚𝐫\n"
			msg += f"➣𝘌𝘭𝘪𝘮𝘪𝘯𝘢𝘳 𝘭𝘪𝘯𝘬𝘴 𝘦𝘯 𝘳𝘰𝘰𝘵 **/deleteall**\n"
		else:
			msg += f"➣𝘙𝘰𝘰𝘵: 𝐃𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞. 𝐏𝐮𝐞𝐝𝐞 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐚𝐫\n"	
		msg += "➣𝘌𝘴𝘵𝘢𝘥𝘰 𝘥𝘦𝘭 𝘣𝘰𝘵: "+ Configs["status"] +"\n\n"
		msg += f"♽ 𝕾𝖙𝖔𝖗𝖆𝖌𝖊 𝕮𝖔𝖓𝖙𝖗𝖔𝖑 :\n"
		msg += f"➣𝘛𝘰𝘵𝘢𝘭 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **{sizeof_fmt(used)}** / **{sizeof_fmt(total)}**\n"
		msg += f"➣𝘍𝘳𝘦𝘦 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **{sizeof_fmt(free)}**\n"
		msg += f"➣𝘊𝘭𝘦𝘢𝘳 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **/free_storage**\n"
		
		if startoken != '':
			msg += f"➣𝘛𝘰𝘬𝘦𝘯: ✅\n"
		else:
			msg +="➣𝘛𝘰𝘬𝘦𝘯: 🔴\n\n"
		if Configs[username]["m"] == "e":
			msg+= f"\n➣𝘌𝘥𝘶𝘤𝘢: {statused}   **⤶ You**\n"
			msg+= f"➣𝘜𝘤𝘭𝘷: {statusuc}\n"
			msg+= f"➣𝘙𝘦𝘱𝘰: {statusre}\n"
		elif Configs[username]["m"] == "u":
			msg+= f"\n➣𝘌𝘥𝘶𝘤𝘢: {statused}\n"
			msg+= f"➣𝘜𝘤𝘭𝘷: {statusuc}   **⤶ You**\n"
			msg+= f"➣𝘙𝘦𝘱𝘰: {statusre}\n"
		else: 
			msg+= f"\n➣𝘌𝘥𝘶𝘤𝘢: {statused}\n"
			msg+= f"➣𝘜𝘤𝘭𝘷: {statusuc}\n"
			msg+= f"➣𝘙𝘦𝘱𝘰: {statusre}   **⤶ You**\n"
		msg+= f"\n ➣𝘛𝘰𝘵𝘢𝘭 𝘉𝘰𝘵 𝘜𝘙𝘓𝘴: {urltotal}\n"
		msg += f"➣𝘓𝘪𝘯𝘬𝘴 𝘚𝘶𝘣𝘪𝘥𝘰𝘴: {url}\n"
		msg+= "➣𝘋𝘦𝘭𝘦𝘵𝘦 𝘠𝘰𝘶𝘳 𝘜𝘙𝘓𝘴: **/deletelinks**\n"
		await a.edit(msg)

	if message.text == "/change_status" :
		if username in boss:
			if Configs["status"] == "Off":
				Configs["status"] = "On"
			else:
				Configs["status"] = "Off"
			await client.send_message(username,f"Status cambiado a "+  Configs["status"])
			await send_config()
		else :
			await client.send_message(username,"🚷 Comando para administradores")
			return

	if "/users" == msg:
		if username not in boss:
			await client.send_message(username,"🚷 Comando para administradores")
			return		
		total = len(Configs) - 6
		message = "**Usuarios: **"+ str(total)+'\n\n'
		for user in Configs:
			if user == "globaltoken":continue
			if user == "globalproxy":continue
			if user == "status":continue
			if user == "Yama_Tsukami":continue
			if user == "Orisha91":continue
			if user == "UltraFastSuport":continue
			ic = 0
			if not exists ('downloads/'+ str(user)+'/'):
				mkdir ('downloads/'+ str(user)+'/')
			icd = 'downloads/'+ str(user)+'/'
			for g in os.listdir(icd):
				if os.path.isfile(os.path.join(icd, g)):
					ic += 1

			message+=f"{user}\n"
		msg = f"{message}\n"
		await client.send_message(username,msg)
	
	if message.text.startswith('/zips'):
		list = msg.split(" ")		
		if len(list)!=2:
			await message.reply("Manera Correcta:\n**/zips 500**.")
			return		
		zips = list[1]
		try:
			zips = int(zips)
		except:
			await message.reply("Los zips deben ser un numero entero.")
			return		
		Configs[username]["z"] = zips
		await send_config()
		try:
			await message.reply("✅ Done!")
		except:
			await message.reply("Ha intentado establecer la misma configuracion.")
	
	if message.text.startswith('/add'): 
		list = msg.split(" ")		
		if not username in boss:
			await message.reply("🚷 Comando para administradores")
			return			
		if len(list)!=2:
			await message.reply("Manera Correcta:\n**/add username**.")
			return		
		uss = list[1]
		Configs[uss] ={"z":99,"m":"u","a":"n"}	
		await send_config()
		await client.send_message(username,f"@{uss} Add")
	
	if message.text.startswith('/set_proxy'):	
		if username in boss:
			tokeno = str(msg.split(' ')[1])
			tokeno = iprox(tokeno.replace('socks5://',''))
			Configs["globalproxy"] = tokeno
			await client.send_message(username,'Proxy cargado')			
			await send_config()
		else:
			await client.send_message(username,"🚷 Comando para administradores")
			return
	
	if message.text.startswith("/educa"):
		if Configs[username]["a"] == "a" or Configs[username]["a"] == "re": 
			Configs[username]["m"] = "e"
			await send_config()
			await client.send_message(usid,"Modo de subida configurado a Educa")
		else: 
			await client.send_message(username,"🚷 No ha pagado por este servicio")
			return
	
	if message.text.startswith("/uclv"):
		if Configs[username]["a"] == "a":
			Configs[username]["m"] = "u"
			await send_config()
			await client.send_message(usid,"Modo de subida configurado a UCLV")
		else: 
			await client.send_message(username,"🚷 No ha pagado por este servicio")
			return
	
	if message.text.startswith("/repo"):
		if Configs[username]["a"] == "a" or Configs[username]["a"] == "re":
			Configs[username]["m"] = "r"
			await send_config()
			await client.send_message(usid,"Modo de subida configurado a Repotematico")
		else: 
			await client.send_message(username,"🚷 No ha pagado por este servicio")
			return
				
	if message.text.startswith('/set_token'):	
		if username in boss:
			tokeno = str(msg.split(' ')[1])
			Configs["globaltoken"] = tokeno
			await client.send_message(username,'Token cargado')			
			await send_config()
		else:
			await client.send_message(username,"🚷 Comando para administradores")
			return

	if message.text.startswith('/kick'):
		list = msg.split(" ")		
		if not username in boss:
			await message.reply("🚷 Comando para administradores")
			return			
		if len(list)!=2:
			await message.reply("Manera Correcta:\n**/kick username**.")
			return		
		uss = list[1]
		del Configs[uss]
		await send_config()
		await client.send_message(username,f'@{uss} Kick')
	
	if msg.startswith('/deletelinks'):
			proxy = Configs["globalproxy"]
			if proxy == "":
				proxy = aiohttp.TCPConnector()
			else:
				proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
			async with aiohttp.ClientSession(connector=proxy) as session:
				total_urls = len(Urls[username])
				if total_urls == 0:
					await bot.send_message(usid,"🔄Su total de URLs es igual a 0 no puede borrar")
					return
				deleted = 0
				for url in Urls[username]:
					link = f"https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/delete_file/archivo/{url}?_=1670274909872"
					async with session.get(link) as response:
						if loads(await response.text())["success"]:
							deleted+=1
				if total_urls == deleted:
					Urls[username] = []
					await client.send_message(usid,"**Eliminados exitosamente**")
					await client.send_message(-1001801166709,f"**@{username}** **#Elimino** {total_urls} links")
	
	if message.text.startswith('/ls'):
		msg = files_formatter('downloads/'+str(username)+'/',username)
		await message.reply(msg)
	
	if message.text.startswith('/rm'):
		list = msg.split("/rm")[1]	
		filespath = Path('downloads/'+ str(username)+'/')
		result = []
		for p in filespath.rglob("*"):
			if p.is_file():
				result.append(str(Path(p).name))
		result.sort()
		try:
			unlink('downloads/'+ str(username)+'/'+result[int(list)])
			msg = files_formatter('downloads/'+ str(username)+'/',username)
			await message.reply(msg)
		except: pass
	
	if message.text.startswith('/deleteall'):
		filespath = Path('downloads/'+ str(username)+'/')
		result = []
		for p in filespath.rglob("*"):
			if p.is_file():
				result.append(str(Path(p).name))				
		for f in result:
			unlink('downloads/'+ str(username)+'/'+f)
		msg = files_formatter('downloads/'+ str(username)+'/',username)
		await message.reply(msg)

	if "/free_storage" == msg:
		if username not in boss:
			await client.send_message(username,"🚷Comando para administradores")
			return
		try:
			shutil.rmtree("downloads/")
			await client.send_message(username,"Almacenamiento Liberado")
		except Exception as ex:
			await client.send_message(username,f"💢 {ex}")

	if message.text.startswith('/upload'):
		list = int(msg.split("/upload")[1])		
		filespath = Path('downloads/'+ str(username)+'/')
		result = []
		for p in filespath.rglob("*"):
			if p.is_file():
				result.append(str(Path(p).name))
		result.sort()
		try:
			path = 'downloads/'+ str(username)+'/'+result[list]
			msg = await message.reply(f"**Seleccionado** {path}")
			if Configs[username]["m"] == "u":
				await uploadfile(path,usid,msg,username)
			elif Configs[username]["m"] == "r":
				await upload_repo(path,usid,msg,username)
			else:
				await uploadfileapi(path,usid,msg,username)
		except Exception as ex:
			await client.send_message(username,f"💢 {ex}")
#**********YOUTUBE************
	elif "youtu.be/" in msg or "twitch.tv/" in msg or "youtube.com/" in msg or "xvideos.com" in msg or "xnxx.com" in msg:
		#Restringir a 1 archivo
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count < 10 or username in boss:
			pass
		else:
			await client.send_message(username,'🛑Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return

		list = msg.split(" ")
		url = list[0]
		
		try:
			format = str(list[1])
		except:
			format = "720"
		
		msg = await message.reply("__**Recopilando información**__")
		await client.send_message(-1001801166709,f'**@{username} #Envio un link de youtube:**\n**Url:** {url}\n**Formato:** {str(format)}p')
		download = await ytdlp_downloader(url,usid,msg,username,lambda data: download_progres(data,msg,format),format)
		if Configs[username]["m"] == "u":
				await uploadfile(download,usid,msg,username)
		elif Configs[username]["m"] == "r":
				await upload_repo(download,usid,msg,username)
		else:
				await uploadfileapi(download,usid,msg,username)

#**********MEDIAFIRE**********		
	elif message.text.startswith("https://www.mediafire.com/"):
		#Restringir a 1 archivo
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count < 10 or username in boss:
			pass
		else:
			await client.send_message(username,'🛑Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return
		
		url = msg
		
		if "?dkey=" in str(url):
			url = str(url).split("?dkey=")[0]
		
		msg = await message.reply("__**Recopilando información**__")
		await client.send_message(-1001801166709,f'**@{username} #Envio un link de mediafire:**\n**Url:** {url}\n')
		file = await download_mediafire(url, 'downloads/'+str(username)+'/', msg, callback=mediafiredownload)
		if Configs[username]["m"] == "u":
				await uploadfile(file,usid,msg,username)
		elif Configs[username]["m"] == "r":
				await upload_repo(file,usid,msg,username)
		else:
				await uploadfileapi(file,usid,msg,username)
	
#*********HTTP****************	
	elif message.text.startswith("https"):
		initial_count = 0
		dir = 'downloads/'+ str(username)+'/'
		for path in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, path)):
				initial_count += 1
		if initial_count < 10 or username in boss:
			pass
		else:
			await client.send_message(username,'🛑Su almacenamiento esta ocupado, para continuar use **/deleteall**')
			return
		
		url = msg
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as r:
				try:
					filename = unquote_plus(url.split("/")[-1])
				except:
					filename = r.content_disposition.filename
				fsize = int(r.headers.get("Content-Length"))
				msg = await message.reply("__**Recopilando información**__")
				await client.send_message(-1001801166709,f'**@{username} #Envio un link :**\n**Url:** {url}\n')
				f = open(f"downloads/{username}/{filename}","wb")
				newchunk = 0
				start = time()
				async for chunk in r.content.iter_chunked(1024*1024):
					newchunk+=len(chunk)
					await mediafiredownload(newchunk,fsize,filename,start,msg)
					f.write(chunk)
				f.close()
				file = f"downloads/{username}/{filename}"
				await msg.edit("✅**Archivo descargado.**")
				if Configs[username]["m"] == "u":
					await uploadfile(file,usid,msg,username)
				elif Configs[username]["m"] == "r":
					await upload_repo(file,usid,msg,username)
				else:
					await uploadfileapi(file,usid,msg,username)
                
seg = 0

async def ytdlp_downloader(url,usid,msg,username,callback,format):
	class YT_DLP_LOGGER(object):
		def debug(self,msg):
			pass
		def warning(self,msg):
			pass
		def error(self,msg):
			pass
	resolution = str(format)	
	dlp = {"logger":YT_DLP_LOGGER(),"progress_hooks":[callback],"outtmpl":f"./downloads/{username}/%(title)s.%(ext)s","format":f"best[height<={resolution}]"}
	downloader = yt_dlp.YoutubeDL(dlp)
	loop = asyncio.get_running_loop()
	filedata = await loop.run_in_executor(None,downloader.extract_info, url)
	filepath = downloader.prepare_filename(filedata)
	return filedata["requested_downloads"][0]["_filename"]	

def download_progres(data,message,format):
	if data["status"] == "downloading":
		filename = data["filename"].split("/")[-1]
		_downloaded_bytes_str = data["_downloaded_bytes_str"]
		_total_bytes_str = data["_total_bytes_str"]
		if _total_bytes_str == "N/A":
			_total_bytes_str = data["_total_bytes_estimate_str"]		
		_speed_str = data["_speed_str"].replace(" ","")
		_eta_str = data["_eta_str"]
		_format_str = format		
		msg= f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
		msg+= f"▶️ 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {_downloaded_bytes_str} of {_total_bytes_str} ({_speed_str})\n\n"
		msg+= f"🎥Resolución: {_format_str}p\n\n"	
		global seg 
		if seg != localtime().tm_sec:
		#if int(localtime().tm_sec) % 2 == 0 :
			try:
				message.edit(msg,reply_markup=message.reply_markup)
			except:
				pass
		seg = localtime().tm_sec

async def mediafiredownload(chunk,total,filename,start,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	timeto = round(total - chunk) / mbs
	msg= f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
	msg+= f"▶️ 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(chunk)} of {sizeof_fmt(total)} ({sizeof_fmt(mbs)}/s)\n\n"
	delta = timedelta(seconds=int(timeto))
	tim = str(delta).split(":")[1]+"m,"+str(delta).split(":")[2]+"s"
	#msg+= f"⏰{tim}"
	global seg
	#if int(localtime().tm_sec) % 2 == 0 :
	if seg != localtime().tm_sec:
		try:
			await message.edit(msg)
		except:
			pass
	seg = localtime().tm_sec
	
async def downloadmessage_progres(chunk,filesize,filename,start,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	timeto = round(filesize - chunk) / mbs
	msg= f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
	msg+= f"▶️ 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(chunk)} of {sizeof_fmt(filesize)} ({sizeof_fmt(mbs)}/s)\n\n"
	delta = timedelta(seconds=int(timeto))
	tim = str(delta).split(":")[1]+"m,"+str(delta).split(":")[2]+"s"
	global seg
	#if int(localtime().tm_sec) % 2 == 0 :
	if seg != localtime().tm_sec:
		try:
			await message.edit(msg)
		except:
			pass
	seg = localtime().tm_sec

async def uploadfile(file,usid,msg,username):
	usernamew = ''
	passwordw = ''
	moodle = "https://moodle.uclv.edu.cu"
	uplog = "token"
	rep = 4
	token = Configs["globaltoken"]
	zips = Configs[username]["z"]
	if int(zips) > 399:
		await msg.edit("⛔ Si usa UCLV los zips no pueden ser mayores a 399 MB")
		return
	proxy = Configs["globalproxy"]
	if proxy == "":
		proxy = aiohttp.TCPConnector()
	else:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
		
	await msg.edit("__**Recopilando información**__")
	filename = Path(file).name
	filenamex = file.split("/")[-1]
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	logerrors = 0
	logslinks = []
	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"[📦] Comprimiendo\nZips: {parts}\nTamaño: {sizeof_fmt(zipssize)}")
		files = sevenzip(file,volume=zipssize)
		if uplog == "token":		
			client = MoodleClient(usernamew,passwordw,moodle,proxy)
			for path in files:
				while logerrors < 20:
					try:
						upload = await client.uploadtoken(path,lambda chunk,total,start,filen: uploadfile_progres(chunk,total,start,filen,msg),token)
						await bot.send_message(usid,f"✅ Uᴘʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ\n\n🖇[{filenamex}]({upload})",disable_web_page_preview=True)
						logslinks.append(upload)
						break
					except:
						logerrors+=1	
			if len(logslinks) == len(files):
				await msg.edit("Finalizado exitosamente")
				with open(filename+".txt","w") as f:
					message = ""
					for li in logslinks:
						message+=li+"\n"
					f.write(message)
				
				await bot.send_document(usid,filename+".txt")
				os.unlink(filename+".txt")
			else:
				await msg.edit("Ha fallado la subida")
			
	else:
		if uplog == "token":		
			client = MoodleClient(usernamew,passwordw,moodle,proxy)
			while logerrors<20:
				try:
					upload = await client.uploadtoken(file,lambda chunk,total,start,filen: uploadfile_progres(chunk,total,start,filen,msg),token)
					await bot.send_message(usid,f"✅ Uᴘʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ\n\n🖇[{filenamex}]({upload})",disable_web_page_preview=True)
					logslinks.append(upload)
					break
				except:
					logerrors+=1
			if len(logslinks) == 1:
				await msg.edit("Finalizado exitosamente")
				with open(filename+".txt","w") as f:
					message = ""
					lin = ""
					for li in logslinks:
						message+=li+"\n"
						lin+=li+"\n"
					f.write(message)				
				await bot.send_document(usid,filename+".txt")							
				await bot.send_message(-1001354171639,f"🖍 Nombre: {filename}\n📦 Tamaño: {sizeof_fmt(filesize)}\n🖇 Enlaces:\n{lin}")
				await bot.send_document(-1001354171639,filename+".txt")
				os.unlink(filename+".txt")
			else:
				await msg.edit("Ha fallado la subida")

async def uploadfileapi(file,usid,msg,username):
	host = "https://educa.uho.edu.cu/"
	proxy = Configs["globalproxy"]
	zips = Configs[username]["z"]
	if int(zips) > 999 and username not in boss:
		await msg.edit("⛔ Si usa Educa los zips no pueden ser mayores a 999 MB")
		return
	if proxy == "":
		proxy = aiohttp.TCPConnector()
	else:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	await msg.edit("__**Recopilando información**__")
	filename = file.split("/")[-1]
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	logslinks = []
	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"[📦] Comprimiendo\nZips: {parts}\nTamaño: {sizeof_fmt(zipssize)}")
		files = sevenzip(file,volume=zipssize)
		session = aiohttp.ClientSession(connector=proxy)
		for file in files:
			try:
				if file.endswith(".zip"):
						filename_god = file
				else:
						file = filezip(file,volume=None)
						filename_god = file[0].split("zip")[0]+".zip"
						os.rename(file[0],filename_god)
				fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
				query = {"s97304e7e":fi}
				async with session.post("https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/upload_file/archivo",data=query,timeout=60*30) as resp:
							url = loads(await resp.text())["files"][0]["url"]
							await bot.send_message(usid,f"✅ Uᴘʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ\n\n🖇[{Path(filename_god).name}]({url})",disable_web_page_preview=True)
							logslinks.append(url)
							Urls[username].append(url.split("/")[-1])
			except Exception as ex:
				await msg.edit(f"{ex}")
		if len(logslinks) == len(files):
				await msg.edit("**Finalizado exitosamente**")
						
				with open(filename_god+".txt","w") as t:
						message = ""
						lin = ""
						for li in logslinks:
							message+=li+"\n"
							lin+=li+"\n"
						t.write(message)
				await bot.send_document(usid,filename_god+".txt")
				await bot.send_message(-1001354171639,f"🖍 Nombre: {filename}\n📦 Tamaño: {sizeof_fmt(filesize)}\n🖇 Enlaces:\n{lin}")
				await bot.send_document(-1001354171639,filename_god+".txt")
				os.unlink(filename_god+".txt")
		else:
			await msg.edit("Ha fallado la subida ")
	else:
			async with aiohttp.ClientSession(connector=proxy) as session:
				try:
					if file.endswith(".zip"):
							filename_god = file
					else:
							file = filezip(file,volume=None)
							filename_god = file[0].split("zip")[0]+".zip"
							os.rename(file[0],filename_god)
					fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
					query = {"s97304e7e":fi}
					async with session.post("https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/upload_file/archivo",data=query,timeout=60*30) as resp:
							url = loads(await resp.text())["files"][0]["url"]
							await bot.send_message(usid,f"✅ Uᴘʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ\n\n🖇[{Path(filename_god).name}]({url})",disable_web_page_preview=True)
							logslinks.append(url)
							Urls[username].append(url.split("/")[-1])
				except Exception as ex:
							await msg.edit(f"{ex}")
			if len(logslinks) == 1:
						await msg.edit("**Finalizado exitosamente**")
						with open(filename_god+".txt","w") as t:
								message = ""
								lin = ""
								for li in logslinks:
									message+=li+"\n"
									lin+=li+"\n"
								t.write(message)
						await bot.send_document(usid,filename_god+".txt")
						await bot.send_message(-1001354171639,f"🖍 Nombre: {filename}\n📦 Tamaño: {sizeof_fmt(filesize)}\n🖇 Enlaces:\n{lin}")
						await bot.send_document(-1001354171639,filename_god+".txt")
						os.unlink(filename_god+".txt")
			else:
				await msg.edit("Ha fallado la subida")

async def upload_repo(file,usid,msg,username):
	proxy = Configs["globalproxy"]
	zips = Configs[username]["z"]
	if int(zips) > 100:
		await msg.edit("⛔ Si usa Repotematico los zips no pueden ser mayores a 100 MB")
		return
	if proxy == "":
		proxy = aiohttp.TCPConnector()
	else:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	await msg.edit("__**Recopilando información**__")
	filename = file.split("/")[-1]
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	logslinks = []
	session = aiohttp.ClientSession(connector=proxy)
	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"[📦] Comprimiendo\nZips: {parts}\nTamaño: {sizeof_fmt(zipssize)}")
		files = sevenzip(file,volume=zipssize)
		await create_session(session)
		for file in files:
			print("ok")
			try:
				print("try")
				if file.endswith(".zip"):
						filename_god = file
				else:
						print("else")
						file = filezip(file,volume=None)
						print(file)
						filename_god = file[0].split("zip")[0]+".zip"
						print(filename)
						os.rename(file[0],filename_god)
				fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
				print("ok fi")
				upload = await upload_file(fi,session)
				print("ok upload")
				await bot.send_message(usid,f"✅ Uᴘʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ\n\n🖇[{Path(filename_god).name}]({upload})",disable_web_page_preview=True)
				logslinks.append(upload)
			except Exception as ex:
				print(ex)
				pass
		print(len(files)); print(len(logslinks))
		if len(logslinks) == len(files):
				await msg.edit("**Finalizado exitosamente**")
						
				with open(filename_god+".txt","w") as t:
						message = ""
						lin = ""
						for li in logslinks:
								message+=li+"\n"
								lin+=li+"\n"
						t.write(message)
				await bot.send_document(usid,filename_god+".txt")
				await bot.send_message(-1001354171639,f"🖍 Nombre: {filename}\n📦 Tamaño: {sizeof_fmt(filesize)}\n🖇 Enlaces:\n{lin}")
				await bot.send_document(-1001354171639,filename_god+".txt")
				os.unlink(filename_god+".txt")
		else:
			await msg.edit(" Ha fallado la subida")
	else:
			await create_session(session)	
			try:
				if file.endswith(".zip"):
						filename_god = file
				else:
						file = filezip(file,volume=None)
						filename_god = file[0].split("zip")[0]+".zip"
						os.rename(file[0],filename_god)
				fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
				upload = await upload_file(fi,session)
				await bot.send_message(usid,f"✅ Uᴘʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ\n\n🖇[{Path(filename_god).name}]({upload})",disable_web_page_preview=True)
				logslinks.append(upload)
			except Exception as ex:
				print(ex)
				pass
			if len(logslinks) == 1:
					await msg.edit("**Finalizado exitosamente**")
					with open(filename_god+".txt","w") as t:
								message = ""
								lin = ""
								for li in logslinks:
									message+=li+"\n"
									lin+=li+"\n"
								t.write(message)
					await bot.send_document(usid,filename_god+".txt")
					await bot.send_message(-1001354171639,f"🖍 Nombre: {filename}\n📦 Tamaño: {sizeof_fmt(filesize)}\n🖇 Enlaces:\n{lin}")
					await bot.send_document(-1001354171639,filename_god+".txt")
					os.unlink(filename_god+".txt")
			else:
				await msg.edit("Ha fallado la subida")

async def create_session(session,username='obysoft',password='Obysoft2001@'):
    HOST = 'https://repotematico.uo.edu.cu/'
    HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    user = username+str(randint(00000000000000,99999999999999))
    mail = f'{user}@gmail.com'
    regurl = f'{HOST}user/register'
    resp = await session.get(regurl,headers=HEADERS)
    soup = BeautifulSoup(await resp.text(),'html.parser')
    formreg = soup.find('form',{'id':'user-register-form'})
    #print(await resp.text())
    inputs = formreg.find_all('input')
    upload_data = {
                'timezone':(None,'America/New_York'),
                'form_build_id':(None,user),
                'form_id':(None,'user_register_form'),
                'op':(None,'Crear nueva cuenta')
                }
    for input in inputs:
        for item in upload_data:
            try:
                if item == input['name']:
                    upload_data[item] = (None,input['value'])
            except:pass
    upload_data['name'] = (None,user)
    upload_data['mail'] = (None,mail)
    upload_data['pass[pass1]'] = (None,password)
    upload_data['pass[pass2]'] = (None,password)
    HEADERS['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    cookies = {**resp.cookies}
    cookie = 'has_js=1; '
    for cook in cookies:
        cookie += f'{cook}={cookies[cook]}'
    resp = await session.post(regurl,data=upload_data,headers=HEADERS)
    log = 'No se a podido crear la session'
    if resp.url!=regurl:
        soup = BeautifulSoup(await resp.text(),'html.parser')
        messages = soup.find('div',{'class':'messages'})
        if messages:
            try:
                log = messages.contents[2]
            except:
                log = 'Se a creado la session correctamente'

async def upload_file(path,session):
            urlup = f'https://repotematico.uo.edu.cu/node/add/objetos-de-aprendizaje'
            resp = await session.get(urlup)
            soup = BeautifulSoup(await resp.text(),'html.parser')
            form = soup.find('form',{'id':'objetos-de-aprendizaje-node-form'})
            of = path
            upload_data = {}
            upload_data['title'] = ''
            upload_data['changed'] = ''
            upload_data['form_build_id'] = ''
            upload_data['form_token'] = ''
            upload_data['form_id'] = ''
            upload_data['field_oautor[und][0][value]'] = ''
            upload_data['field_psubido_por[und][0][value]'] = ''
        
            upload_data['field_oimagen[und][0][fid]'] = ''
            upload_data['field_oimagen[und][0][display]'] = ''
            upload_data['body[und][0][summary]'] = ''
            upload_data['body[und][0][value]'] = ''
        
            upload_data['field_pcc_by[und][0][fid]'] = ''
            upload_data['field_pcc_by[und][0][display]'] = ''
            upload_data['field_pcc_by_sa[und][0][fid]'] = ''
            upload_data['field_pcc_by_sa[und][0][display]'] = ''
            upload_data['field_pcc_by_nd[und][0][fid]'] = ''
            upload_data['field_pcc_by_nd[und][0][display]'] = ''
            upload_data['field_pcc_by_nc[und][0][fid]'] = ''
            upload_data['field_pcc_by_nc[und][0][display]'] = ''
            upload_data['field_pcc_by_nc_sa[und][0][fid]'] = ''
            upload_data['field_pcc_by_nc_sa[und][0][display]'] = ''
            upload_data['field_pcc_by_nc_nd[und][0][fid]'] = ''
            upload_data['field_pcc_by_nc_nd[und][0][display]'] = ''
            upload_data['field_pgnu_gpl[und]'] = '_none'
            upload_data['field_pgpl_v1[und][0][fid]'] = ''
            upload_data['field_pgpl_v1[und][0][display]'] = ''
            upload_data['field_pgpl_v2[und][0][fid]'] = ''
            upload_data['field_pgpl_v2[und][0][display]'] = ''
            upload_data['field_pgpl_v3[und][0][fid]'] = ''
            upload_data['field_pgpl_v3[und][0][display]'] = ''

            upload_data['field_odescarga[und][0][fid]'] = '0'
            upload_data['field_odescarga[und][0][display]'] = ''
            upload_data['field_pgfdl[und][0][fid]'] = ''
            upload_data['field_pgfdl[und][0][display]'] = ''
            upload_data['path[alias]'] = ''
        
            upload_data['ajax_page_state[css][modules/system/system.base.css]'] = ''
            upload_data['ajax_page_state[css][modules/system/system.menus.css]'] = ''
            upload_data['ajax_page_state[css][modules/system/system.messages.css]'] = ''
            upload_data['ajax_page_state[css][modules/system/system.theme.css]'] = ''
            upload_data['ajax_page_state[css][misc/ui/jquery.ui.core.css]'] = ''
            upload_data['ajax_page_state[css][misc/ui/jquery.ui.theme.css]'] = ''
            upload_data['ajax_page_state[css][misc/ui/jquery.ui.button.css]'] = ''
            upload_data['ajax_page_state[css][misc/ui/jquery.ui.resizable.css]'] = ''
            upload_data['ajax_page_state[css][misc/ui/jquery.ui.dialog.css]'] = ''
            upload_data['ajax_page_state[css][modules/system/system.admin.css]'] = ''
            upload_data['ajax_page_state[css][modules/system/system.admin.css]'] = ''
            upload_data['ajax_page_state[css][misc/vertical-tabs.css]'] = ''
            upload_data['ajax_page_state[css][modules/book/book.css]'] = ''
            upload_data['ajax_page_state[css][modules/comment/comment.css]'] = ''
            upload_data['ajax_page_state[css][modules/field/theme/field.css]'] = ''
            upload_data['ajax_page_state[css][modules/node/node.css]'] = ''
            upload_data['ajax_page_state[css][modules/search/search.css]'] = ''
            upload_data['ajax_page_state[css][modules/user/user.css]'] = ''
            upload_data['ajax_page_state[css][sites/all/modules/views/css/views.css]'] = ''
            upload_data['ajax_page_state[css][sites/all/modules/ckeditor/css/ckeditor.css]'] = ''
            upload_data['ajax_page_state[css][sites/all/modules/ctools/css/ctools.css'] = ''
            upload_data['ajax_page_state[css][sites/all/modules/tagadelic/tagadelic.css]'] = ''
            upload_data['ajax_page_state[css][sites/all/modules/cycle/stylesheets/drupal-cycle.css]'] = ''
            upload_data['ajax_page_state[css][sites/all/modules/ckeditor/css/ckeditor.editor.css]'] = ''
            upload_data['ajax_page_state[css][modules/filter/filter.css]'] = ''
            upload_data['ajax_page_state[css][modules/file/file.css]'] = ''
            upload_data['ajax_page_state[css][modules/image/image.css]'] = ''
            upload_data['ajax_page_state[css][modules/image/image.css]'] = ''
            upload_data['ajax_page_state[css][sites/all/themes/touch/style.css]'] = ''
            upload_data['ajax_page_state[js][0]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/ckeditor/includes/ckeditor.utils.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/libraries/ckeditor/ckeditor.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/jquery/1.10/jquery.min.js]'] = ''
            upload_data['ajax_page_state[js][misc/jquery-extend-3.4.0.js]'] = ''
            upload_data['ajax_page_state[js][misc/jquery.once.js]'] = ''
            upload_data['ajax_page_state[js][misc/drupal.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.core.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.widget.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.button.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.mouse.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.draggable.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.position.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.resizable.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/ui/minified/jquery.ui.dialog.min.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/ui/external/jquery.cookie.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/replace/misc/jquery.form.min.js]'] = ''
            upload_data['ajax_page_state[js][misc/vertical-tabs.js]'] = ''
            upload_data['ajax_page_state[js][misc/states.js]'] = ''
            upload_data['ajax_page_state[js][misc/form.js]'] = ''
            upload_data['ajax_page_state[js][misc/ajax.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/jquery_update/js/jquery_update.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/admin_menu/admin_devel/admin_devel.js]'] = ''
            upload_data['ajax_page_state[js][public://languages/es_hqb_krYVjzr4GA3jB0eHRzekT05UwKk2YOZI3UdJiXA.js]'] = ''
            upload_data['ajax_page_state[js][misc/progress.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/autologout/autologout.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/cycle/cycle.js]'] = ''
            upload_data['ajax_page_state[js][misc/autocomplete.js]'] = ''
            upload_data['ajax_page_state[js][misc/textarea.js]'] = ''
            upload_data['ajax_page_state[js][modules/field/modules/text/text.js]'] = ''
            upload_data['ajax_page_state[js][modules/filter/filter.js]'] = ''
            upload_data['ajax_page_state[js][misc/collapse.js]'] = ''
            upload_data['ajax_page_state[js][modules/file/file.js]'] = ''
            upload_data['ajax_page_state[js][modules/path/path.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/modules/conditional_fields/js/conditional_fields.js]'] = ''
            upload_data['ajax_page_state[js][sites/all/themes/touch/js/scrolltopcontrol.js]'] = ''
            upload_data['ajax_page_state[jquery_version]'] = '1.7'
            upload_data['ajax_iframe_upload'] = '1'

            for data in upload_data:
                try:
                    upload_data[data] = form.find('input',{'name':data})['value']
                except:pass
                if '[css]' in data or '[js]' in data:
                    upload_data[data] = '1'
                if '[fid]' in data:
                    upload_data[data] = '0'
                if '[display]' in data:
                    upload_data[data] = '1'

            upload_data['body[und][0][format]'] = 'filtered_html'
            upload_data['field_plicencia[und]'] = '_none'
            upload_data['field_pcreative_commons[und]'] = '_none'
            upload_data['field_ofacultad[und]'] = '_none'
            upload_data['field_ongenier_a_mec_nica_e_indu[und]'] = '_none'
            upload_data['field_oiencias_econ_micas_y_empr[und]'] = '_none'
            upload_data['field_oingenier_a_el_ctrica[und]'] = '_none'
            upload_data['field_oiencias_naturales_y_exact[und]'] = '_none'
            upload_data['field_ociencias_sociales[und]'] = '_none'
            upload_data['field_oconstrucci_n[und]'] = '_none'
            upload_data['field_ocultura_f_sica[und]'] = '_none'
            upload_data['field_oderecho[und]'] = '_none'
            upload_data['field_oducaci_n_ciencias_natural[und]'] = '_none'
            upload_data['field_oducaci_n_ciencias_sociale[und]'] = '_none'
            upload_data['field_oeducaci_n_infantil[und]'] = '_none'
            upload_data['field_ongenier_a_qu_mica_y_agron[und]'] = '_none'
            upload_data['field_oasignatura[und]'] = '_none'
            upload_data['field_oipo_de_objeto_de_aprendiz[und]'] = '_none'
            upload_data['additional_settings__active_tab'] = 'edit-path'
            upload_data['_triggering_element_name'] = 'field_odescarga_und_0_upload_button'
            upload_data['_triggering_element_value'] = 'Subir al servidor'
            upload_data['ajax_html_ids[]'] = 'wrapper,header-top,logo,site-slogan,block-search-form,search-block-form,edit-search-block-form--2,edit-actions--2,edit-submit--2,header,main-menu,content-body,main,main-content,highlighted,block-node-recent,page-title,block-system-main,objetos-de-aprendizaje-node-form,edit-title,edit-field-oautor,field-oautor-add-more-wrapper,edit-field-oautor-und-0-value,edit-field-psubido-por,field-psubido-por-add-more-wrapper,edit-field-psubido-por-und-0-value,edit-field-ofacultad,edit-field-ofacultad-und,edit-field-ongenier-a-mec-nica-e-indu,edit-field-ongenier-a-mec-nica-e-indu-und,edit-field-oiencias-econ-micas-y-empr,edit-field-oiencias-econ-micas-y-empr-und,edit-field-oingenier-a-el-ctrica,edit-field-oingenier-a-el-ctrica-und,edit-field-oiencias-naturales-y-exact,edit-field-oiencias-naturales-y-exact-und,edit-field-ociencias-sociales,edit-field-ociencias-sociales-und,edit-field-oconstrucci-n,edit-field-oconstrucci-n-und,edit-field-ocultura-f-sica,edit-field-ocultura-f-sica-und,edit-field-oderecho,edit-field-oderecho-und,edit-field-oducaci-n-ciencias-natural,edit-field-oducaci-n-ciencias-natural-und,edit-field-oducaci-n-ciencias-sociale,edit-field-oducaci-n-ciencias-sociale-und,edit-field-oeducaci-n-infantil,edit-field-oeducaci-n-infantil-und,edit-field-ongenier-a-qu-mica-y-agron,edit-field-ongenier-a-qu-mica-y-agron-und,edit-field-oasignatura,edit-field-oasignatura-und,edit-field-oasignatura-und-autocomplete,edit-field-oasignatura-und-autocomplete-aria-live,edit-field-oipo-de-objeto-de-aprendiz,edit-field-oipo-de-objeto-de-aprendiz-und,edit-field-oimagen,edit-field-oimagen-und-0-ajax-wrapper,edit-field-oimagen-und-0-upload,edit-field-oimagen-und-0-upload-button,edit-body,body-add-more-wrapper,edit-body-und-0-summary,cke_edit-body-und-0-summary,cke_edit-body-und-0-summary_arialbl,cke_1_top,cke_13,cke_1_toolbox,cke_15,cke_16,cke_16_label,cke_17,cke_18,cke_18_label,cke_19,cke_19_label,cke_20,cke_20_label,cke_21,cke_21_label,cke_22,cke_22_label,cke_23,cke_23_label,cke_24,cke_25,cke_25_label,cke_26,cke_26_label,cke_27,cke_27_label,cke_28,cke_28_label,cke_29,cke_29_label,cke_30,cke_31,cke_31_label,cke_32,cke_32_label,cke_33,cke_33_label,cke_34,cke_34_label,cke_35,cke_35_label,cke_36,cke_36_label,cke_37,cke_38,cke_38_label,cke_39,cke_39_label,cke_40,cke_14,cke_14_label,cke_14_text,cke_41,cke_42,cke_42_label,cke_43,cke_43_label,cke_44,cke_44_label,cke_45,cke_45_label,cke_46,cke_46_label,cke_47,cke_47_label,cke_48,cke_48_label,cke_49,cke_50,cke_50_label,cke_51,cke_51_label,cke_52,cke_52_label,cke_53,cke_53_label,cke_54,cke_54_label,cke_55,cke_56,cke_56_label,cke_57,cke_57_label,cke_58,cke_58_label,cke_59,cke_59_label,cke_60,cke_60_label,cke_61,cke_61_label,cke_62,cke_63,cke_63_label,cke_64,cke_64_label,cke_65,cke_65_label,cke_1_contents,cke_71,cke_1_bottom,cke_1_resizer,cke_1_path_label,cke_1_path,edit-body-und-0-value,cke_edit-body-und-0-value,cke_edit-body-und-0-value_arialbl,cke_2_top,cke_76,cke_2_toolbox,cke_78,cke_79,cke_79_label,cke_80,cke_81,cke_81_label,cke_82,cke_82_label,cke_83,cke_83_label,cke_84,cke_84_label,cke_85,cke_85_label,cke_86,cke_86_label,cke_87,cke_88,cke_88_label,cke_89,cke_89_label,cke_90,cke_90_label,cke_91,cke_91_label,cke_92,cke_92_label,cke_93,cke_94,cke_94_label,cke_95,cke_95_label,cke_96,cke_96_label,cke_97,cke_97_label,cke_98,cke_98_label,cke_99,cke_99_label,cke_100,cke_101,cke_101_label,cke_102,cke_102_label,cke_103,cke_77,cke_77_label,cke_77_text,cke_104,cke_105,cke_105_label,cke_106,cke_106_label,cke_107,cke_107_label,cke_108,cke_108_label,cke_109,cke_109_label,cke_110,cke_110_label,cke_111,cke_111_label,cke_112,cke_113,cke_113_label,cke_114,cke_114_label,cke_115,cke_115_label,cke_116,cke_116_label,cke_117,cke_117_label,cke_118,cke_119,cke_119_label,cke_120,cke_120_label,cke_121,cke_121_label,cke_122,cke_122_label,cke_123,cke_123_label,cke_124,cke_124_label,cke_125,cke_126,cke_126_label,cke_127,cke_127_label,cke_128,cke_128_label,cke_2_contents,cke_133,cke_2_bottom,cke_2_resizer,cke_2_path_label,cke_2_path,switch_edit-body-und-0-value,edit-body-und-0-format,edit-body-und-0-format-help,edit-body-und-0-format--2,edit-body-und-0-format-guidelines,edit-field-plicencia,edit-field-plicencia-und,edit-field-pcreative-commons,edit-field-pcreative-commons-und,edit-field-pcc-by,edit-field-pcc-by-und-0-ajax-wrapper,edit-field-pcc-by-und-0-upload,edit-field-pcc-by-und-0-upload-button,edit-field-pcc-by-sa,edit-field-pcc-by-sa-und-0-ajax-wrapper,edit-field-pcc-by-sa-und-0-upload,edit-field-pcc-by-sa-und-0-upload-button,edit-field-pcc-by-nd,edit-field-pcc-by-nd-und-0-ajax-wrapper,edit-field-pcc-by-nd-und-0-upload,edit-field-pcc-by-nd-und-0-upload-button,edit-field-pcc-by-nc,edit-field-pcc-by-nc-und-0-ajax-wrapper,edit-field-pcc-by-nc-und-0-upload,edit-field-pcc-by-nc-und-0-upload-button,edit-field-pcc-by-nc-sa,edit-field-pcc-by-nc-sa-und-0-ajax-wrapper,edit-field-pcc-by-nc-sa-und-0-upload,edit-field-pcc-by-nc-sa-und-0-upload-button,edit-field-pcc-by-nc-nd,edit-field-pcc-by-nc-nd-und-0-ajax-wrapper,edit-field-pcc-by-nc-nd-und-0-upload,edit-field-pcc-by-nc-nd-und-0-upload-button,edit-field-pgnu-gpl,edit-field-pgnu-gpl-und,edit-field-pgpl-v1,edit-field-pgpl-v1-und-0-ajax-wrapper,edit-field-pgpl-v1-und-0-upload,edit-field-pgpl-v1-und-0-upload-button,edit-field-pgpl-v2,edit-field-pgpl-v2-und-0-ajax-wrapper,edit-field-pgpl-v2-und-0-upload,edit-field-pgpl-v2-und-0-upload-button,edit-field-pgpl-v3,edit-field-pgpl-v3-und-0-ajax-wrapper,edit-field-pgpl-v3-und-0-upload,edit-field-pgpl-v3-und-0-upload-button,edit-field-odescarga,edit-field-odescarga-und-0-ajax-wrapper,edit-field-odescarga-und-0-upload,edit-field-odescarga-und-0-upload-button,edit-field-pgfdl,edit-field-pgfdl-und-0-ajax-wrapper,edit-field-pgfdl-und-0-upload,edit-field-pgfdl-und-0-upload-button,active-vertical-tab,edit-path,edit-path-alias,edit-actions,edit-submit,edit-preview,sidebar-first,block-system-user-menu,block-menu-menu-men-docente,block-menu-menu-menuselect,block-menu-menu-enlaces,block-tagadelic-taxonomy-tagadelic-taxonomy,block-views-slickslideshow-block,block-my-visitors-my-visitors-block,footer,block-system-powered-by,autologout-cache-check,autologout-cache-check-bit,topcontrol'
            upload_data['ajax_page_state[theme]'] = 'touch'
            upload_data['ajax_page_state[theme_token]'] = ''
            upload_data['files[field_odescarga_und_0]'] = of
            
            upurl = f'https://repotematico.uo.edu.cu/file/ajax/field_odescarga/und/0/' + upload_data['form_build_id']
            resp = await session.post(upurl,data=upload_data)
            jsonparse = loads(str(await resp.text()).replace('<textarea>','').replace('</textarea>',''))
            #print(jsonparse)
            datasoup =  BeautifulSoup(jsonparse[-1]['data'],'html.parser')
            url = datasoup.find('a')['href']
            return url
                	
def uploadfile_progres(chunk,filesize,start,filename,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	msg = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
	msg+= f"▶️ 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(chunk)} of {sizeof_fmt(filesize)} ({sizeof_fmt(mbs)}/s)\n\n"
	global seg
	#if int(localtime().tm_sec) % 2 == 0 :
	if seg != localtime().tm_sec:
		try:
			message.edit(msg,reply_markup=message.reply_markup)
		except:
			pass
	seg = localtime().tm_sec

@bot.on_callback_query()
async def callback(cli: Client, callback: CallbackQuery):
	username = callback.from_user.username
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)
class MoodleClient:
	def __init__(self,username,password,moodle,proxy):
		self.url = moodle
		self.username = username
		self.password = password
		self.session = aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True),connector=proxy)
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"}
		
	async def uploadtoken(self,f,progress,token):
		#print(token)
		url = self.url+"/webservice/upload.php"
		file = Progress(f,progress)
		query = {"token":token,"file":file}
		async with self.session.post(url,data=query,headers=self.headers,ssl=False) as response:
			text = await response.text()
		dat = loads(text)[0]
		url = self.url+"/draftfile.php/"+str(dat["contextid"])+"/user/draft/"+str(dat["itemid"])+"/"+str(quote(dat["filename"]))
		urlw = self.url+"/webservice/rest/server.php?moodlewsrestformat=json"
		query = {"formdata":f"name=Event&eventtype=user&timestart[day]=31&timestart[month]=9&timestart[year]=3786&timestart[hour]=00&timestart[minute]=00&description[text]={quote_plus(url)}&description[format]=1&description[itemid]={randint(100000000,999999999)}&location=&duration=0&repeat=0&id=0&userid={dat['userid']}&visible=1&instance=1&_qf__core_calendar_local_event_forms_create=1","moodlewssettingfilter":"true","moodlewssettingfileurl":"true","wsfunction":"core_calendar_submit_create_update_form","wstoken":token}
		async with self.session.post(urlw,data=query,headers=self.headers) as response:
			text = await response.text()
		try:
			return findall("https?://[^\s\<\>]+[a-zA-z0-9]",loads(text)["event"]["description"])[-1].replace("pluginfile.php/","webservice/pluginfile.php/")+"?token="+token
			print('Correcto')
		except:
			return url
			print('Error')			
def iprox(proxy):
    tr = str.maketrans(
        "@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ZYXWVUTSRQPONMLKJIHGFEDCBAzyIwvutsrqponmlkjihgf3dcba9876543210|-_;,:&%$#=/.@",
    )
    return str.translate(proxy[::2], tr) 
def files_formatter(path,username):
	filespath = Path(str(path))
	result = []
	for p in filespath.rglob("*"):
		if p.is_file():
			result.append(str(Path(p).name))
	stat = shutil.disk_usage(filespath)
	usado = sizeof_fmt(stat[1])
	total = sizeof_fmt(stat[0])
	result.sort()
	msg = '**Archivos**\n'
	msg +='**Eliminar todo:** /deleteall\n\n'
	if result == []:
		return msg
	i = 0
	for n in result:
		size = Path(str(path)+"/"+n).stat().st_size
		msg+=f"**{i}** `{n}`  **[ {sizeof_fmt(size)} ]**\n**/upload{i} | /rm{i}**\n\n"
		i+=1
	return msg

#mediafiredl
async def extractDownloadLink(contents):
    for line in contents.splitlines():
        m = re.search(r'href="((http|https)://download[^"]+)', line)
        if m:
            return m.groups()[0]
async def download_mediafire(url, path, msg, callback=None):
	session = aiohttp.ClientSession()
	response = await session.get(url)
	url = await extractDownloadLink(await response.text())
	response = await session.get(url)
	filename = response.content_disposition.filename
	f = open(path+"/"+filename, "wb")
	chunk_ = 0
	total = int(response.headers.get("Content-Length"))
	start = time()
	while True:
		chunk = await response.content.read(1024)
		if not chunk:
			break
		chunk_+=len(chunk)
		if callback:
			await callback(chunk_,total,filename,start,msg)
		f.write(chunk)
		f.flush()
	return path+"/"+filename

#tools
def sevenzip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size

    if not volume:
        volume = fsize + 1024

    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3

    with MultiVolume(
        fpath.with_name(fpath.name+".7z"), mode="wb", volume=volume, ext_digits=ext_digits
    ) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)

            archive_writer.write(fpath, fpath.name)

    files = []
    for file in archive._files:
        files.append(file.name)
    unlink(fpath)
    return files
   
def filezip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size

    if not volume:
        volume = fsize + 1024

    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3

    with MultiVolume(
        fpath.with_name(fpath.name+"zip"), mode="wb", volume=volume, ext_digits=0) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)

            archive_writer.write(fpath, fpath.name)

    files = []
    for file in archive._files:
        files.append(file.name)
    unlink(fpath)
    return files
class Progress(BufferedReader):
    def __init__(self, filename, read_callback):
        f = open(filename, "rb")
        self.filename = Path(filename).name
        self.__read_callback = read_callback
        super().__init__(raw=f)
        self.start = time()
        self.length = Path(filename).stat().st_size

    def read(self, size=None):
        calc_sz = size
        if not calc_sz:
            calc_sz = self.length - self.tell()
        self.__read_callback(self.tell(), self.length,self.start,self.filename)
        return super(Progress, self).read(size)

def update(username):
    Configs[username] = {"z": 900,"m":"e","a":"a"}

async def get_messages():
	msg = await bot.get_messages(Channel_Id,message_ids=9)
	Configs.update(loads(msg.text))

async def send_config():
	try:
		await bot.edit_message_text(Channel_Id,message_id=9,text=dumps(Configs,indent=4))
	except Exception as x:
		print(x)
		pass


bot.start()
bot.loop.run_forever()
