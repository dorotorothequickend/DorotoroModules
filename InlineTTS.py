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
    """Перед началом работы с модулем необходимо решить каптчу в боте @Silero_Voice_Bot, иначе модуль работать не будет. Английские символы не поддерживаются. Советы:\n\nАббревиатуры необходимо писать вот так - ЭСЭСЭСЭР\nУдарение надо ставить вот так - удар+ение"""

    strings = {"name": "InlineTTS"}

    @loader.command()
    async def astts(self, message: Message):
        "<герой> <ваш текст> - синтезирует текст в голос героев из Warcraft III и обычных говорилок."
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(
                message,
                "<b><emoji document_id=6327716471849878717>😱</emoji> | Чел... я пустоту не озвучиваю.</b>",
            )
            return
        reply = await message.get_reply_message()
        async with self._client.conversation("@silero_voice_bot") as conv:
            await conv.send_message(args)
            r = await conv.get_response()
            my_msg = await conv.send_message(args)
        if r.text != "Введите код на фото.":
            await r.delete()
            await my_msg.delete()
        await message.respond(file=r, reply_to=reply.id if reply else None)
        if message.out:
            await message.delete()

    @loader.command()
    async def warcraftv(self, message):
        "- список голосов для синтеза (Герои Warcraft III)"
        await utils.answer(
            message,
            " 💬 Warcraft III Voices:\n\n<code> arthas </code>| <code>  kelthuzad </code>| <code>  anubarak </code> | <code>  thrall </code> | <code>  grunt </code> | <code>  cairne </code> | <code>  rexxar </code> | <code>  uther </code> | <code> jaina </code> | <code>  kael  | <code> garithos </code> | <code>  malev </code> | <code>  naisha </code> | <code> tyrande </code> | <code> furion </code> | <code>  illidan </code> | <code>  ladyvashj </code> | <code>  narrator </code> | <code>  medivh </code> | <code>  villagerm </code> | <code> acolyte </code> | <code> sylvanas </code> | <code> dread_bm </code> | <code> dread_t </code> | <code> illidan_f </code> | <code> mannoroth </code> | <code> muradin </code> | <code> peasant </code> | <code> priest </code> | <code> sorceress </code> | <code> peon </code> | <code> chen </code>",
        )

    @loader.command()
    async def silerov(self, message):
        "- список голосов для синтеза (Обычные голоса Silero)"
        await utils.answer(
            message,
            "👾 Silero Voices:\n\n<code> aidar </code> | <code> baya </code> | <code> kseniya </code> | <code> xenia </code> | <code> eugene </code>",
        )

    @loader.command()
    async def halflifev(self, message):
        "- список голосов для синтеза (голоса Half-Life)"
        await utils.answer(
            message,
            "🔫 Half-Life Voices:\n\n<code> alyx </code> | <code> breen </code> | <code> gman_e2 </code> | <code> father </code> | <code> barney </code> | <code> gman </code> | <code> kleiner </code> | <code> vort_e2 </code> | <code> vort </code>",
        )

    @loader.command()
    async def portalv(self, message):
        "- список голосов для синтеза (голоса Portal 2)"
        await utils.answer(
            message,
            "🔮 Portal 2 Voices:\n\n <code> glados </code> | <code> wheatley </code>",
        )

    @loader.command()
    async def starcraftv(self, message):
        "- список голосов для синтеза (голоса Starcraft)"
        await utils.answer(
            message,
            "🪅 Starcraft Voices:\n\n<code> hanson </code> | <code> kerrigan </code> | <code> stetmann </code> | <code> tosh </code> | <code> hill </code> | <code> raynor </code> | <code> swann </code> | <code> tychus </code> | <code> valerian </code>",
        )

    @loader.command()
    async def stalkerv(self, message):
        "- список голосов для синтеза (голоса STALKER)"
        await utils.answer(message, "🛖 Stalker Voices:\n\n<code>bandit</code>")

    @loader.command()
    async def dotav(self, message):
        "- список голосов для синтеза (Новые голоса Dota 2)"
        await utils.answer(
            message,
            "<emoji document_id=5239991179226915011>ℹ</emoji> Dota 2 Voices:\n\n<code>announcer</code> | <code>antimage</code> | <code>batrider</code> | <code>bloodseeker</code> | <code>bounty</code> | <code>bristle</code> | <code>clockwerk</code> | <code>doom</code> | <code>earth</code> | <code>gyro</code> | <code>huskar</code> | <code>juggernaut</code> | <code>kotl</code> | <code>kunkka</code> | <code>lancer</code> | <code>lina</code> | <code>luna</code> | <code>meepo</code> | <code>mortred</code> | <code>omni</code> | <code>pudge</code> | <code>queen</code> | <code>ranger</code> | <code>riki</code> | <code>shaker</code> | <code>skywrath</code> | <code>sniper</code> | <code>storm</code> | <code>templar</code> | <code>tide</code> | <code>treant</code> | <code>tusk</code> | <code>windranger</code> | <code>witchdoctor</code> | <code>wraith</code>"
        )
    
    @loader.command()
    async def lolv(self, message):
        "- список голосов для синтеза (Новые голоса LOL)"
        await utils.answer(
            message,
            "🏳️‍🌈 LOL Voices:\n\n<code>evelynn</code> | <code>pantheon</code> | <code>yuumi</code>"
        )
