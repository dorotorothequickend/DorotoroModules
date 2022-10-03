# ---------------------------------------------------------------------------------
# Name: AccountDeleter
# Description: No description
# Author: Dorotoro
# Commands:
# / / / .delacc / / /
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
#             https://www.gnu.org/licenses/agpl-3.0.html
#
#
# Special Thanks: sk1llzmeow, amore, den4iksop - they help me with set profile picture (SOON)
# meta developer: @DorotoroMods

import time
from telethon import functions, types
from .. import loader, utils
from telethon.tl.functions.account import UpdateProfileRequest

@loader.tds
class AccountDeleter(loader.Module):
    strings = {"name": "AccountDeleter"}

    @loader.command()
    async def delacc(self, m):
        "- удаляет ваш аккаунт Telegram. !!!ОПАСНО!!!"
        text = "Удаление аккаунта через..."
        await utils.answer(m, f"{text} <b>10</b> <emoji document_id=5296432770392791386>✈️</emoji>")
        time.sleep(0.5)
        await utils.answer(m, f"{text} <b>6</b> <emoji document_id=5296432770392791386>✈️</emoji>")
        time.sleep(0.7)
        await utils.answer(m, f"{text} <b>3</b> <emoji document_id=5296432770392791386>✈️</emoji>")
        time.sleep(1)
        await utils.answer(m, f"{text} <b>1</b> <emoji document_id=5296432770392791386>✈️</emoji>")
        time.sleep(0.8)
        await self._client(functions.account.UpdateProfileRequest(first_name='Deleted Account', last_name='', about='Аккаунт удалён. Вся информация на https://telegram.org/faq'))
        await utils.answer(m, "<b>Ваш аккаунт полностью удалён. <emoji document_id=6325592348529003273>😦</emoji></b>")