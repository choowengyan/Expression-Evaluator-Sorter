from compiler.Lexer import Lexer
from compiler.Parser import Parser


# inputs = ['42', '02.2', '', '01', '00', '(', '+']
# inputs = ['42.0']
# inputs = ['42+1-10', '1 -+- 2 . 9', '1 2 * 2 ** 2']
# # inputs = ['1**2']
# # inputs = ['-2.9']
# # inputs = ['(2+1)*3']
# # inputs = ['2 * 3 + ((1 + 2) - (3 * 4))']
# for i in inputs:
#     # lexer = Lexer(i)
#     # print(lexer.getNextToken())
#     # print(lexer)
#     parser = Parser(i)
#     print(parser.parse())
#     print()
#     # ast = parser.parse(i)
#     # print(ast)


exp = '(23+23)'

parser = Parser(exp)
print(parser.parse())
    # print()