# -------------------------------------------------|
# ST1507 DSAA CA2 : Expression Evaluator & Sorter  |
# -------------------------------------------------|
# Name  : Silviana (1939213)                       |
#       : Choo Weng Yan (1940208)                  |
# Class : DIT/FT/2B/14                             |
# -------------------------------------------------|

'''
Evaluating Expression and Sorting Expression
'''

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return 'Token(type: {}, value: {})'.format(self.type, self.value)