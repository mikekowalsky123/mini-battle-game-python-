import random

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
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic']
    
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
    
    def getSpellName(self, i):
        return self.magic[i]["name"]
    
    def getSpellMpCost(self, i):
        return self.magic[i]["cost"]

    def chooseAction(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
    
    def chooseMagic(self):
        print("Magic")
        i = 1
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
    
    
