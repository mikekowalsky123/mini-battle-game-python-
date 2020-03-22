from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hiElixer = Item("Hi-Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

playerMagic = [fire, thunder, blizzard, meteor, quake, cure, cura]
playerItems = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 2},
                {"item": superPotion, "quantity": 3}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 2}, {"item": grenade, "quantity": 2}]

player1Items = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 2},
                {"item": superPotion, "quantity": 3}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 2}, {"item": grenade, "quantity": 2}]
player2Items = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 2},
                {"item": superPotion, "quantity": 3}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 2}, {"item": grenade, "quantity": 2}]
player3Items = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 2},
                {"item": superPotion, "quantity": 3}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 2}, {"item": grenade, "quantity": 2}]

#instantiate people
player1 = Person("Valos", 3260, 65, 60, 34, playerMagic, player1Items)
player2 = Person("Nick", 1000, 65, 60, 34, playerMagic, player2Items)
player3 = Person("Robot", 5000, 65, 60, 34, playerMagic, player3Items)

enemy1 = Person("Imp", 1250, 130, 560, 325, [], [])
enemy2 = Person("Badass", 20000, 1000, 400, 100, [], [])
enemy3 = Person("Imp", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

print(len(players))

playersAlive = True
enemiesAlive = True
running = True
i = 0
back = 0


print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    for player in players:
        if back > 0:
            back -=1
            continue
        if player.hp == 0:
            continue
        
        print("==================")
        print(Bcolors.BOLD + Bcolors.OKGREEN + "\nPlayers:" + Bcolors.ENDC)
        print(Bcolors.BOLD + "NAME                        " + Bcolors.OKGREEN + "HP                                     " + Bcolors.OKBLUE + "MP" + Bcolors.ENDC)
        for i in players:
            i.getStats()
        print(Bcolors.BOLD + Bcolors.FAIL + "\nEnemies:" + Bcolors.ENDC)
        for i in enemies:
            i.getEnemyStats()
        
        index = player.chooseAction()
        
        if index == 0:
            dmg = player.generateDamage()
            target = player.chooseTarget(enemies)
            if target == -1:
                back = len(players) + len(enemies) - 1
                continue
            enemies[target].takeDamage(dmg)
            print(player.name, "attacked", enemies[target].name, "for", dmg, "points of damage.")

            if enemies[target].hp == 0:
                del enemies[target]
        elif index == 1:
            magicChoice = player.chooseMagic()
            if magicChoice == -1:
                back = len(players) + len(enemies) - 1
                continue

            spell = player.magic[magicChoice]
            magicHp = spell.generateDamage()
            cost = spell.cost

            currentMp = player.getMp()

            if cost > currentMp:
                print(Bcolors.FAIL + "\nNot enough MP!", player.name, "has only", str(player.getMp()) + "\\" + str(player.getMaxMp()) + "\n" + Bcolors.ENDC)
                continue
            
            player.reduceMp(cost)

            if spell.type == "white":
                player.heal(magicHp)
                print(Bcolors.OKBLUE + "\n" + player.name + " casts " + spell.name + " and heals", player.name, "for", str(magicHp), "health points." + Bcolors.ENDC)
            elif spell.type == "black":
                target = player.chooseTarget(enemies)
                if target == -1:
                    back = len(players) + len(enemies) - 1
                    continue
                enemies[target].takeDamage(magicHp)
                print(Bcolors.OKBLUE + "\n" + player.name + " casts " + spell.name + " and attacks", enemies[target].name, "for", str(magicHp), "points of damage." + Bcolors.ENDC)
                if enemies[target].hp == 0:
                    del enemies[target]
        elif index == 2:
            itemChoice = player.chooseItem()
            if itemChoice == -1:
                back = len(players) + len(enemies) - 1
                continue
            
            item = player.items[itemChoice]
            
            if item["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + player.name, "doesn't have any", item["item"].name + "\n" + Bcolors.ENDC)
                continue
            else:
                player.items[itemChoice]["quantity"] -= 1
            
            if item["item"].type == "potion":
                player.heal(item["item"].prop)
                print(Bcolors.OKGREEN + "\n" + item["item"].name + " heals " + player.name + " for", str(item["item"].prop), "HP" + Bcolors.ENDC)
            elif item["item"].type == "elixer":
                if item["item"].name == "Hi-Elixer":
                    for i in players:
                        i.hp = i.maxHp
                        i.mp = i.maxMp
                    print(Bcolors.OKGREEN + "\n" + item["item"].name + " fully restores everybody's HP and MP" + Bcolors.ENDC)
                else:
                    player.hp = player.maxHp
                    player.mp = player.maxMp
                    print(Bcolors.OKGREEN + "\n" + item["item"].name + " fully restores " + player.name + "'s HP and MP" + Bcolors.ENDC)
            elif item["item"].type =="attack":
                target = player.chooseTarget(enemies)
                if target == -1:
                    back = len(players) + len(enemies) - 1
                    continue
                enemies[target].takeDamage(item["item"].prop)
                print(Bcolors.OKGREEN + "\n" + player.name + " uses " + item["item"].name + " and attacjs", enemies[target].name, "for", str(item["item"].prop), "points of damage." + Bcolors.ENDC)
                if enemies[target].hp == 0:
                    del enemies[target]

    for enemy in enemies:
        if back > 0:
            back -=1
            continue

        if enemy.getHp():
            enemyChoice = random.randrange(0, 3)
            
            if enemyChoice == 0:
                enemyDmg = enemy.generateDamage()
                hitPlayer = random.randrange(0, len(players))
                players[hitPlayer].takeDamage(enemyDmg)
                print(Bcolors.BOLD + Bcolors.FAIL + "Enemy attacks", players[hitPlayer].name, "for", str(enemyDmg), "points of damage." + Bcolors.ENDC)
                if players[hitPlayer].hp == 0:
                        del players[hitPlayer]
            elif enemyChoice == 1:
                magicChoice = random.randrange(0, len(enemy.magic))

                spell = enemy.magic[magicChoice]
                magicHp = spell.generateDamage()
                cost = spell.cost

                currentMp = enemy.getMp()

                if cost > currentMp:
                    continue
                
                enemy.reduceMp(cost)

                if spell.type == "white":
                    enemy.heal(magicHp)
                    print(Bcolors.OKBLUE + "\n" + enemy.name + " casts " + spell.name + " and heals", enemy.name, "for", str(magicHp), "health points." + Bcolors.ENDC)
                elif spell.type == "black":
                    target = random.randrange(0, len(players))
                    players[target].takeDamage(magicHp)
                    print(Bcolors.FAIL + "\n" + enemy.name + " casts " + spell.name + " and attacks", players[target].name, "for", str(magicHp), "points of damage." + Bcolors.ENDC)
                    if players[target].hp == 0:
                        del players[target]
            #elif enemyChoice == 2:

    if enemy1.getHp() == 0 and enemy2.getHp() == 0 and enemy3.getHp() == 0:
        enemiesAlive = False
        print(Bcolors.OKGREEN + "You won!" + Bcolors.ENDC)
    elif player1.getHp() == 0 and player2.getHp() == 0 and player3.getHp() == 0:
        playersAlive = False
        print(Bcolors.FAIL + "You lose!" + Bcolors.ENDC)

    if playersAlive == False or enemiesAlive == False:
        running = False