from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)})

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)


    def is_empty(self):
        if self.root is None:
            return True
        return False
    def __insert(self,data):
        new_node = Node(data,None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self,*values):
        for i in values:
            self.__insert(i)

    def search(self,data):
        if self.is_empty():
            raise Exception("The tree is empty")
        else:
            node = self.root
            while node and data != node.data:
                if data < node.data:
                    node = node.left
                else:
                    node = node.right
            return node
    def is_right(self,node):
        return node == node.parent.right

    def reassign(self,node,new_child):
        if new_child is not None:
            new_child.parent = node.parent
        elif node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child
    def remove(self,data):
        node = self.search(data)
        if node is not None:
            if node.left is None and node.right is None:
                self.reassign(node,None)
            elif node.left is None:
                self.reassign(node,node.right)
            elif node.right is None:
                self.reassign(node,node.left)
            else:
                temp = self.get_max(node.left)
                self.remove(temp.data)
                node.data = temp.data
        else:
            raise Exception("节点不存在")


    def get_max(self,node):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node

b = BST()
# b.insert(4)
# b.insert(3)
# b.insert(5)
# b.insert(6)
# b.insert(4)
# b.insert(1,2,3,4,5,6)
b.insert(5,3,5,2,6,4,7,6,8)
print(b)
aa = b.search(6)
print(aa)
b.remove(6)
print(b)