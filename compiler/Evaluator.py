from utils.BinaryTree import BinaryTree
from utils.Stack import Stack
from compiler.Lexer import Lexer
from compiler.Parser import Parser
from compiler.TokenTypes import *


class Evaluator:
    def __init__(self, exp):
        self.exp = exp
        self.parser = Parser(exp)

    def buildParseTree(exp):
        parser = Parser(exp)
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)


        # parser tree
        ast = parser.parse()
        print("ast\n",ast)


    def evaluate(ast):
        leftTree = ast.getLeftTree()
        print('left', leftTree)

        rightTree = ast.getRightTree()
        print('right', rightTree)
        
        op = ast.getKey()
        print("op", op)

        try:
            if leftTree != None and rightTree != None:
                if op == '+':
                    return round(evaluate(leftTree) + evaluate(rightTree), 2)
                elif op == '-':
                    return round(evaluate(leftTree) - evaluate(rightTree), 2)
                elif op == '*':
                    return round(evaluate(leftTree) * evaluate(rightTree), 2)
                elif op == '**':
                    return round(evaluate(leftTree) ** evaluate(rightTree), 2)
                elif op == '/':
                    if evaluate(rightTree) != 0:
                        return round(evaluate(leftTree) / evaluate(rightTree),2)
                    else:
                        print(f'{evaluate(leftTree)} cannot divide by 0, please try again.')
                        # eval_expression()
            else:
                return ast.getKey()
        except TypeError:
            print('Seems like expression format is invalid. Please try again.\n')
            # eval_expression()
          





    # def input_expression():
    #     while True:
    #         try:
    #             exp = input('Please enter expression: \n')
    #         except EOFError:
    #             break
    #         if not exp:
    #             continue

    #         lexer = Lexer(exp)
    #         parser = Parser(lexer)
    #         ast = parser.parse()

    #         print(ast)


# exp = '(23+23-23+(23**3))'
# eval = Evaluator()
# eval.buildParseTree()
# eval.evaluate()
