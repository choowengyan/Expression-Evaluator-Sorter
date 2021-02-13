  
from utils.ClassicMenu import ClassicMenu
from utils.InteractiveMenu import InteractiveMenu
from compiler.Lexer import Lexer
from compiler.Parser import Parser
import os


ClassicMenu = ClassicMenu() # classic menu version 
InteractiveMenu = InteractiveMenu() # interactive version 


while True:
    ClassicMenu.header()
    version = int(input("Welcome! Please choose a mode for the program:\n1. Original Mode\n2. Interactive Mode\n>>> "))
    try:
        if version == 1 :
            print()
            ClassicMenu.select_option()
        elif version ==2 : 
            print()
            InteractiveMenu.select_option()
    except ValueError:
        print('Invalid option, please try again.\n')

    # press key function to allow user to continue the application
    try:
        os.system('pause')  
    except whatever_it_is:
        os.system('read -p "\nPress any key to continue"')