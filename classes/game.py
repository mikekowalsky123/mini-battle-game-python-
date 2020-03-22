import random
import math

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']
    
    def generateDamage(self):
        return random.randrange(self.atkl, self.atkh)

    def generateSpellDamage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def takeDamage(self, dmg):
        self.hp -= dmg
        if(self.hp < 0):
            self.hp = 0
        return self.hp
    
    def getHp(self):
        return self.hp
    
    def getMaxHp(self):
        return self.maxHp
    
    def getMp(self):
        return self.mp
    
    def getMaxMp(self):
        return self.maxMp
    
    def reduceMp(self, cost):
        self.mp -= cost
    
    def heal(self, hp):
        self.hp += hp
        if self.hp > self.maxHp:
            self.hp = self.maxHp
    
    def gainMp(self, mp):
        if self.mp < self.maxMp:
            self.mp += mp
            if self.mp > self.maxMp:
                self.mp = self.maxMp
            return mp
        else:
            return 0

    def chooseAction(self):
        i = 1
        print("\n" + Bcolors.BOLD + "Character:", self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Actions:" + Bcolors.ENDC)

        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1
        

        goodChoice = False
        
        while goodChoice == False:
            choice = int(input(Bcolors.OKBLUE + "Choose action:" + Bcolors.ENDC)) -1
            if choice >= 0 and choice < len(self.actions):
                goodChoice = True
            else:
                print("There is no action like this!")
        
        return choice
    
    def chooseMagic(self):
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "Magic:" + Bcolors.ENDC)
        i = 1
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
        print("Type 0 to back to actions")
        
        goodChoice = False
        
        while goodChoice == False:
            choice = int(input(Bcolors.OKBLUE + "Choose spell:" + Bcolors.ENDC)) -1
            if choice >= -1 and choice < len(self.magic):
                goodChoice = True
            else:
                print("There is no spell like this!")
        
        return choice
    
    def chooseItem(self):
        i = 1
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "Items:" + Bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":", item["item"].descr, "(x" + str(item["quantity"]) + ")")    
            i+=1
        print("Type 0 to back to actions")

        goodChoice = False
        
        while goodChoice == False:
            choice = int(input(Bcolors.OKBLUE + "Choose item:" + Bcolors.ENDC)) -1
            if choice >= -1 and choice < len(self.items):
                if self.items[choice]["quantity"] == 0:
                    print("This character doesn't have any those items")
                else:
                    goodChoice = True
            else:
                print("There is no action like this!")
        
        return choice

    def chooseTarget(self, enemies):
        i = 1
        print("\n" + Bcolors.FAIL + Bcolors.BOLD + "Target:" + Bcolors.ENDC)
        for enemy in enemies:
            print("    " + str(i) + ". " + enemy.name)
            i += 1
        print("Type 0 to back to actions")
        
        goodChoice = False
        
        while goodChoice == False:
            choice = int(input(Bcolors.OKBLUE + "Choose target:" + Bcolors.ENDC)) -1
            if choice >= -1 and choice < len(enemies):
                goodChoice = True
            else:
                print("There is no enemy like this!")
        
        return choice
    
    def getStats(self):
        hpTicks = math.ceil((self.hp / self.maxHp) * 100 / 4)
        mpTicks = math.ceil((self.mp / self.maxMp) * 100 / 5)

        hpTopBar = ""
        mpTopBar = ""
        hpBar = ""
        mpBar = ""

        hpString = str(self.hp) + "/" + str(self.maxHp)
        mpString = str(self.mp) + "/" + str(self.maxMp)

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

        name = self.name
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
        if len(mpString) < 8:
            decreased = 8 - len(mpString)
            while decreased > 0:
                currentMp += " "
                decreased -= 1
        
        currentMp += mpString

        print(Bcolors.BOLD + Bcolors.OKGREEN + "                            " + hpTopBar + "              " + Bcolors.OKBLUE + mpTopBar + Bcolors.ENDC)
        print(name
            + Bcolors.OKGREEN + currentHp + " |" + hpBar + "|  "
            + Bcolors.OKBLUE + currentMp + "  |" + mpBar + "| \n"
            + Bcolors.ENDC)
    
    def getEnemyStats(self):
        hpTicks = math.ceil((self.hp / self.maxHp) * 100 / 2)

        hpTopBar = ""
        hpBar = ""

        hpString = str(self.hp) + "/" + str(self.maxHp)

        while hpTicks > 0:
            hpBar += "█"
            hpTopBar += "_"
            hpTicks -= 1
        while len(hpBar) < 50:
            hpBar += " "
            hpTopBar += "_"

        name = self.name
        if len(name) < 16:
            decreased = 16 - len(name)
            while decreased > 0:
                name += " "
                decreased -= 1

        currentHp = ""
        if len(hpString) < 12:
            decreased = 12 - len(hpString)
            while decreased > 0:
                currentHp += " "
                decreased -= 1
        
        currentHp += hpString

        print(Bcolors.BOLD + Bcolors.FAIL + "                              " + hpTopBar + Bcolors.ENDC)
        print(name
            + Bcolors.FAIL + currentHp + " |" + hpBar + "|  "
            + Bcolors.ENDC)