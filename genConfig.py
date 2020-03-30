import simplejson as json
import os

spellsJson = open("./config/spells.json", "w")
itemsJson = open("./config/items.json", "w")
playersJson = open("./config/players.json", "w")
enemiesJson = open("./config/enemies.json", "w")

spells = [{
        "name": "Fireball",
        "cost": 20,
        "value": 300,
        "school": "attack"
    },
    {
        "name": "Thunder",
        "cost": 25,
        "value": 400,
        "school": "attack"
    },
    {
        "name": "Blizzard",
        "cost": 30,
        "value": 500,
        "school": "attack"
    },
    {
        "name": "Cure",
        "cost": 20,
        "value": 200,
        "school": "white"
    },
    {
        "name": "Super Cure",
        "cost": 40,
        "value": 600,
        "school": "white"
    }
]

items = [{
        "name": "Potion",
        "itemType": "potion",
        "description": "Heals 100 HP",
        "value": 100
    },
    {
        "name": "Super Potion",
        "itemType": "potion",
        "description": "Heals 300 HP",
        "value": 300
    },
    {
        "name": "Elixer",
        "itemType": "elixer",
        "description": "Fully restores HP and MP",
        "value": 1
    },
    {
        "name": "Scroll of FireRain",
        "itemType": "attack",
        "description": "Deals 500 damage",
        "value": 500
    }
]

players = [{
        "name": "YourMama",
        "hp": 3260,
        "mp": 65,
        "atk": 100,
        "df": 60,
        "spells": [0, 1, 2, 3, 4],
        "items": [{
                "id": 0,
                "quantity": 5
            },
            {
                "id": 1,
                "quantity": 2
            },
            {
                "id": 2,
                "quantity": 2
            },
            {
                "id": 3,
                "quantity": 1
            }
        ]
    },
    {
        "name": "Moron",
        "hp": 1200,
        "mp": 20,
        "atk": 500,
        "df": 120,
        "spells": [3],
        "items": [{
                "id": 0,
                "quantity": 5
            },
            {
                "id": 1,
                "quantity": 2
            },
            {
                "id": 2,
                "quantity": 2
            },
            {
                "id": 3,
                "quantity": 1
            }
        ]
    },
    {
        "name": "SmartBoy",
        "hp": 1500,
        "mp": 240,
        "atk": 25,
        "df": 35,
        "spells": [0, 1, 2, 3, 4],
        "items": [{
                "id": 0,
                "quantity": 10
            },
            {
                "id": 1,
                "quantity": 5
            },
            {
                "id": 2,
                "quantity": 4
            },
            {
                "id": 3,
                "quantity": 3
            }
        ]
    },
    {
        "name": "Nick",
        "hp": 2000,
        "mp": 100,
        "atk": 200,
        "df": 25,
        "spells": [0, 1, 2, 3, 4],
        "items": [{
                "id": 0,
                "quantity": 5
            },
            {
                "id": 1,
                "quantity": 2
            },
            {
                "id": 2,
                "quantity": 2
            },
            {
                "id": 3,
                "quantity": 1
            }
        ]
    }
]

enemies = [{
        "name": "BadAss",
        "hp": 9000,
        "mp": 100,
        "atk": 400,
        "df": 100,
        "spells": [0, 1, 2, 3, 4],
        "items": [{
                "id": 0,
                "quantity": 3
            },
            {
                "id": 1,
                "quantity": 1
            },
            {
                "id": 2,
                "quantity": 1
            },
            {
                "id": 3,
                "quantity": 1
            }
        ]
    },
    {
        "name": "Super Spider",
        "hp": 2000,
        "mp": 20,
        "atk": 100,
        "df": 10,
        "spells": [],
        "items": []
    },
    {
        "name": "BadRobot",
        "hp": 4000,
        "mp": 20,
        "atk": 150,
        "df": 100,
        "spells": [3],
        "items": [
            {
                "id": 3,
                "quantity": 5
            }
        ]
    },
    {
        "name": "Nick Alter-Ego",
        "hp": 2000,
        "mp": 100,
        "atk": 100,
        "df": 25,
        "spells": [0, 1, 2, 3, 4],
        "items": [{
                "id": 0,
                "quantity": 5
            },
            {
                "id": 1,
                "quantity": 2
            },
            {
                "id": 2,
                "quantity": 2
            },
            {
                "id": 3,
                "quantity": 1
            }
        ]
    }
]

spellsJson.write(json.dumps(spells))
itemsJson.write(json.dumps(items))
playersJson.write(json.dumps(players))
enemiesJson.write(json.dumps(enemies))