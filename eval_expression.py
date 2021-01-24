import re 
import ast 
import operator as op

#------------------------
#       Classes
#------------------------

# class Stack to build binary tree 
class Stack:

    def __init__(self):
        self.__list= []

    def isEmpty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def clear(self):
        self.__list.clear()

    def push(self, item):
        self.__list.append(item)

    def pop(self): # popTail
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()

    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]

    def __str__(self):
        output = '<'
        for i in range( len(self.__list) ):
            item = self.__list[i]
            if i < len(self.__list)-1 :
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output

# binary tree ( access function )
class BinaryTree:

    # constructor 
    def __init__(self,key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    # we are going to override the inherited __str__ function 
    # str function n preorder function will work together 
    def __str__(self):
        return self.preorder(0) # start from root (0) -> which is 0

    def preorder(self, level):
        output =  str(level*'-') + str(self.key) + '\n'
        if self.leftTree != None:
            output += self.leftTree.preorder(level+1) 

        if self.rightTree != None:
            output += self.rightTree.preorder(level+1) 

        return output 


    # access functions 
    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getLeftTree(self):
        return self.leftTree

    def getRightTree(self):
        return self.rightTree

    # insert functions
    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree

    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t =BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree

    # print function - expression tree
    def printPreorder(self, level):
        print(str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)

        if self.rightTree != None:
            self.rightTree.printPreorder(level+1) 

    def printInorder(self, level):
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
        #print( str(level*'-') + str(self.key))
        if self.rightTree != None:
            self.rightTree.printInorder(level+1) 


#--------------------------
#       Functions 
#--------------------------

# building a parse tree
def buildParseTree(exp):
    operators =r'(\*\*|\*|\+|\-|/|\(|\))'
    tokens = map(str.strip, re.split(operators, exp)) #split and strip spaces 
    tokens = list(filter(None, tokens)) # remove empty parts 

    print("tokens: ", tokens)

    print("Expression Tree: ")
    stack = Stack()
    tree = BinaryTree('?')
    stack.push(tree)
    
    #node
    currentTree = tree

    # process that breaks down each and every token (number, brackets, anything)
    for t in tokens:

        # RULE 1: If token is '(' add a new node as left child
        # and descend into that node
        if t == '(':
            currentTree.insertLeft('?')
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree() 

        # RULE 2: If token is operator set key of current node
        # to that operator and add a new node as right child
        # and descend into that node
        elif t in ['+', '-', '*', '**', '/']:
            currentTree.setKey(t)
            currentTree.insertRight('?')
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()

        # RULE 3: If token is number, set key of the current node
        # to that number and return to parent
        elif t not in ['+', '-', '*', '**', '/', ')'] :
            # accept integer and float 
            try:
                currentTree.setKey(int(t))
            except ValueError:
                currentTree.setKey(float(t))
            parent = stack.pop()
            currentTree = parent

        # RULE 4: If token is ')' go to parent of current node
        elif t == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree 

# Evaluate parse tree 
def evaluate(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()

    try:
        if leftTree != None and rightTree != None:
            if op == '+':
                return round(evaluate(leftTree) + evaluate(rightTree),2)
            elif op == '-':
                return round(evaluate(leftTree) - evaluate(rightTree),2)
            elif op == '*':
                return round(evaluate(leftTree) * evaluate(rightTree),2)
            elif op == '**':
                return round(evaluate(leftTree) ** evaluate(rightTree),2)
            elif op == '/':
                if evaluate(rightTree) != 0:
                    return round(evaluate(leftTree) / evaluate(rightTree),2)
                else:
                    print(f'{evaluate(leftTree)} cannot divide by 0, please try again.')
                    eval_expression()
        else:
            return tree.getKey()
    except TypeError:
        print('Seems like expression format is invalid. Please try again.\n')
        eval_expression()
          

def eval_expression():
    while True: 
        exp = input('Please enter expression: \n')

        try: 
            # empty input
            if len(exp) == 0: 
                print("Expression is empty. Please try again.\n")
            # expression doesn't starts and end with brackets 
            elif not exp.startswith('(') and not exp.endswith(')'):
                print('Invalid expression format. Please try again\n')
            # expression contains letters 
            elif re.search('[a-zA-Z]+',exp) is not None:
                print("Only integers/ float are allowed, please try again.\n")
            else:
                tree = buildParseTree(exp)
                tree.printPreorder(0)
                print(f'\nExpression evaluates to: \n{evaluate(tree)}')
                return False
                break
        except ValueError: 
            print('You entered invalid expression format. Please try again.\n')


# --------------------
#   Main Program 
# --------------------
# eval_expression()
