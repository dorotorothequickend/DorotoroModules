# ---------------------------------------------------------------------------------
# Name: FkinRickRoll
# Description: No description
# Author: Dorotoro
# Commands:
# / / / .rickvid / / / .rickbait
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
from telethon.tl.functions.account import UpdateProfileRequest

@loader.tds
class FuckingRickRoll(loader.Module):
    """Лучший способ зарикроллить собеседника."""
    strings = {"name": "FkinRickRoll"}

    @loader.command()
    async def rickvid(self, message):
        "- стандартный RickRoll."
        photo = await self._client.send_file(message.to_id, "https://siasky.net/AAAszL8plrdwyskshNBDBNBQx7IeQGVajIVq305Xd7w4vg", caption="<b><i>You've been Rickrolled!</i></b>")
        upload = await self._client.upload_file(await client.download_file(photo, bytes))
        await client(UploadProfilePhotoRequest(upload))

    @loader.command()
    async def rickbait(self, message):
        "- отправляет видео с океаном, в конце которого вашего собеседника ждет RickRoll."
        photo = await self._client.send_file(message.to_id, "https://siasky.net/_Al0XoSpEfN-aZlzdzQX2jc92xCKjlVHAC1uvcvDrRg7fw")
        upload = await self._client.upload_file(await client.download_file(photo, bytes))
        await client(UploadProfilePhotoRequest(upload))
