from compiler.Lexer import Lexer
from compiler.Parser import Parser
from compiler.Evaluator import Evaluator





exp = '(23+23-*23/+(23**3))'
# exp = '-3+23'


evaluator = Evaluator(exp)
# evaluator.printParseTree()
evaluator.eval_expression()
# print(eval(exp))
# evaluator.evaluate()




