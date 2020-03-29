import simplejson as json
import os
import random
import math
from termcolor import colored, cprint

class DataLoader:
    data = None
    def openData(self, path):
        raise NotImplementedError
    def getData(self):
        raise NotImplementedError


class JsonLoader(DataLoader):
    def openData(self, path):
        if os.path.isfile(path) and os.stat(path).st_size != 0:
            self.data = open(path)
        return self
    def getData(self):
        if self.data:
            return json.loads(self.data.read())
        else:
            return None
        

class Config:
    def __init__(self, configPath: str, dataLoader: DataLoader):
        self.configPath = configPath
        self.dataLoader = dataLoader
    
    def loadConfigs(self):
        self.spellsList = self.dataLoader.openData(self.configPath + "spells.json").getData()
        self.itemsList = self.dataLoader.openData(self.configPath + "items.json").getData()
        self.playersList = self.dataLoader.openData(self.configPath + "players.json").getData()
        self.enemiesList = self.dataLoader.openData(self.configPath + "enemies.json").getData()
    
    
    def getSpells(self):
        return self.spellsList

    def getItems(self):
        return self.itemsList

    def getPlayers(self):
        return self.playersList

    def getEnemies(self):
        return self.enemiesList

class RandomGeneratorInterface:
    def generate(self, value, minPercent, maxPercent):
        raise NotImplementedError

class RandomValuesGenerator(RandomGeneratorInterface):
    def generate(self, value, minPercent = 0.95, maxPercent = 1.05):
        minValue = round(value * minPercent)
        maxValue = round(value * maxPercent)
        return random.randint(minValue, maxValue)

class MessageGeneratorInterface:
    def attack(self, attacker, target, value):
        raise NotImplementedError
    
    def heal(self, healed, value):
        raise NotImplementedError

    def castSpell(self, caster, spell):
        raise NotImplementedError

    def notEnoughMp(self, caster):
        raise NotImplementedError

    def useItem(self, user, item):
        raise NotImplementedError

    def died(self, character):
        raise NotImplementedError
    
    def headline(self, message):
        raise NotImplementedError

    def menuElement(self, index, message):
        raise NotImplementedError

    def statElement(self, hpTopBar, mpTopBar, hpBar, mpBar, hp, mp):
        raise NotImplementedError
    
    def usedElixer(self):
        raise NotImplementedError
    
    def playerTurn(self):
        raise NotImplementedError

    def enemyTurn(self):
        raise NotImplementedError

    def characterAttributes(self, attrName, attrValue):
        raise NotImplementedError

    def players(self):
        raise NotImplementedError    

    def enemies(self):
        raise NotImplementedError    

class MessageGenerator(MessageGeneratorInterface):
    def attack(self, attacker, target, value):
        cprint(attacker.getName() + " attacks " + target.getName() + " for " + str(value) + ".", "red")
    
    def heal(self, healed, value):
        cprint(healed.getName() + " has been healed for " + str(value) + ".", "green")

    def castSpell(self, caster, spell):
        cprint(caster.getName() + " casts " + spell.getName() + "!", "blue")

    def notEnoughMp(self, caster):
        cprint(caster.getName() + " does not have enough MP", "blue")

    def useItem(self, user, item):
        cprint(user.getName() + " uses " + item.getName() + "!", "yellow")

    def died(self, character):
        cprint(character.getName() + " has been killed.", "red", attrs=['bold'])
    
    def headline(self, message):
        cprint(message, "white", attrs=['bold'])
    
    def menuElement(self, index, message):
        print("\t" + str(index) + ". " + message)
    
    def statElement(self, name, hpTopBar, mpTopBar, hpBar, mpBar, hp, mp):
        cprint("                            " + hpTopBar, "red", attrs=['bold'], end="              ")
        cprint(mpTopBar, "blue", attrs=['bold'])
        cprint(name, "white", attrs=['bold'], end="")
        cprint(hp + " |" + hpBar + "|", "red", attrs=['bold'], end="  ")
        cprint(mp + "  |" + mpBar + "|", "blue", attrs=['bold'])

    def usedElixer(self, user):
        cprint(user.getName() + "'s HP and MP have been restored!", "cyan")
    
    def playerTurn(self):
        cprint("\nPlayer turn.", "green", attrs=['bold'])

    def enemyTurn(self):
        cprint("\nEnemy turn.", "red", attrs=['bold'])
    
    def characterAttributes(self, attrName, attrValue):
        cprint(attrName + ":", attrs=['bold'], end=' ')
        cprint(str(attrValue), end=', ')
    
    def players(self):
        cprint("\nPlayers:", "green", attrs=['bold'])
    
    def enemies(self):
        cprint("\nEnemies:", "red", attrs=['bold'])

