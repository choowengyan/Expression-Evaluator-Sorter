from compiler.Lexer import Lexer
from compiler.Parser import Parser
from compiler.Evaluator import Evaluator
import os, sys
os.system('color')

# binary expressions
b_exp = ['1+2', '1-2', '1*2', '1/2', '1%2', '1**2', '1//3']

# unary expressions
u_exp = ['1', '-1', '+1', '--1', '-+1']


# fully parenthesized expressions
fpe_exp = ['((23-2)*(342-2))', '((200+(4*3.14))/(2**3))']

# binary unary expressions
bu_exp = ['1+--1', '2----2', '--2 + 1', '-2 + 1']

# invalid expressions
iv_exp = ['1/0', '1 */ 2', '1 /* 2', '1 -* 2', '1 _ 2', '(1-2', '2-1)', 'abc', '-+']

def testing(expressions, is_valid):
    print('------------------------------------')
    for i, exp in enumerate(expressions):
        evaluator = Evaluator()
        result = evaluator.eval_expression(exp)

        if is_valid:
            sys.stdout.write('{} | {} \t\t| {}\t'.format(i, eval(exp), result))
            if eval(exp) == result:
                sys.stdout.write('\033[94m[PASSED]')
            else:
                sys.stdout.write('\033[33m[FAILED]')
        else:
            sys.stdout.write('{} | {} | {}\t'.format(i, exp, result))
            if None == result:
                sys.stdout.write('\033[94m[PASSED]')
            else:
                sys.stdout.write('\033[33m[FAILED]')
        print('\033[m\n')
    print('\n')

valid_test_cases = [b_exp, u_exp, fpe_exp, bu_exp]
invalid_test_cases = [iv_exp]

for case in valid_test_cases:
    testing(case, True)

for case in invalid_test_cases:
    testing(case, False)


#exp = '((23-2)*(342-2))'
# exp = '-3+23'
# exp = input('expression')
# evaluator = Evaluator()
# evaluator.eval_expression(exp)
# evaluator = Evaluator()
# evaluator.printParseTree()
# evaluator.eval_expression()
# print(eval(exp))
# evaluator.evaluate()
# exp = '(232*23-2)'
# print("eval",eval(exp))