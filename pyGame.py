# pythone game tutorial
# andrew ogle

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### player setup ###


class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = Player()

### Title Screen ###


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()  # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()  # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    title_screen_selections()

### help menu ###


def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    title_screen_selections()



### Map ###
"""
a1 a2... # player starts at b2
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED =False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1':False,'a2':False,'a3':False,'a4':False,
    'b1':False,'b2':False,'b3':False,'b4':False,
    'c1':False,'c2':False,'c3':False,'c4':False,
    'd1':False,'d2':False,'d3':False,'d4':False
}

zonemap ={
    'a1':{
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED:False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2':{
        ZONENAME: "Town Entrance",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED :False,
        UP : '',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a3',
    },
    'a3':{
        ZONENAME: "Town Square",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED :False,
        UP : '',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'a4',
    },
    'a4':{
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED:False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1':{
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED:False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
       'b2':{
        ZONENAME: "home",
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks the same - nothing has changed',
        SOLVED:False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
    },
}
### Game Interactivity ###
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "=========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go','travel', 'walk', 'quit', 'examine', 'interact', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go','travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'interact', 'inspect', 'look']:
        play_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to? \n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to the" + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("you have already exhuasted this zone")
    else:
        print("you have triggered a puzzle")

### Game Functionality ###
def start_game():
    os.system('clear')

    question1 = "Hello, what's your name? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    
    question2 = "What role do you want to play? \n"
    question2added = "You can play as a warrior, priest, or mage \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("\n you are now a " + player_job + "!")
    while player_job not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("\n you are now a " + player_job + "!")

    if myPlayer.job is 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job is 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job is 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60
    
    ### intro ###

    question3 = "Welcome " + player_name + " the" + player_job + "\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system('clear')
    print('lets start now')
    main_game_loop()
    
    

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

title_screen()