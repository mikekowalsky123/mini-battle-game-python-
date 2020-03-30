'''from classes.game import DataLoader, JsonLoader, Config, MessageGenerator, CompatiblityMessageGenerator, Menu, Statistics, Actions, CheckAlive, SelectMessage
from classes.character import Character'''
from classes.game import JsonLoader, Config, MessageGenerator, CompatiblityMessageGenerator, Menu, SelectMessage
from game import Game

running = True

while running:

    messageSelect = SelectMessage.get()
    if messageSelect == 1:
        message = MessageGenerator()
    else:
        message = CompatiblityMessageGenerator()

    menu = Menu(message)

    game = Game(message, menu)

    mainMenu = ["Start a game", "Get help", "Exit"]
    menu.display("Main Menu", mainMenu)
    mainMenuChoice = menu.getChoice(mainMenu, "Select option")

    if mainMenuChoice == 0:
        game.startFight()

    elif mainMenuChoice == 1:
        print("\nActually there is no help. :)\n")

    elif mainMenuChoice == 2:
        running = False
