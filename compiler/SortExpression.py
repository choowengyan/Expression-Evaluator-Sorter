from compiler.Evaluator import *
from compiler.Parser import *

import sys
import os 
import glob
import click
import numpy as np


class SortExpression:
    def __init__(self, expression_list=[]):
        self.expression_list = expression_list
        self.sorted_value = None
        self.sorted_list = []
        self.inputFileName = None
        self.outputFileName = None
        super().__init__()

    def openFile(self):
        while True:
            try:
                self.inputFileName = input('Please enter input file: ')
                self.outputFileName = input('Please enter output file: ')
                inputFileName = self.inputFileName
                outputFileName = self.outputFileName

                with open(inputFileName) as f:
                    self.file_exp = [line.rstrip('\n') for line in f] 
                    #print(self.file_exp)
                return False

            except FileNotFoundError or IOError or PermissionError:
                print('\nInput or Output File not accessible, please try again\n')
        return outputFileName, self.file_exp

    def eval_expression(self, file_exp):
        values = []
        file_exp = self.file_exp
        print('\n>>> Evaluation and sorting started:')
        for i in file_exp:
            parser = Parser(i)
            tree = parser.parse()
            evaluator = Evaluator()
            value = evaluator.evaluate(tree)

            values.append(value)
            #print(f'{i} ==> {evaluator.evaluate(tree)}')
        #print("sorted value",sorted(values))
        #print(type(file_exp[0]))

        exp_val_list = list(zip(file_exp, values))
        #print("exp_val_list",exp_val_list)
        self.expression_list = exp_val_list
        return exp_val_list

    # bubble sort value 
    def sort_val(self, exp_list):

        l = len(exp_list)
        #print(exp_list[0])

        for i in range(0, l):
            for j in range(0, l-i-1):
                if(exp_list[j][1] > exp_list[j+1][1]):
                    temp = exp_list[j]
                    exp_list[j] = exp_list[j+1]
                    exp_list[j+1] = temp
        return exp_list
        self.sorted_value = exp_list
        
    # sort expressions by length 
    def sort_length(self, sorted_value):
        v = len(sorted_value)
        #print(sorted_value[0])

        for x in range(0, v):
            for y in range(0, v-x-1):
                if (sorted_value[y][1] == sorted_value[y+1][1]) and len(sorted_value[y][0]) > len(sorted_value[y+1][0]):
                    tmp = sorted_value[y]
                    sorted_value[y] = sorted_value[y+1]
                    sorted_value[y+1] = tmp

        #print("sorted_value(with length)", sorted_value)
        return sorted_value
        self.sorted_list = sorted_value

    # get unique value from list of expression values 
    def get_unique_value(self, sorted_list):
        unique_value = []
        for i in range(0, len(sorted_list)):
            val = sorted_list[i][1]
            unique_value.append(val)
        unique_value = np.unique(unique_value)
        #print(unique_value)
        self.get_unique_value = unique_value

    def write_expression(self, sorted_list):
        #print("getunique\n",self.get_unique_value)
        #print("sortedlist\n",sorted_list)

        unique_val_l = len(self.get_unique_value)
        output_file = open(self.outputFileName, 'w')
        
        for i in range(0, unique_val_l):
            #print(self.get_unique_value[i])
            output_file.write(f'\n*** Expressions with value = {self.get_unique_value[i]}\n')
            print(f'\n*** Expressions with value = {self.get_unique_value[i]}')

            for j in range(0, len(sorted_list)):
                #print("smtg",sorted_list[j][1])
                if self.get_unique_value[i] == sorted_list[j][1]:
                    #print(f'***Expressions with value = {self.get_unique_value[i]}')
                    output_file.write(f'{sorted_list[j][0]} ==> {sorted_list[j][1]}\n')
                    print(f'{sorted_list[j][0]} ==> {sorted_list[j][1]}')
        output_file.close()

        print("\n>>> Evaluation and sorting completed!\n ") 

    def eval_sort_output(self):
        
        sort = SortExpression()

        while True:
            exp = sort.openFile()
            eval = sort.eval_expression(exp)
            value = sort.sort_val(eval)

            sorted_ = sort.sort_length(value)
            sort.get_unique_value(sorted_)
            sort.write_expression(sorted_)

            return False

    



# sort = SortExpression()
# exp = sort.openFile2()
# eval = sort.eval_expression(exp)
# value = sort.sort_val(eval)
# sorted_ = sort.sort_length(value)
# sort.get_unique_value(sorted_)
# sort.write_expression(sorted_)


# sortEx = SortExpression()
# sortEx.eval_sort_output()