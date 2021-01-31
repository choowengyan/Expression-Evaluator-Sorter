import re 
import ast 
import operator as op
from itertools import accumulate
from Stack import Stack
from BinaryTree import BinaryTree

#--------------------------
#       Functions 
#--------------------------

# building a parse tree
def buildParseTree(exp):
    #operators =r'(\*\*|\*|\+|\-|/|\(|\))'
    operators =r"(\*\*|\*|\+|\-|\/|\(|\))"
    tokens = map(str.strip, re.split(operators, exp)) #split and strip spaces 
    tokens = list(filter(None, tokens)) # remove empty parts 

    print("tokens: ", tokens)

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

    # validate()
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
        # print(exp)
        #validate user input expression 
        try: 
            # empty input
            if len(exp) == 0: 
                print("Expression is empty. Please try again.\n")
            # expression doesn't starts and end with brackets 
            elif not exp.startswith('(') or not exp.endswith(')'):
                print('Invalid expression format. Please try again\n')
            # expression contains letters 
            elif re.search('[a-zA-Z]+',exp) is not None:
                print("Only integers/ float are allowed, please try again.\n")
            else:
                tree = buildParseTree(exp)
                # validate(exp)
                # printTree()
                
                _tree = True 
                while _tree:
                    # while True:
                    print('\nPlease choose the way of transversing the Expression Tree:')
                    print('1. Inorder Traversal\n2. Preorder Traversal\n3. Postorder Traversal\n')

                    traversal = input('Your choice: ')

                    if traversal == '1':  
                        print('\nExpression Tree (Inorder Traversal): ')
                        tree.printInorder(0) 
                        _tree = False
                    elif traversal == '2':
                        print('\nExpression Tree (Preorder Traversal): ')
                        tree.printPreorder(0)
                        _tree = False
                    elif traversal == '3':
                        print('\nExpression Tree (Postorder Traversal): ')
                        tree.printPostorder(0)
                        _tree = False
                    else:
                        print("Invalid input, please try again\n")
                # tree.printPreorder(0)
                print(f'\nExpression evaluates to: {evaluate(tree)}\n')
                return False
                break
        except ValueError: 
            print('You entered invalid expression format. Please try again.\n')


def validate(exp):
    tokens   = buildParseTree(exp)
    error    = ""
    pLevel   = 0

    for errorPos,token in enumerate(tokens):
        pLevel += (part=="(")-(part==")")
        if pLevel<0: 
            error="too many closing parentheses";break
        if part in ["**","*","+","-","/","(",")"]: 
            continue
        if all(p.isdigit() for p in part.split(".",1)): 
            continue
        error = "invalid operand: " + part
        break
    if not error and pLevel!=0:
        errorPos,error = len(parts),"unbalanced parentheses"
    if error:
        print("".join(parts))
        indent = " " * sum(map(len,parts[:errorPos]))
        print(indent+"^")
        print(indent+"|__ Error!",error)
            

# --------------------
#   Main Program 
# --------------------
# eval_expression()
