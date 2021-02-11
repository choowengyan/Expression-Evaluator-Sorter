from compiler.Lexer import Lexer
from compiler.Parser import Parser
from compiler.Evaluator import Evaluator





#exp = '((23-2)*(342-2))'
# exp = '-3+23'
exp = input('expression')
evaluator = Evaluator()
evaluator.eval_expression(exp)
# evaluator = Evaluator()
# evaluator.printParseTree()
# evaluator.eval_expression()
# print(eval(exp))
# evaluator.evaluate()
exp = '(232*23-2)'
print("eval",eval(exp))