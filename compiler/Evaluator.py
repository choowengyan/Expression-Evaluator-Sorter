# -------------------------------------------------|
# ST1507 DSAA CA2 : Expression Evaluator & Sorter  |
# -------------------------------------------------|
# Name  : Silviana (1939213)                       |
#       : Choo Weng Yan (1940208)                  |
# Class : DIT/FT/2B/14                             |
# -------------------------------------------------|

'''
Evaluates input expression by importing tokens and trees from utils and compiler 
folder. 

Methods:
- print Parse Tree
    - Preoder Traversal
    - Inoder Traversal
    - Postoder Traversal
- evaluate expression and return value in 2 decimal places 
'''

from utils.BinaryTree import BinaryTree
from utils.Stack import Stack
from compiler.Lexer import Lexer
from compiler.Parser import Parser
from compiler.TokenTypes import *


class Evaluator:
    def __init__(self, exp=''):
        self.exp = exp
        self.parser = Parser(exp)
        self.tree = self.parser.parse()

    # Print tree in different traversal order 
    def printParseTree(self):
        # parser tree
        # print("ast\n{}".format(self.tree))
        # print(self.evaluate(self.tree))
        order_choice = int(input('\nPrint expression in:\n1. Preorder Traversal\n2. Inorder Traversal\n3. Postorder Traversal\n>>> '))

        if order_choice == 1:
            print('\nPreorder Tree Transversal:')
            self.tree.printPreorder(0)
        elif order_choice == 2:
            print('\nInorder Tree Transversal:')
            self.tree.printInorder(0)
        elif order_choice == 3:
            print('\nPostorder Tree Transversal:')
            self.tree.printPostorder(0)
        else:
            print('Invalid choice, please try again.\n')

    # Evaluate expressions 
    def evaluate(self, ast):
        try:
            leftTree = ast.getLeftTree()
            rightTree = ast.getRightTree()
            op = ast.getKey()
            # Unary Operator
            if leftTree == None:
                if op == '+':
                    return +self.evaluate(rightTree)
                elif op == '-':
                    return -self.evaluate(rightTree)
            # Binary Operator
            if leftTree != None and rightTree != None:
                if op == '+':
                    return round(self.evaluate(leftTree) + self.evaluate(rightTree), 2)
                elif op == '-':
                    return round(self.evaluate(leftTree) - self.evaluate(rightTree), 2)
                elif op == '*':
                    return round(self.evaluate(leftTree) * self.evaluate(rightTree), 2)
                elif op == '%':
                    return round(self.evaluate(leftTree) % self.evaluate(rightTree), 2)
                elif op == '**':
                    return round(self.evaluate(leftTree) ** self.evaluate(rightTree), 2)
                elif op == '//':
                    return round(self.evaluate(leftTree) // self.evaluate(rightTree), 2)
                elif op == '/':
                    return round(self.evaluate(leftTree) / self.evaluate(rightTree), 2)
            else:
                return ast.getKey()
        except TypeError:
            print('Seems like expression format is invalid. Please try again.\n')
        except ValueError:
            print('Seems like expression format is invalid. Please try again.\n')
        except AttributeError:
            print('Seems like expression format is invalid. Please try again.\n')
        except ZeroDivisionError:
            print(f'{self.evaluate(leftTree)} cannot divide by 0, please try again.')

    # Print chosen parse tree traversal order and return expression value 
    def eval_expression(self, exp):
        self.exp = exp
        try:
            # empty input
            if len(self.exp) == 0:
                print("Expression is empty. Please try again.\n")
            else:
                try:
                    self.parser = Parser(exp)
                    self.tree = self.parser.parse()
                    self.printParseTree()
                except:
                    raise ValueError('Invalid input, please try again.\n')
                result = self.evaluate(self.tree)
                print(f'\nExpression evaluates to: \n{result}\n')
                # return result to assert on test_evalexp.py
                return result
                return False
        except ValueError:
            raise ValueError('You entered invalid expression format. Please try again.\n')
