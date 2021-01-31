# selection menu

from collections import namedtuple
from eval_expression import *
import sys
import os
import msvcrt
import time
import AnsiEscapeCodes as constant

# prints menu and runs the function of the chosen option
class interactiveMenu:
    def __init__(self):
        self.chosen = 0
        self.Option = namedtuple('Option', 'label')
        self.options = {1: self.Option("Evaluate Expression"),
                        2: self.Option("Sort Expressions"),
                        3: self.Option("Exit")}


    def header(self):
        border_symbol = "*"
        course = ' ST1507 DSAA: Expression Evaluator & Sorter'
        done_by = ' - Done by: Silviana (1939213) & Choo Weng Yan (1940208)'
        class_name = ' - Class: DIT/FT/2B/14'

        # border = (len(done_by)+4) * border_symbol
        border = 60*border_symbol
        separator = (len(border)-4) * "-"

        print(border)
        print(border_symbol, course.center(55), border_symbol.rjust(2))
        print(border_symbol, separator, border_symbol)
        print(border_symbol, len(separator)*" ", border_symbol)
        print(border_symbol, done_by, border_symbol)
        print(border_symbol, class_name, border_symbol.rjust(35))
        print(border, '\n')

    def printMenu(self, move_cursor):
        print("Please press up or down arrow to select: ")
        self.chosen += move_cursor
        
        if self.chosen <= 0:
            self.chosen = len(self.options)
        if self.chosen > len(self.options):
            self.chosen = 1

        os.system('color')

        for option in sorted(self.options.keys()):
            sys.stdout.write(constant.COLOR['BLUE'])
            print(constant.COLOR['YELLOW'] + '>' if self.chosen == option else '', self.options[option].label)
            sys.stdout.write(constant.COLOR['DEFAULT'])

    # selection
    def select_option(self):
        self.header()
        self.printMenu(1)
        while True:
            # time.sleep(0.5)
            if msvcrt.kbhit():
                first_key = msvcrt.getch()
                if first_key == b'\x00':
                    key = msvcrt.getch()
                    if key in [b'H', b'P']:
                        self.delete_last_lines(n=4)
                        self.printMenu(1 if key == b'P' else -1)
                elif first_key == b'\r':
                    self.process_selection()
                    break
                else:
                    pass

    def process_selection(self):
        print()
        if self.chosen == 1:
            print('Option 1: Evaluate Expression has chosen.\n') 
            eval_expression()
            return False

        elif self.chosen == 2:
            print('Option 2: Sort Expression has chosen.\n')
            # sort exp to be done
            return False
        elif self.chosen == 3:
            print('Option 3: Exit\nBye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter')
            # exits the program
            sys.exit()
        else:
            print('Input number is not in the menu option, please try again.\n')

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear') 

    def delete_last_lines(self, n):
        for _ in range(n): 
            sys.stdout.write(constant.CURSOR_UP_ONE) 
            sys.stdout.write(constant.ERASE_LINE) 


# menu = Menu()
# menu.select_option()
