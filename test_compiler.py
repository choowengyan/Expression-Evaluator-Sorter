from compiler.Lexer import Lexer
from compiler.Parser import Parser
from utils.Stack import Stack
from utils.BinaryTree import BinaryTree

# inputs = ['42', '02.2', '', '01', '00', '(', '+']
# inputs = ['42.0']
inputs = ['-42+1-10', '1 -+- 2.9', '1 2 * 2 ** 2', '-23 + 23 - 3']
# inputs = ['1 -+- 2.9 + 2', '-23 + 23 - 3']
# # inputs = ['1**2']
# # inputs = ['-2.9']
# # inputs = ['(2+1)*3']
# # # inputs = ['2 * 3 + ((1 + 2) - (3 * 4))']
for i in inputs:
# #     # lexer = Lexer(i)
# #     # print(lexer.getNextToken())
# #     # print(lexer)
    parser = Parser(i)
    print(parser.parse())
    # print(ast)
    # ast = parser.parse(i)


# exp = '-23+1'

# lexer = Lexer(exp)
# parser = Parser(exp)
# ast = parser.parse()
# print(ast)
# print()
# print("getKey\n", ast.getKey())
# print("left\n", ast.getLeftTree())
# print("right\n", ast.getRightTree())
# print("tree\n", ast)
# print("lexer\n", lexer.getNextToken())


