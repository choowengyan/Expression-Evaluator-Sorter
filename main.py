from classicMenu import classicMenu
from interactiveMenu import interactiveMenu
import os


classicMenu = classicMenu() # classic menu version 
interactiveMenu = interactiveMenu() # interactive version 


while True:
    classicMenu.header()
    version = int(input("Welcome! Please choose a mode for the program:\n1. Original Mode\n2. Interactive Mode\n>>> "))
    try:
        if version == 1 :
            print()
            classicMenu.select_option()
        elif version ==2 : 
            print()
            interactiveMenu.select_option()
    except ValueError:
        print('Invalid option, please try again.\n')

    # press key function to allow user to continue the application
    try:
        os.system('pause')  
    except whatever_it_is:
        os.system('read -p "Press any key to continue"')