class CompatiblityMessageGenerator(MessageGeneratorInterface):
    def attack(self, attacker, target, value):
        print(attacker.getName() + " attacks " + target.getName() + " for " + str(value) + ".")
    
    def heal(self, healed, value):
        print(healed.getName() + " has been healed for " + str(value) + ".")

    def castSpell(self, caster, spell):
        print(caster.getName() + " casts " + spell.getName() + "!")

    def notEnoughMp(self, caster):
        print(caster.getName() + " does not have enough MP")

    def useItem(self, user, item):
        print(user.getName() + " uses " + item.getName() + "!")

    def died(self, character):
        print(character.getName() + " has been killed.")
    
    def headline(self, message):
        print(message)
    
    def menuElement(self, index, message):
        print("\t" + str(index) + ". " + message)
    
    def statElement(self, name, hpTopBar, mpTopBar, hpBar, mpBar, hp, mp):
        print("                            " + hpTopBar, end="              ")
        print(mpTopBar)
        print(name, end="")
        print(hp + " |" + hpBar + "|", end="  ")
        print(mp + "  |" + mpBar + "|")

    def usedElixer(self, user):
        print(user.getName() + "'s HP and MP have been restored!")
    
    def playerTurn(self):
        print("\nPlayer turn.")

    def enemyTurn(self):
        print("\nEnemy turn.")
    
    def characterAttributes(self, attrName, attrValue):
        print(attrName + ":", end=' ')
        print(str(attrValue), end=', ')
    
    def players(self):
        print("\nPlayers:")
    
    def enemies(self):
        print("\nEnemies:")

class MenuInterface:
    def __init__(self, message):
        raise NotImplementedError

    def display(self, name, elements):
        raise NotImplementedError

    def getChoice(self, name, elements):
        raise NotImplementedError

class Menu(MenuInterface):
    def __init__(self, message):
        self.message = message
    
    def display(self, name, elements):
        i = 1
        self.message.headline(name)
        for element in elements:
            self.message.menuElement(i, element)
            i += 1
    
    def getChoice(self, elements, toPrompt):
        correct = False
        while not correct:
            choice = int(input(toPrompt + ": ")) - 1
            
            if choice >= 0 and choice < len(elements):
                correct = True
            else:
                print("There is no option: " + str(choice))
        
        return choice

class Statistics():
    def __init__(self, message):
        self.message = message

    def generateStat(self, character):
        hpTicks = math.ceil((character.getHp() / character.getMaxHp()) * 100 / 4)
        mpTicks = math.ceil((character.getMp() / character.getMaxMp()) * 100 / 5)

        hpTopBar = ""
        mpTopBar = ""
        hpBar = ""
        mpBar = ""

        hpString = str(character.getHp()) + "/" + str(character.getMaxHp())
        mpString = str(character.getMp()) + "/" + str(character.getMaxMp())

        while hpTicks > 0:
            hpBar += "█"
            hpTopBar += "_"
            hpTicks -= 1
        while len(hpBar) < 25:
            hpBar += " "
            hpTopBar += "_"

        while mpTicks > 0:
            mpBar += "█"
            mpTopBar += "_"
            mpTicks -= 1
        while len(mpBar) < 20:
            mpBar += " "
            mpTopBar += "_"

        name = character.getName()

        if len(name) < 16:
            decreased = 16 - len(name)
            while decreased > 0:
                name += " "
                decreased -= 1

        currentHp = ""
        if len(hpString) < 10:
            decreased = 10 - len(hpString)
            while decreased > 0:
                currentHp += " "
                decreased -= 1
        
        currentHp += hpString

        currentMp = ""
        if len(mpString) < 10:
            decreased = 10 - len(mpString)
            while decreased > 0:
                currentMp += " "
                decreased -= 1
        
        currentMp += mpString

        self.message.statElement(name, hpTopBar, mpTopBar, hpBar, mpBar, currentHp, currentMp)
    
    def getStats(self, players, enemies):
        for player in players:
            self.generateStat(player)
        for enemy in enemies:
            self.generateStat(enemy)
    
    def getAttrs(self, party):
        for member in party:
            print(member.getName() + ":")
            self.message.characterAttributes("Normal attack", member.getAtk())
            self.message.characterAttributes("Defense", member.getDf())
            print("\n")
        

class Actions:
    def __init__(self, message: MessageGeneratorInterface):
        self.message = message
    
    def attack(self, attacker, target, value):
        minValue = round(value * 0.95)
        maxValue = round(value * 1.05)

        value = random.randint(minValue, maxValue)

        self.message.attack(attacker, target, value)
        target.setHp(target.getHp() - value)
    
    def heal(self, healed, value):
        self.message.heal(healed, value)
        healed.setHp(healed.getHp() + value)

    def elixer(self, user):
        user.setHp(user.getMaxHp()).setMp(user.getMaxMp())
        self.message.usedElixer(user)
    
    def castSpell(self, caster, spell, isPlayer = False):
        if spell.castSpell(caster):
            if isPlayer:
                self.message.castSpell(caster, spell)
            return True
        else:
            self.message.notEnoughMp(caster)
            return False
    
    def useItem(self, user, item, i, isPlayer = False):
        if item.use():
            self.message.useItem(user, item.getItem())
            user.setItemsQuantity(i, user.getItemsQuantity(i) - 1)
            return True
        else:
            return False

class CheckAlive:
    @staticmethod
    def getAlive(party):
        alive = []
        for member in party:
            if member.getHp() > 0:
                alive.append(member)
        return alive
    
    @staticmethod
    def getDead(dead, party, messanger):
        for member in party:
            if member.getHp() == 0:
                messanger.died(member)
                dead.append(member)
        return dead
        

class SelectMessage:
    @staticmethod
    def get():
        print("Do you want:")
        print("1. Colours")
        print("2. Without colours (compatibility option)")
        choice = int(input("Type option:"))
        return choice

