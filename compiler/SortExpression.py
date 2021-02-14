# -------------------------------------------------|
# ST1507 DSAA CA2 : Expression Evaluator & Sorter  |
# -------------------------------------------------|
# Name  : Silviana (1939213)                       |
#       : Choo Weng Yan (1940208)                  |
# Class : DIT/FT/2B/14                             |
# -------------------------------------------------|


'''
Sorting Expression class will prompt user for input file and output file in order
to read and write the expressions. 

This class will evaluate the expressions and sort them using bubble sort method. 
The functions will firstly sort the expressions by their values, and later by expression length.
User will be given option to sort expressions in ascending or descending order.

'''


from compiler.Evaluator import *
from compiler.Parser import *
from collections import OrderedDict 
import sys
import os 
import glob
import click


class SortExpression:

    # constructor 
    def __init__(self, expression_list=[]):
        self.expression_list = expression_list
        self.sorted_value = None
        self.sorted_list = []
        super().__init__()

    # prompt user for input and output file 
    def openFile(self):
        while True:
            try:
                self.inputFileName = input('Please enter input file: ')
                self.outputFileName = input('Please enter output file: ')
                inputFileName = self.inputFileName
                outputFileName = self.outputFileName

                # reads expression from input file 
                with open(inputFileName) as f:
                    self.file_exp = [line.rstrip('\n') for line in f] 
                return False

            except FileNotFoundError or IOError or PermissionError:
                print('\nInput or Output File not accessible, please try again\n')
        return outputFileName, self.file_exp

    # evaluate expressions and return values into the list 
    def eval_expression(self, file_exp):
        values = []
        file_exp = self.file_exp

        for i in file_exp:
            parser = Parser(i)
            tree = parser.parse()
            evaluator = Evaluator()

            value = evaluator.evaluate(tree)
            values.append(value)

        # form tuple, compile expression and values by zipping them up 
        exp_val_list = list(zip(file_exp, values))
        self.expression_list = exp_val_list
        return exp_val_list

    '''
    Implementation of bubble sort method to sort expression 
    '''

    # sort the value of expression (ascending order)
    def sort_val_asc(self, exp_list):

        l = len(exp_list)

        for i in range(0, l):
            for j in range(0, l-i-1):
                if(exp_list[j][1] > exp_list[j+1][1]):
                    temp = exp_list[j]
                    exp_list[j] = exp_list[j+1]
                    exp_list[j+1] = temp
        return exp_list
        self.sorted_value = exp_list

    # sort the value of expression (descending order)
    def sort_val_desc(self, exp_list):
        l = len(exp_list)

        for i in range(0, l):
            for j in range(0, l-i-1):
                if(exp_list[j][1] < exp_list[j+1][1]):
                    temp = exp_list[j+1]
                    exp_list[j+1] = exp_list[j]
                    exp_list[j] = temp
        return exp_list
        self.sorted_value = exp_list
        
    # sort the length expression (ascending order)
    def sort_length_asc(self, sorted_value):
        v = len(sorted_value)

        for x in range(0, v):
            for y in range(0, v-x-1):
                if (sorted_value[y][1] == sorted_value[y+1][1]) and len(sorted_value[y][0]) > len(sorted_value[y+1][0]):
                    tmp = sorted_value[y]
                    sorted_value[y] = sorted_value[y+1]
                    sorted_value[y+1] = tmp

        self.sorted_list = sorted_value
        return sorted_value

    # sort the length of expression (descending order)
    def sort_length_desc(self, sorted_value):
        v = len(sorted_value)

        for x in range(0, v):
            for y in range(0, v-x-1):
                if (sorted_value[y][1] == sorted_value[y+1][1]) and len(sorted_value[y][0]) < len(sorted_value[y+1][0]):
                    tmp = sorted_value[y+1]
                    sorted_value[y+1] = sorted_value[y]
                    sorted_value[y] = tmp

        return sorted_value
        self.sorted_list = sorted_value

    # get unique value from list of expression values 
    def get_unique_value(self, sorted_list):
        unique_value = []
 
        for i in range(0, len(sorted_list)):
            val = sorted_list[i][1]
            unique_value.append(val)

        # OrderedDict module to get the exact order of the value from the list 
        unique_value = list(OrderedDict.fromkeys(unique_value))
        self.get_unique_value = unique_value

    # write expression into the output file 
    def write_expression(self, sorted_list):

        unique_val_l = len(self.get_unique_value)
        output_file = open(self.outputFileName, 'w')
        
        for i in range(0, unique_val_l):
            output_file.write(f'\n*** Expressions with value = {self.get_unique_value[i]}\n')
            print(f'\n*** Expressions with value = {self.get_unique_value[i]}')

            for j in range(0, len(sorted_list)):
                if self.get_unique_value[i] == sorted_list[j][1]:
                    output_file.write(f'{sorted_list[j][0]} ==> {sorted_list[j][1]}\n')
                    print(f'{sorted_list[j][0]} ==> {sorted_list[j][1]}')
        output_file.close()

        print("\n>>> Evaluation and sorting completed!\n ") 

    # prompt user for order of sorting
    # print output on terminal and output file 
    def printOutput(self):
        
        sort = SortExpression()

        while True:
            exp = sort.openFile()
            sort_choice = int(input('\nPrint expression in:\n1. Ascending Order\n2. Descending Order\n>>>'))
            print('\n>>> Evaluation and Sorting has started: ')
            self.eval_ = sort.eval_expression(exp)
            
            try: 
                if sort_choice == 1:
                    self.value = sort.sort_val_asc(self.eval_)
                    self.sorted_ = sort.sort_length_asc(self.value)
                elif sort_choice == 2:
                    self.value = sort.sort_val_desc(self.eval_)
                    self.sorted_ = sort.sort_length_desc(self.value)
                else: 
                    print('Invalid input, please try again')
                    sort.printOutput()
            except ValueError:
                print('Only choice "1" or choice "2" is allowed, please try again.\n')
                sort.printOutput()

            sort.get_unique_value(self.sorted_)
            sort.write_expression(self.sorted_)
            return False

