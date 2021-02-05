from compiler.Lexer import Lexer
from compiler.Parser import Parser
from compiler.Evaluator import Evaluator





# exp = '(23+23-23+(23**3))'
exp = '(23+23-3)'


eval = Evaluator(exp)
Evaluator.buildParseTree(exp)
#Evaluator.evaluate(exp)




