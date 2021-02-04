# Expression parser: recursive descent implementation
from utils import BinaryTree
from compiler.Lexer import Lexer
from compiler.TokenTypes import *

class Parser:
    def __init__(self, string):
        self.__string = string
        self.__lexer = Lexer(self.__string)
        self.__current_token = self.__lexer.getNextToken()
        self.__lookahead = None

    def __str__(self):
        return('lexer-------------\n{}\ncurrent token: {}'.format(self.__lexer, self.__current_token))

    def error(self):
        raise Exception('Error in Parser')

    # Parses string into AST
    def parse(self):
        self.__lexer = Lexer(self.__string)
        self.__lookahead = self.__lexer.getNextToken()
        return self.Expression()
    
    def Expression(self):
        return self.AdditiveExpression()

    def __BinaryExpression(self, builder_func, operator_token):
        left = builder_func()
        while self.__lookahead.type == operator_token:
            operator = self.__eat(operator_token).value
            right = builder_func()
            if right == None or left == None:
                raise ValueError('__BinaryExpression: Invalid Binary Expression')
            left = {
                'type': 'BinaryExpression',
                'operator': operator,
                'left': left,
                'right': right
            }
        return left
    
    def __UnaryExpression(self, builder_func, operator_token):
        while self.__lookahead.type == operator_token:
            operator = self.__eat(operator_token).value
            right = builder_func()
            left = {
                'type': 'UnaryExpression',
                'operator': operator,
                'right': right
            }
        return left

    def AdditiveExpression(self):
        return self.__BinaryExpression(self.MultiplicativeExpression, 'ADDITIVE_OPERATOR')

    def MultiplicativeExpression(self):
        return self.__BinaryExpression(self.ExponentialExpression, 'MULTIPLICATIVE_OPERATOR')
    
    def ExponentialExpression(self):
        return self.__BinaryExpression(self.PrimaryExpression, 'EXPONENTIAL_OPERATOR')
    
    def PrimaryExpression(self):
        if self.__lookahead.type == OPEN_PARENTHESIS:
            return self.ParenthesizedExpression()
        elif self.__lookahead.type == ADDITIVE_OPERATOR:
            return self.__UnaryExpression(self.PrimaryExpression, ADDITIVE_OPERATOR)
        else:
            return self.NumericLiteral()
    
    def ParenthesizedExpression(self):
        self.__eat(OPEN_PARENTHESIS)
        expression = self.Expression()
        self.__eat(CLOSING_PARENTHESIS)
        return expression
    
    # NumericLiteral
    #   : NUMBER
    #   ;
    def NumericLiteral(self):
        try:
            token = self.__eat('NUMBER')
            return {
                'type': 'NumericLiteral',
                'value': token.value
            }
        except:
            print('Error in NumericLiteral(): Not a number')

    def __eat(self, token_type):
        try:
            token = self.__lookahead
            if token.type == None:
                raise TypeError()
            if token.type != token_type:
                raise TypeError()
            self.__lookahead = self.__lexer.getNextToken()
            return token
        except TypeError:
            print('Error in __eat: Unexpected token: {}, expected {}'.format(token.type, token_type))