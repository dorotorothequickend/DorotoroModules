# ---------------------------------------------------------------------------------
# Name: RandomJumoreska
# Description: No description
# Author: Dorotoro
# Commands:
# / / / .rndmjumoreska / / /
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
# meta developer: @DorotoroMods

from .. import loader, utils
import random
from random import choice


anekdoti = ["— Как называется древнейшее государство геев?\n — Глиномесопотамия", "Первые признаки СПИДа:\n 1) Резкая боль в заднем проходе.\n 2) Тяжелое дыхание в затылок.", "Два еврея сидят в туалете. Один говорит:\n — Скажи Мойша. Вот мы сейчас какаем. Это умственная или физическая работа?\n — Я думаю умственная. Если бы это была физическая работа, мы таки кого-нибудь наняли.", "В Тольятти началось и очень быстро заглохло восстание машин.", "— Что сделал каннибал торч?\n — Покурил мальца", "Почему Кеннеди не пьёт?\n Его выносит с первого шота.", "Маленький одноногий мальчик встал не с той ноги и упал.", "-Знаете почему у маленького слепого мальчика упало мороженое?\n -Почему?\n -Его сбила фура.", "Учительница с зарплатой 4.000₽ плачет когда пишет на доске 'классная работа'", "Лесник-мошенник развёл костёр", "До электрических скатов были скаты внутреннего сгорания.", "В садике, после прививки, дети не выбрасывают ватку, потому что от неё пахнет папой.", "Пошли мужики в сауну париться. Парились-парились да спарились!", "В советские годы секс был не главным. Главным был Сталин.", "Вокзальная проститутка вышла замуж за бас гитариста и скатилась до его уровня.", "Российские программисты массово ушли на front end. (писав этот модуль я сам посмеялся)", "В Эстонии полностью расхищен алмазный фонд: пропали все три стеклореза.", "Карлик устроил пьяную драку в мини-баре.", "Приезжаешь в Ереван, а там русские в шашки играют", "— Что такое минет по-кавказски?\n — Как и обычный, только с аджикой.", "Собрались как-то все гендеры и беременная женщина подраться. Все честно: двое на двое", "— От винта, пидорасы! — кричал Карлсон, отгоняя пидорасов от винта.", "Цыганская сборная привезла с Олимпиады всё золото", "Один мальчик выпил пива перед итоговым сочинением и пришел на него готовым", "В семье химикатов случилось горе. Отца нейтрализовали.", "Три мужика рассказывают у кого жена тупее.\n — Моя дура - купила наушники. А плеера-то у неё нет!\n Все ржут.\n — Моя ещё тупее - купила принтер. А компьютера-то у неё нет!\n Все хохочут.\n — Эт всё хуйня, вот моя презервативов набрала и на море укатила!\n Все молчат.\n — А члена-то у неё нет!", "'Не лает, не кусает, в дом не пускает.' - приговаривал мужик, подпирая дверь мёртвой собакой.", "По судьбе Райана Гослинга в роли медведя в концовке фильма 'Лесной Драйв' вопрос не стоит", "мышь, задумавшая что-то злое, называется злоумышьленник)", "Каждый раз, когда Буратино кидал палку Мальвине, Артемон ее возвращал", "Когда на границе у вас спрашивают когда вы купили билет, главное не переспросить 'Какой из?'", "Каждый раз, когда Буратино кидал палку Мальвине, Артемон ее возвращал", "У нас на работе есть девушка: по гороскопу она весы, а по весам – телец.", "Воспитательница детского сада с десятилетним стажем набила себе на руке три татушки три та та.", "— Что такое причастие? — спрашивает ребёнок священника.\n Батюшка пытается объяснить о Причастии все что знает и простыми словами. После его объяснения ребенок долго выглядит очень задумчивым, а потом выдаёт:\n — А что же тогда деепричастие?", "Штирлиц порол чушь. Чушь отчаянно визжала", "Армянин, открыв дверцы шкафа, нашел вход в Нардию.", "— Капитан! Земля!\n — Мы ещё не отплыли, долбоёб", "В Ираке прошёл турнир по КсГо. Террористы выиграли.", "Заходит как-то в бар феменистка. А нет, не заходит А хули вы хотели? 46 тонн!", "Мальчик, который умеет читать мысли, проиграл в покер девочке которая не умеет думать.", "Приходит Гуччио Гуччи в итальянский дом моды, а там Армани в нарды играет", "Продается: Французское ружье времен Второй мировой. Ни разу не стреляло. Один раз уронили.", "На диване лежал пьяный Петрович, и в нем боролись два человека: один хотел спать, другой срать. Пoбeдили oбa.", "Heмой аквалангист Василий прочел пo гyбaм бeлoй акулы, что ему пиздец", "Рэпер FACE поехал в гастрольный тур по США под псевдонимом ЕБАЛО.", "епер с диареей зачитал дристайл", "Идёт медведь по арктическому кругу. Видит — машину снегом занесло. Сел в неё и замёрз.", "Грузин - порноактёр назвал своего сына Камшот.", "Страсть к закладкам осталась в Питере со времён закладки города", "Мисс таиланд на хую вертела все обвинения в свой адрес.", "Привозят карлика в больницу, а у него микро инсульт", "Таджикские ученые запустили в космос шептуна.", "Врачи-хипстеры сидят в неординаторской.", "Если часы с кукушкой перевернуть лицом к стене получатся часы с дятлом.", "Гестапо обложило все выходы... Но Штирлиц вышел через вход", "Дважды был женат, и оба раза неудачно. Первая жена ушла, а вторая - нет.", "— О, мадам! У вас безупречный вкус.\n — Мужчина, перестаньте меня лизать!", "На Камчатке последнюю парту называют Калининградом.", "Изобрел Попов радио, включил — а слушать-то нечего!", "Принесли Гена и Чебурашка домой ящик пива. Чебурашка случайно разбил одну бутылку. Гена это увидел, схватил весь ящик, ебанул об стену и заорал: 'Вот и попили, блять, пивка!'", "На выборах в Национальное Собрание Армении большинство мест получила партия в нарды.", "Недавно прошел чемпионат мира по логике. Победил победитель, подарили подарок.", "— Штирлиц, говорят, что Вы 'голубой', - сказал Мюллер.\n — Я? - покраснел Штирлиц. - А теперь?", "— Милый, я ушла! Суп в холодильнике, картофель в мундире, игла в яйце, земля в иллюминаторе", "Отдам кота. Приучен к горшку. А также к Цою и к сектору газа.", "Сегодня в Москве перевернулся грузовик, перевозивший Виагру. Кольцевая до сих пор стоит.", "Тренер камикадзе:\n — Смотри, показываю 1 раз", "Сталкер почуял за собой хвост.\n «Мутирую», – подумал сталкер.", "Тайские учёные разработали очко", "Почему слепым так нравится выгуливать собак?", "Штирлиц направился на передовую и увидел замерзающих солдат. 'Атака стыла' - догадался Штирлиц", "Мальчик с ловкими ягодицами отбирает у отца ремень во время порки.", "Приходят два похуиста в музыкальный магазин и говорят: 'Нам по барабану.'", "Штрилиц шёл, с трудом разбирая дорогу. На утро Гитлеру было доложено, что ночью разобрали 13 км железнодорожных путей.", "У физика-твердотельщика случился понос и он стал гидродинамиком", "Педофил-каннибал, вот вроде взрослый человек, а внутри ребёнок.", "Находчивый отец, чтобы узнать, матерится ли его сын, ударил его по пальцам молотком.", "Барабанщик группы 'Бутырка' долго не соглашался сидеть и стучать.", "Британскими учёными был проведён эксперимент о влиянии музыки на растения. Цветок которому включали классику расцвёл быстрее остальных. У цветка которому включали панк-рок опали все лепестки и умер горшок", "Программисты понимают анекдоты только категории C++", "Колобок повесился, Буратино утонул, негр умер своей смертью."]

@loader.tds
class RandomJumoreska(loader.Module):
    """Отправляет случайную юмореску."""
    strings = {"name": "RandomJumoreska"}

    @loader.command()
    async def rndmjumoreska(self,m):
        "- выдать рандомную юмореску."
        randomjumor = random.choice(anekdoti)
        await utils.answer(m, f"<b>{randomjumor}</b>")
        
