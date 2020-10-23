from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)})
class BST:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)









