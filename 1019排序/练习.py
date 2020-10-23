from pprint import pformat

def cheng(n):
    if n <= 2 :
        return n
    return cheng(n-1) * n

# print(cheng(5))

def function(n):
    if n <= 2:
        return n
    return  function(n-2) + function(n-1)

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
    def reassign(self,node,new_child):
        if new_child is not None:
            new_child.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child

    def is_right(self, node):
        return node == node.parent.right

    #遍历
    #前序遍历 (根左右) 递归实现
    def preOrder(self,node):
        if node is None:
            return None
        else:
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)
    #前序遍历用栈实现
    def preOrder1(self,node):
        stack = [node]
        while len(stack) > 0:
            print(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            node = stack.pop()
    #中序遍历用栈实现 (左根右)
    def inOrder(self,node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()  # 按顺序弹出,并收集右侧
                print(node.value, end="-->")
                node = node.right

class priortyQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def __repr__(self):
        return str(self.array)

    def insert(self,data):
        self.array.append(data)
        self.size += 1
        self.heapfiy_up()

    def heapfiy_up(self):
        index = len(self.array) - 1
        parent_index = (index - 1) >> 1
        temp = self.array[index]
        while index > 0 and self.array[parent_index] < temp:
            # self.array[index] = self.array[parent_index]
            self.array[index],self.array[parent_index] = self.array[parent_index],self.array[index]
            index = parent_index
            parent_index = (index - 1) >> 1
        self.array[index] = temp

    def remove(self):
        remove_node = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapfiy_down()
        return remove_node

    def heapfiy_down(self):
        index = 0
        total_index =len(self.array) - 1
        maxvalue_index = index
        while True:
            # maxvalue_index = index
            if 2 * index + 1 <= total_index and self.array[maxvalue_index] < self.array[2 * index + 1]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.array[maxvalue_index] < self.array[2 * index + 2]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.array[index], self.array[maxvalue_index] = self.array[maxvalue_index], self.array[index]
            index = maxvalue_index


pq = priortyQueue()
pq.insert(5)
pq.insert(6)
pq.insert(10)
pq.insert(8)
pq.insert(3)
pq.insert(4)
pq.insert(3)
pq.insert(5)
pq.insert(9)
print(pq)

# print(pq.remove())

pq.remove()
print(pq)









