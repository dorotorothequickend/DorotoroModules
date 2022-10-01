# ---------------------------------------------------------------------------------
#  ,_     _          
#  |\_,-~/          
#  / _  _ |    ,--.  馃寪 This module was loaded through https://t.me/hikkamods_bot
# (  @  @ )   / ,-'  馃攼 Licensed under the CC BY-NC-ND 4.0.
#  \  _T_/-._( (     
#  /         `. \    鈿狅笍 Owner of this bot doesn't take responsibility for any
# |         _  \ |   errors caused by this module or this module being non-working
#  \ \ ,  /      |   and doesn't take ownership of any copyrighted material.
#   || |-_\__   /    
#  ((_/`(____,-'     
# ---------------------------------------------------------------------------------
# Name: GloryTo
# Description: Этот модуль - причина всех военных конфликтов!
# Author: Dorotoro (@km90h)
# Commands:
# .gtr | .gtu | .gtserb | .gtchina | .gtusa | .gtazer | .gttaiwan | .gtlnr | .gtdnr | .gtrusemp | .gtussr
# ---------------------------------------------------------------------------------
#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/km90h
#           Licensed under the Creative Commons CC BY-NC-ND 4.0
#
#                    Full license text can be found at:
#       https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
#
#                           Human-friendly one:
#            https://creativecommons.org/licenses/by-nc-nd/4.0
# meta developer: Dorotoro

import re
from .. import loader, utils

@loader.tds
class GloryTo(loader.Module):
	strings = {"name": "GloryTo"}
	
	@loader.command()
	async def gtr(self, m):
		"- write #GloryToRussia"
		await m.edit("<b> #GloryToRussia 🇷🇺<b>")
	
	@loader.command()
	async def gtu(self, m):
		"- write #GloryToUkraine"
		await m.edit("<b> #GloryToUkraine 🇺🇦 <b>")

	@loader.command()
	async def gtserb(self,m):
		"- write #GloryToSerbia"
		await m.edit("<b> #GloryToSerbia 🇷🇸 <b>")

	@loader.command()
	async def gtchina(self,m):
		"- write #GloryToChina"
		await m.edit("<b> #GloryToChina 🇨🇳 <b>")
	
	@loader.command()
	async def gtusa(self,m):
		"- write #GloryToUSA"
		await m.edit("<b> #GloryToUSA 🇺🇸 <b>")
	
	@loader.command()
	async def gtazer(self,m):
		"- write #GloryToAzerbaijan"
		await m.edit("<b> #GloryToAzerbaijan 🇦🇿 <b>")

	@loader.command()
	async def gtarmenia(self,m):
		"- write #GloryToArmenia"
		await m.edit("<b> #GloryToArmenia <b> 🇦🇲")

	@loader.command()
	async def gttaiwan(self,m):
		"- write #GloryToTaiwan"
		await m.edit("<b> #GloryToTaiwan 🇹🇼 <b>")

	@loader.command()
	async def gtlnr(self,m):
		"- write #GloryToLNR (ONLY FOR TG PREMIUM USERS)"
		await m.edit("<b> #GloryToLNR <emoji document_id=5458587315033087411>🇷🇺</emoji> <b>")

	@loader.command()
	async def gtdnr(self,m):
		"- write #GloryToDNR (ONLY FOR TG PREMIUM USERS)"
		await m.edit("<b> #GloryToDNR <emoji document_id=5456276227490847488>🇷🇺</emoji>")

	@loader.command()
	async def gtrusemp(self,m):
		"- write #GloryToRussianEmpire (ONLY FOR TG PREMIUM USERS)"
		await m.edit("<b> #GloryToRussianEmpire <emoji document_id=5460713001722059680>🇷🇺</emoji> <b>")

	@loader.command()
	async def gtussr(self,m):
		"- write #GloryToUSSR (ONLY FOR TG PREMIUM USERS)"
		await m.edit("<b> #GloryToUSSR <emoji document_id=5460995979937324686>🇷🇺</emoji>")