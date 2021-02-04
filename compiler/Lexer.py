'''
The lexer reads characters from the input/character reader and produces tokens. 
In other words, it converts a character stream into a token stream. 
Hence its sometimes also called the tokenizer. 
These tokens are produced according to the defined grammar. 
'''
import os
import sys
import math
import re
from compiler.Token import Token
from compiler.TokenTypes import *

'''
Lexer Class
------------------------
Constructors:
- __expression
- __input
- __current_char

Methods:
- getNextToken
- __number
- __advance
- __isspace
- __isnum
- __isdot
- __isAdditiveOperator
- __isMultiplicativeOperator
- __isOpenParenthesis
- __isClosingParenthesis
'''

class Lexer():
    def __init__(self, expression):
        self.__expression = expression
        self.__position = 0
        self.__current_char = self.__expression[self.__position] if len(self.__expression) > 0 else None

    def __str__(self):
        return 'expression: {}\nposition: {}'.format(self.__expression, self.__position)

    def error(self):
        raise Exception('Invalid syntax')

    def getNextToken(self):
        while self.__current_char is not None:
            if self.__isspace():
                self.__advance()
                continue

            if self.__isnum():
                return Token(NUMBER, self.__number())

            if self.__isAdditiveOperator():
                operator = self.__current_char
                self.__advance()
                return Token(ADDITIVE_OPERATOR, operator)

            if self.__isMultiplicativeOperator():
                operator = self.__current_char
                self.__advance()
                if self.__isMultiplicativeOperator():
                    operator += self.__current_char
                    if self.__isExponentialOperator(operator):
                        self.__advance()
                        return Token(EXPONENTIAL_OPERATOR, operator)
                return Token(MULTIPLICATIVE_OPERATOR, operator)
            
            if self.__isOpenParenthesis():
                parenthesis = self.__current_char
                self.__advance()
                return Token(OPEN_PARENTHESIS, parenthesis)
            
            if self.__isClosingParenthesis():
                parenthesis = self.__current_char
                self.__advance()
                return Token(CLOSING_PARENTHESIS, parenthesis)
            return self.error()
        return Token(EOF, self.__current_char)

    def __hasMoreTokens(self):
        return self.__position < len(self.__expression)

    def __number(self):
        number = ''
        while self.__current_char is not None and (self.__isnum() or self.__isdot() or self.__isspace()):
            # skip whitespaces between digits
            if self.__isspace():
                self.__advance()
                continue
            number += self.__current_char
            self.__advance()
        if re.match('([0-9]{1,}[.])[0-9]+', number):
            return float(number)
        elif re.match('[0-9]+', number):
            return int(number)
        else:
            return self.error()
        
    def __isnum(self):
        return re.match('^[0-9]', self.__current_char) != None
    
    def __isdot(self):
        return re.match('^[.]', self.__current_char) != None

    def __isspace(self):
        return re.match('^\s+', self.__current_char) != None

    def __isAdditiveOperator(self):
        operators = '^[+-]'
        return re.match(operators, self.__current_char) != None
    
    def __isMultiplicativeOperator(self):
        operators = '^\*$|^\/$|^\%$'
        return re.match(operators, self.__current_char) != None

    def __isExponentialOperator(self, operator):
        operators = '^\*\*$|^\/\/$'
        return re.match(operators, operator) != None

    def __isOpenParenthesis(self):
        paren = '[(]'
        return re.match(paren, self.__current_char) != None

    def __isClosingParenthesis(self):
        paren = '[)]'
        return re.match(paren, self.__current_char) != None

    def __advance(self):
        self.__position += 1
        if not self.__hasMoreTokens():
            self.__current_char = None
        else:
            self.__current_char = self.__expression[self.__position]
