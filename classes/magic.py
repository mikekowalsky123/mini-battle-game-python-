import random
import math

class SpellInterface:
    def __init__(self, name, cost, value, school):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError
    
    def setName(self, name):
        raise NotImplementedError
    
    def getCost(self):
        raise NotImplementedError
    
    def setCost(self, cost):
        raise NotImplementedError
    
    def getValue(self):
        raise NotImplementedError

    def setValue(self, value):
        raise NotImplementedError

    def getSchool(self):
        raise NotImplementedError

    def setSchool(self, school):
        raise NotImplementedError
    
    def castSpell(self, caster):
        raise NotImplementedError

class Spell(SpellInterface):
    def __init__(self, name, cost, value, school):
        self.name = name
        self.cost = cost
        self.value = value
        self.school = school
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        return self
    
    def getCost(self):
        return self.cost
    
    def setCost(self, cost):
        self.cost = cost
        return self
    
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self
    
    def getSchool(self):
        return self.school

    def setSchool(self, school):
        self.school = school
        return self
    
    def castSpell(self, caster):
        if caster.getMp() >= self.getCost():
            actualMp = caster.getMp()
            caster.setMp(actualMp - self.getCost())
            return True
        else:
            return False



