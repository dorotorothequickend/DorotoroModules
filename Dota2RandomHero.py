# ---------------------------------------------------------------------------------
# Name: Dota2RandomHero
# Description: No description
# Author: Dorotoro 
# Commands:
# .dota2hero | .dota2build | .dota2pick | .dota2hb
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
from .. import loader, utils

hero1 = ['Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunnka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Broodmother', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Mirana', 'Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Phantom Lancer', 'Razor', 'Phantom Assasin', 'Naga Siren', 'Nyx Assasin', 'Pangolier', 'Riki', 'Slark', 'Terrorblade', 'Shadow Fiend', 'Spectre', 'Sniper', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparation', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'KOTL', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Natures', 'Prophet', 'Necrophos', 'Puck', 'Pugna', 'QOP', 'Rubick', 'Skywrath Mage', 'Shadow Shaman', 'Shadow Demon', 'Silencer', 'Tinker', 'Storm Spirit', 'Techies', 'Visage', 'Warlock', 'Void Spirit', 'Windranger', 'Winter Wyvern', 'Zeus', 'Witch Doctor']
hero2 = ['Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunnka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Broodmother', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Mirana', 'Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Phantom Lancer', 'Razor', 'Phantom Assasin', 'Naga Siren', 'Nyx Assasin', 'Pangolier', 'Riki', 'Slark', 'Terrorblade', 'Shadow Fiend', 'Spectre', 'Sniper', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparation', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'KOTL', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Natures', 'Prophet', 'Necrophos', 'Puck', 'Pugna', 'QOP', 'Rubick', 'Skywrath Mage', 'Shadow Shaman', 'Shadow Demon', 'Silencer', 'Tinker', 'Storm Spirit', 'Techies', 'Visage', 'Warlock', 'Void Spirit', 'Windranger', 'Winter Wyvern', 'Zeus', 'Witch Doctor']
hero3 = ['Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunnka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Broodmother', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Mirana', 'Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Phantom Lancer', 'Razor', 'Phantom Assasin', 'Naga Siren', 'Nyx Assasin', 'Pangolier', 'Riki', 'Slark', 'Terrorblade', 'Shadow Fiend', 'Spectre', 'Sniper', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparation', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'KOTL', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Natures', 'Prophet', 'Necrophos', 'Puck', 'Pugna', 'QOP', 'Rubick', 'Skywrath Mage', 'Shadow Shaman', 'Shadow Demon', 'Silencer', 'Tinker', 'Storm Spirit', 'Techies', 'Visage', 'Warlock', 'Void Spirit', 'Windranger', 'Winter Wyvern', 'Zeus', 'Witch Doctor']
hero4 = ['Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunnka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Broodmother', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Mirana', 'Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Phantom Lancer', 'Razor', 'Phantom Assasin', 'Naga Siren', 'Nyx Assasin', 'Pangolier', 'Riki', 'Slark', 'Terrorblade', 'Shadow Fiend', 'Spectre', 'Sniper', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparation', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'KOTL', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Natures', 'Prophet', 'Necrophos', 'Puck', 'Pugna', 'QOP', 'Rubick', 'Skywrath Mage', 'Shadow Shaman', 'Shadow Demon', 'Silencer', 'Tinker', 'Storm Spirit', 'Techies', 'Visage', 'Warlock', 'Void Spirit', 'Windranger', 'Winter Wyvern', 'Zeus', 'Witch Doctor']
hero5 = ['Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunnka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Broodmother', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Mirana', 'Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Phantom Lancer', 'Razor', 'Phantom Assasin', 'Naga Siren', 'Nyx Assasin', 'Pangolier', 'Riki', 'Slark', 'Terrorblade', 'Shadow Fiend', 'Spectre', 'Sniper', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparation', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'KOTL', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Natures', 'Prophet', 'Necrophos', 'Puck', 'Pugna', 'QOP', 'Rubick', 'Skywrath Mage', 'Shadow Shaman', 'Shadow Demon', 'Silencer', 'Tinker', 'Storm Spirit', 'Techies', 'Visage', 'Warlock', 'Void Spirit', 'Windranger', 'Winter Wyvern', 'Zeus', 'Witch Doctor']
randomhero = random.choice(hero1)
build = ['Physical', 'Magic', 'with Aura items', 'Support', "with 6 Divine Rapier's", "with 6 boots", "with 6 Blinks", "without items"]
randombuild = random.choice(build)


@loader.tds
class Dota2RandomHero(loader.Module):
    strings = {"name": "Dota2RandomHero"}

    @loader.command()
    async def dota2hero(self, message):
        "- выбирает рандомного героя из Dota 2"
        await utils.answer(message, f"<b><emoji document_id=5239991179226915011>ℹ</emoji> Вам выпал герой:\n{randomhero}</b>")
    
    @loader.command()
    async def dota2build(self, message):
        "- выбирает рандомный билд на героя из Dota 2."
        await utils.answer(message, f"<b><emoji document_id=5239991179226915011>ℹ</emoji> Вам выпала сборка:\n{randombuild}</b>")

    @loader.command()
    async def dota2pick(self, message):
    	"- рандомный пик героев."
    	randompick = random.choice(hero1)
    	randompick2 = random.choice(hero2)
    	randompick3 = random.choice(hero3)
    	randompick4 = random.choice(hero4)
    	randompick5 = random.choice(hero5)
    	while randompick == randompick2 or randompick == randompick3 or randompick == randompick4 or randompick == randompick5 or randompick2 == randompick3 or randompick2 == randompick4 or randompick2 == randompick5 or randompick3 == randompick4 or randompick3 == randompick5 or randompick4 == randompick5:
    		randompick = random.choice(hero1)
    		randompick2 = random.choice(hero2)
    		randompick3 = random.choice(hero3)
    		randompick4 = random.choice(hero4)
    		randompick5 = random.choice(hero5)
    	await utils.answer(message, f"<b><emoji document_id=5239991179226915011>ℹ</emoji> Вам выпали герои:\n{randompick}\n{randompick2}\n{randompick3}\n{randompick4}\n{randompick5}</b>")   
    
    @loader.command()
    async def dota2hb(self, message):
        "- рандомный герой и рандомный билд."
        await utils.answer(message, f"<b><emoji document_id=5239991179226915011>ℹ</emoji> Вам выпал герой:\n{randomhero}</b> со сборкой <b>{randombuild}</b>")