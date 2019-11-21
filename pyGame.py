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
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'


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

### Game Functionality ###

def start_game():


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
    'a1':False,'a2':False,'a2':False,'a3':False,
    'b1':False,'b2':False,'b2':False,'b3':False,
    'c1':False,'c2':False,'c2':False,'c3':False,
    'd1':False,'d2':False,'d2':False,'d3':False
}

zonemap ={
    'a1':{
        ZONENAME: "Town Market"
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED =False
        UP = ''
        DOWN = 'b1'
        LEFT = ''
        RIGHT = 'a2'
    }
    'a2':{
        ZONENAME: "Town Entrance"
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED =False
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'a3'
    },
    'a3':{
        ZONENAME: "Town Square"
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED =False
        UP = ''
        DOWN = 'b3'
        LEFT = 'a2'
        RIGHT = 'a4'
    },
    'a4':{
        ZONENAME: "Town Hall"
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED =False
        UP = ''
        DOWN = 'b4'
        LEFT = 'a3'
        RIGHT = ''
    },
    'b1':{
        ZONENAME: ""
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED =False
        UP = 'a1'
        DOWN = 'c1'
        LEFT = ''
        RIGHT = 'b2'
    },
       'b2':{
        ZONENAME: ""
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED =False
        UP = 'a2'
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'b3'
    }
}
