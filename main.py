from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 10, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(700, 65, 60, 34, magic)
enemy = Person(1100, 65, 45, 25, magic)

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print("==================")
    
    player.chooseAction()
    choice = input(Bcolors.OKBLUE + "Choose action: ")
    index = int(choice) - 1
    
    if index == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.chooseMagic()
        magicChoice = int(input("Choose spell:")) - 1
        magicDmg = player.generateSpellDamage(magicChoice)
        spell = player.getSpellName(magicChoice)
        cost = player.getSpellMpCost(magicChoice)
        currentMp = player.getMp()

        if cost > currentMp:
            print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
            continue
        
        player.reduceMp(cost)
        enemy.takeDamage(magicDmg)
        print(Bcolors.OKBLUE + "\n" + spell + " deals", str(magicDmg), "points of damage." + Bcolors.ENDC)

    enemyChoice = 1
    enemyDmg = enemy.generateDamage()
    player.takeDamage(enemyDmg)
    print("Enemy attacks for", str(enemyDmg), "points of damage.")

    print("------------------")

    print("Enemy HP:", Bcolors.FAIL + str(enemy.getHp()) + "/" + str(enemy.getMaxHp()) + Bcolors.ENDC)

    print("Your HP:", Bcolors.OKGREEN + str(player.getHp()) + "/" + str(player.getMaxHp()) + Bcolors.ENDC)
    print("Your MP:", Bcolors.OKBLUE + str(player.getMp()) + "/" + str(player.getMaxMp()) + Bcolors.ENDC)

    if enemy.getHp() == 0:
        print(Bcolors.OKGREEN + "You win!" + Bcolors.ENDC)
    elif player.getHp() == 0:
        print(Bcolors.FAIL + "You lose!" + Bcolors.ENDC)

    if player.getHp() == 0 or enemy.getHp() == 0:
        running = False