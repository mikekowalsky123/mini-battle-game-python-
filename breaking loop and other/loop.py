import random


playerhp = 250
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp -= dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage.")
    if playerhp == 30:
        print("So low hp... xYou've been teleported to the nearest inn.")
        break
