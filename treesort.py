#from builtins import None


class Node:
    def __init__(self): # sets up a Node with all variable none
        self.value = None
        self.left = None
        self.right = None

    def addItem(self,value):
        if self.value == None:  # if value not set for this node
            self.value = value  # use that value
        elif value < self.value:    # if the value is less than this node
                                    # add on left
            if self.left==None:     # if left node does not exist
                self.left = Node()  # make it
            self.left.addItem(value) # add item on the left
        else:
            if self.right==None:
                self.right=Node()
            self.right.addItem(value)

    def printTree(self):
        if self.left != None:
            self.left.printTree()
        print(self.value,end=', ')
        if self.right != None:
            self.right.printTree()
        
        
            
        
data = [12,15,7,8,20,14]

rootNode = Node()   # The base of the tree

for item in data:
    rootNode.addItem(item)
    
rootNode.printTree()