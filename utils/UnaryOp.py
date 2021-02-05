class UnaryOp():
    def __init__(self, key, rightTree):
        self.key = key
        self.rightTree = rightTree
    
    def __str__(self):
        return self.preorder(0) # start from root (0) -> which is 0


    def preorder(self, level):
        output =  str(level*'-') + '(' + str(self.key) + ')' + '\n'

        if self.rightTree != None:
            output += self.rightTree.preorder(level+1) 

        return output