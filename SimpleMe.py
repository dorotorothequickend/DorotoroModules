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
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroSimpleMe.png
# meta developer: @DorotoroMods

from .. import loader, utils

@loader.tds
class SimpleMinecraftMe(loader.Module):
    """Сообщает об исполнителе команды от третьего лица."""
    strings = {
        "name": "SimpleMe",
        "symbol": "Символ который используется в конце и в начале сообщения. (например, звезда)"
        }

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "symbol", None, doc=lambda: self.strings("symbol")
            ),
        )


    @loader.command()
    async def me(self, message):
        "<действие> - сообщает об исполнителе команды от третьего лица. команда /me из игры Minecraft.\n\nПример использования: .me открыл браузер\nТакже есть доп. настройка в .config"
        args = utils.get_args_raw(message)
        me = self.client.hikka_me
        nickname = f'{me.first_name} {me.last_name if me.last_name else ""}'
        cfg = self.config["symbol"]
        if not args:
            await utils.answer(message, "<emoji document_id=6325733670132909953>😰</emoji> <b>Вы неправильно вписали действие или же не указали его вовсе. Попробуйте еще раз.</b>")
        if cfg == None:
            await utils.answer(message, f"<emoji document_id=5785175271011259591>🌀</emoji> <b>{nickname}</b> <i>{args}</i><b>")
        if cfg is not None:
            await utils.answer(message, f"<emoji document_id=5785175271011259591>🌀</emoji> <b>{cfg}{nickname}</b> <i>{args}</i><b>{cfg}</b>")
