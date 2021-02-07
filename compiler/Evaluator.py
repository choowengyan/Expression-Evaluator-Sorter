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

    def printParseTree(self):
        # parser tree
        print("ast\n{}".format(self.tree))
        # print(self.evaluate(self.tree))


    def evaluate(self, ast):
        leftTree = ast.getLeftTree()
        rightTree = ast.getRightTree()
        op = ast.getKey()

        try:
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
                elif op == '**':
                    return round(self.evaluate(leftTree) ** self.evaluate(rightTree), 2)
                elif op == '/':
                    return round(self.evaluate(leftTree) / self.evaluate(rightTree),2)
            else:
                return ast.getKey()
        except TypeError:
            print('Seems like expression format is invalid. Please try again.\n')
        except ValueError:
            print('Seems like expression format is invalid. Please try again.\n')
        except ZeroDivisionError:
            print(f'{self.evaluate(leftTree)} cannot divide by 0, please try again.')
          

    def eval_expression():
        while True:
            self.exp = input('Please enter expression: \n')
            try:
                # empty input
                if len(self.exp) == 0: 
                    print("Expression is empty. Please try again.\n")
                else:
                    self.parser = Parser(exp)
                    self.tree = self.parser.parse()
                    self.tree.printPreorder(0)
                    print(f'\nExpression evaluates to: \n{self.evaluate(self.tree)}')
                    return False
                    break
            except ValueError: 
                print('You entered invalid expression format. Please try again.\n')


# exp = '(23+23-23+(23**3))'
# eval = Evaluator()
# eval.buildParseTree()
# eval.evaluate()
