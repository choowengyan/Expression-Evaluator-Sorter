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
                    return round(self.evaluate(leftTree) / self.evaluate(rightTree), 2)
            else:
                return ast.getKey()
        except TypeError:
            print('Seems like expression format is invalid. Please try again.\n')
        except ValueError:
            print('Seems like expression format is invalid. Please try again.\n')
        except ZeroDivisionError:
            print(f'{self.evaluate(leftTree)} cannot divide by 0, please try again.')

    def eval_expression(self, exp):
        while True:
            self.exp = exp
            try:
                # empty input
                if len(self.exp) == 0:
                    print("Expression is empty. Please try again.\n")
                else:
                    #self.parser = Parser(exp)
                    #self.tree = self.parser.parse()
                    # self.tree.printPreorder(0)
                    
                    try:
                        self.parser = Parser(exp)
                        self.tree = self.parser.parse()
             
                        # Print tree in different traversal order 
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
                            self.eval_expression(exp)
                    except ValueError:
                        print('Invalid input, please try again.\n')
                        self.eval_expression(exp)
                        
                    print(f'\nExpression evaluates to: \n{self.evaluate(self.tree)}\n')
                    return False
            except ValueError:
                print('You entered invalid expression format. Please try again.\n')