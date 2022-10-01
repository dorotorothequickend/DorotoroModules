
# ---------------------------------------------------------------------------------
# Name: Dota2RandomHero
# Description: No description
# Author: Dorotoro 
# Commands:
# .dota2randomhero | .dota2randombuild | .dota2randompick
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

import random
import re
from .. import loader, utils

@loader.tds
class Dota2RandomHero(loader.Module):
    strings = {"name": "Dota2RandomHero"}
    prefix = "<b> [/Dota2RandomHero/] </b>\n"

    @loader.command()
    async def dota2randomhero(self, m):
        "- выбирает рандомного героя из Dota 2"
        hero = ['Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunnka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Broodmother', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Mirana', 'Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Phantom Lancer', 'Razor', 'Phantom Assasin', 'Naga Siren', 'Nyx Assasin', 'Pangolier', 'Riki', 'Slark', 'Terrorblade', 'Shadow Fiend', 'Spectre', 'Sniper', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparation', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'KOTL', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Natures', 'Prophet', 'Necrophos', 'Puck', 'Pugna', 'QOP', 'Rubick', 'Skywrath Mage', 'Shadow Shaman', 'Shadow Demon', 'Silencer', 'Tinker', 'Storm Spirit', 'Techies', 'Visage', 'Warlock', 'Void Spirit', 'Windranger', 'Winter Wyvern', 'Zeus', 'Witch Doctor']
        randomhero = random.choice(hero)
        await m.edit(f"<b> {self.prefix} </b>Вам выпал герой: {randomhero}")
    
    @loader.command()
    async def dota2randombuild(self,m):
        "- выбирает рандомный билд на героя из Dota 2."
        build = ['Physical', 'Magic', 'with Aura items', 'Support', "with 6 Divine Rapier's"]
        randombuild = random.choice(build)
        await m.edit(f"<b> {self.prefix} </b>Вам выпала сборка: {randombuild}")
