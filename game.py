from classes.game import DataLoader, JsonLoader, Config, MessageGenerator, CompatiblityMessageGenerator, Menu, Statistics, Actions, CheckAlive, SelectMessage
from classes.character import Character
from classes.magic import Spell
from classes.inventory import Item, ItemManager
import time
import random
from termcolor import colored, cprint


class Game:
    def __init__(self, message, menu):
        self.message = message
        self.menu = menu
    
    def startFight(self):
        fight = True

        print("Loading configuration...")

        dataLoader = JsonLoader()

        config = Config("./config/", dataLoader)
        config.loadConfigs()

        stats = Statistics(self.message)

        actions = Actions(self.message)

        actionElements = ["Attack", "Cast spell",
                          "Use item", "Check characters' statistics"]

        players = []
        enemies = []
        spells = []
        items = []

        for spell in config.getSpells():
            spells.append(
                Spell(spell["name"], spell["cost"], spell["value"], spell["school"]))

        for item in config.getItems():
            items.append(Item(item["name"], item["itemType"],
                              item["description"], item["value"]))

        for player in config.getPlayers():
            players.append(Character(player["name"], player["hp"], player["mp"],
                                     player["atk"], player["df"], player["spells"], player["items"]))

        for enemy in config.getEnemies():
            enemies.append(Character(enemy["name"], enemy["hp"], enemy["mp"],
                                     enemy["atk"], enemy["df"], enemy["spells"], enemy["items"]))

        alivePlayers = players
        aliveEnemies = enemies
        deadPlayers = []
        deadEnemies = []

        # time.sleep(3)

        print("Loading done.")

        # time.sleep(2)

        print("Starting fight!")

        # time.sleep(3)

        while fight:

            self.message.playerTurn()

            for player in alivePlayers:
                stats.getStats(alivePlayers, aliveEnemies)
                print("Current character: " + player.name)
                takenAction = False
                while not takenAction:
                    self.menu.display("Actions", actionElements)
                    actionChoice = self.menu.getChoice(
                        actionElements, "Choose action")
                    attack = False
                    normalAttack = False
                    heal = False
                    elixer = False

                    if actionChoice == 3:
                        self.message.players()
                        stats.getAttrs(alivePlayers)
                        self.message.enemies()
                        stats.getAttrs(aliveEnemies)
                        continue

                    elif actionChoice == 0:
                        value = player.getAtk()
                        attack = True
                        normalAttack = True
                    elif actionChoice == 1:
                        playerSpells = player.getSpells()
                        if not playerSpells:
                            continue

                        spellsName = []
                        for i in playerSpells:
                            spellsName.append(spells[i].getName() + " (value: " + str(spells[i].getValue())
                                              + ", cost: " + str(spells[i].getCost()) + ")")
                        spellsName.append("Back")

                        self.menu.display("Spells", spellsName)
                        spellChoice = self.menu.getChoice(
                            spellsName, "Choose spell")

                        if spellChoice == len(spellsName) - 1:
                            continue

                        chosenSpell = spells[playerSpells[spellChoice]]
                        casted = actions.castSpell(player, chosenSpell, True)

                        if not casted:
                            continue
                        elif casted:
                            value = chosenSpell.getValue()

                        if chosenSpell.getSchool() == "attack":
                            attack = True
                        elif chosenSpell.getSchool() == "white":
                            heal = True
                    elif actionChoice == 2:
                        playerItems = player.getItems()
                        if not playerItems:
                            continue
                        itemsName = []
                        for i in playerItems:
                            id = i["id"]
                            quantity = str(i["quantity"])
                            itemsName.append(items[id].getName()
                                             + " - " + items[id].getDescription() + " (" + quantity + "x)")
                        itemsName.append("Back")

                        self.menu.display("Items", itemsName)
                        itemChoice = self.menu.getChoice(itemsName, "Choose item")

                        if itemChoice == len(itemsName) - 1:
                            continue

                        chosenItem = ItemManager(items[playerItems[itemChoice]["id"]],
                                                 playerItems[itemChoice]["quantity"])

                        used = actions.useItem(
                            player, chosenItem, itemChoice, True)

                        if not used:
                            continue
                        else:
                            value = chosenItem.getItem().getValue()

                        if chosenItem.getItem().getType() == "potion":
                            heal = True
                        elif chosenItem.getItem().getType() == "attack":
                            attack = True
                        elif chosenItem.getItem().getType() == "elixer":
                            elixer = True

                    if attack == True:
                        enemiesName = []
                        for enemy in aliveEnemies:
                            enemiesName.append(enemy.getName())
                        enemiesName.append("Back")

                        self.menu.display("Enemies", enemiesName)
                        enemyChoice = self.menu.getChoice(
                            enemiesName, "Choose enemy")

                        if enemyChoice == len(enemiesName) - 1:
                            continue

                        if normalAttack:
                            defense = round(
                                aliveEnemies[enemyChoice].getDf() / 50)
                            if defense == 0:
                                defense = 1

                            value = round(value / defense)

                        actions.attack(
                            player, aliveEnemies[enemyChoice], value)
                    elif heal == True:
                        actions.heal(player, value)
                    elif elixer == True:
                        actions.elixer(player)

                    takenAction = True

                deadEnemies = CheckAlive.getDead(
                    deadEnemies, aliveEnemies, self.message)
                aliveEnemies = CheckAlive.getAlive(aliveEnemies)

                if not aliveEnemies:
                    print("Won")
                    fight = False
                    break

            self.message.enemyTurn()
            for enemy in aliveEnemies:
                takenAction = False
                while not takenAction:
                    attack = False
                    normalAttack = False
                    heal = False
                    elixer = False
                    actionChoice = random.randint(0, 2)

                    if actionChoice == 0:
                        attack = True
                        normalAttack = True
                    elif actionChoice == 1:
                        enemiesSpells = enemy.getSpells()
                        if not enemiesSpells:
                            continue
                        spellChoice = random.randrange(0, len(enemiesSpells))

                        chosenSpell = spells[enemiesSpells[spellChoice]]

                        if chosenSpell.getSchool() == "white" and enemy.getHp() >= enemy.getMaxHp() * 0.9:
                            continue

                        casted = actions.castSpell(enemy, chosenSpell)

                        if not casted:
                            continue
                        elif casted:
                            value = chosenSpell.getValue()

                        if chosenSpell.getSchool() == "attack":
                            attack = True
                        elif chosenSpell.getSchool() == "white":
                            heal = True
                    elif actionChoice == 2:
                        enemyItems = enemy.getItems()
                        if not enemyItems:
                            continue

                        itemChoice = random.randrange(0, len(enemyItems))

                        chosenItem = ItemManager(items[enemyItems[itemChoice]["id"]],
                                                 enemyItems[itemChoice]["quantity"])

                        if enemy.getHp() >= enemy.getMaxHp() * 0.9:
                            enoughHp = False
                        else:
                            enoughHp = True

                        if enemy.getMp() >= enemy.getMaxMp() * 0.9:
                            enoughMp = False
                        else:
                            enoughMp = True

                        if chosenItem.getItem().getType() == "Potion" and not enoughHp:
                            continue
                        elif chosenItem.getItem().getType() == "Elixer" and (not enoughHp or not enoughMp):
                            continue

                        used = actions.useItem(enemy, chosenItem, itemChoice)

                        if not used:
                            continue
                        else:
                            value = chosenItem.getItem().getValue()

                        if chosenItem.getItem().getType() == "potion":
                            heal = True
                        elif chosenItem.getItem().getType() == "attack":
                            attack = True
                        elif chosenItem.getItem().getType() == "elixer":
                            elixer = True

                    time.sleep(1)
                    if attack == True:
                        target = random.randrange(0, len(alivePlayers))

                        if normalAttack:
                            defense = round(alivePlayers[target].getDf() / 50)
                            if defense == 0:
                                defense = 1

                            value = round(value / defense)

                        actions.attack(enemy, alivePlayers[target], value)
                    elif heal == True:
                        actions.heal(enemy, value)
                    elif elixer == True:
                        actions.elixer(enemy)

                    takenAction = True

                deadPlayers = CheckAlive.getDead(
                    deadPlayers, alivePlayers, self.message)
                alivePlayers = CheckAlive.getAlive(alivePlayers)

                if not alivePlayers:
                    print("Lose")
                    fight = False
                    break
