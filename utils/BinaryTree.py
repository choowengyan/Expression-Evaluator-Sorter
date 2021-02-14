# -------------------------------------------------|
# ST1507 DSAA CA2 : Expression Evaluator & Sorter  |
# -------------------------------------------------|
# Name  : Silviana (1939213)                       |
#       : Choo Weng Yan (1940208)                  |
# Class : DIT/FT/2B/14                             |
# -------------------------------------------------|


# Evaluating Expression & Sorting Expression 

class BinaryTree:
    # constructor 
    def __init__(self, key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    # str function n preorder function will work together 
    def __str__(self):
        return self.preorder(0) # start from root (0) -> which is 0

    def preorder(self, level):
        output =  str(level*'-') + '(' + str(self.key) + ')' + '\n'
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
            t = BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree

    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree

    # print function - expression tree
    def printPreorder(self, level):
        print(str(level * '-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1) 

    def printInorder(self, level):
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)
        print(str(level * '-') + str(self.key))
        if self.rightTree != None:
            self.rightTree.printInorder(level+1) 

    def printPostorder(self, level):
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1) 
        if self.rightTree != None:
            self.rightTree.printPostorder(level+1) 
        print(str(level * '-') + str(self.key))

    def prettyPrint(self, level):
        print("\t\ta")
        print(len("\t\ta"))

