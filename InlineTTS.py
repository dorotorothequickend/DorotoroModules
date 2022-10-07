# ---------------------------------------------------------------------------------
# Name: SileroTTS
# Description: No description
# Author: Dorotoro & code-fixer @Den4ikSuperOstryyPer4ik
# Commands:
# / / / .silerotts / / / .warcraftvoices / / / .silerovoices
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
# 						Copyright 2022 t.me/km90h
#             https://www.gnu.org/licenses/agpl-3.0.html 
#
# meta developer: @DorotoroMods

from .. import loader, utils
from telethon.tl.types import Message
 
@loader.tds 
class InlineTTS(loader.Module): 
	"""Перед началом работы с модулем необходимо решить каптчу в боте @Silero_Voice_Bot, иначе модуль работать не будет. Также пишите имя героя с МАЛЕНЬКОЙ буквы, иначе тоже будет выбивать ошибку. Также (из-за бота) английские символы не поддерживаются."""
	strings = {"name": "InlineTTS"}

	
	@loader.command()
	async def silerotts(self, message: Message):
		"<герой> <ваш текст> - синтезирует текст в голос героев из Warcraft III и обычных говорилок."
		args = utils.get_args_raw(message)
		if not args:
			await utils.answer(message, "<b><emoji document_id=6327716471849878717>😱</emoji> | Чел... я пустоту не озвучиваю.</b>")
			return
		reply = await message.get_reply_message()
		async with self._client.conversation("@silero_voice_bot") as conv:
			await conv.send_message(args) 
			r = await conv.get_response()
		await message.respond(file=r, reply_to=reply.id if reply else None)
		if message.out:
			await message.delete()

	@loader.command()
	async def warcraftvoices(self,m):
		"- всевозможные голоса для синтеза (Герои Warcraft III)"
		await m.edit(" 💬 Warcraft III Voices\n   <code> arthas </code>| <code>  kelthuzad </code>| <code>  anubarak </code> | <code>  thrall </code> | <code>  grunt </code> | <code>  cairne </code> | <code>  rexxar </code> | <code>  uther </code> | <code> jaina </code> | <code>  kael  | <code> garithos </code> | <code>  malev </code> | <code>  naisha </code> | <code> tyrande </code> | <code> furion </code> | <code>  illidan </code> | <code>  ladyvashj </code> | <code>  narrator </code> | <code>  medivh </code> | <code>  villagerm </code> ")

	@loader.command()
	async def silerovoices(self,m):
		"- всевозможные голоса для синтеза (Обычные голоса Silero)"
		await m.edit("👾 Silero Voices:\n <code> aidar </code> | <code> baya </code> | <code> kseniya </code> | <code> xenia </code> | <code> eugene </code>")e>")
