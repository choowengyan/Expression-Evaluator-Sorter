# selection menu

from collections import namedtuple
import sys


# prints menu and runs the function of the chosen option
class Menu:

    Option = namedtuple('Option', 'label')
    options = {1: Option("Evaluate Expression"),
               2: Option("Sort Expressions"),
               3: Option("Exit")}

    # def __init__(self)

    def header(self):
        border_symbol = "*"
        course = ' ST1507 DSAA: Expression Evaluator & Sorter'
        done_by = ' - Done by: Silviana (1939213) & Choo Weng Yan (1940208)'
        class_name = ' - Class: DIT/FT/2B/14'

        # border = (len(done_by)+4) * border_symbol
        border = 60*border_symbol
        seperator = (len(border)-4) * "-"

        print(border)
        print(border_symbol, course.center(55), border_symbol.rjust(2))
        print(border_symbol, seperator, border_symbol)
        print(border_symbol, len(seperator)*" ", border_symbol)
        print(border_symbol, done_by, border_symbol)
        print(border_symbol, class_name, border_symbol.rjust(35))
        print(border, '\n')

    def printMenu(self):
        print("Please select your choice <'1', '2', '3'>: ")
        for option in sorted(self.options.keys()):
            print("{0}. {1}".format(option, self.options[option].label))
        print()

    # selection
    def select_option(self):
        while True:
            self.printMenu()

            try:
                choice = int(input("Please enter your choice: "))
                if choice == 1:
                    print('Option 1: Evaluate Expression has chosen.')
                    # eval expres to be done
                    return False

                elif choice == 2:
                    print('Option 2: Sort Expression has chosen.')
                    # sort exp to be done
                    return False
                elif choice == 3:
                    print('Option 3: Exit')
                    print(
                        'Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter ')
                    # exits the program
                    sys.exit()
                else:
                    print('Input number is not in the menu option, please try again.\n')
            # wrong value type
            except(ValueError):
                print("Only number is allowed, please try again.\n")


menu = Menu()
menu.header()
menu.select_option()
