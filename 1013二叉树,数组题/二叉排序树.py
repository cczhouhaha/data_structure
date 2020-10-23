# 二叉排序树（Binary Sort Tree），又称二叉查找树（Binary Search Tree），亦称二叉搜索树。
# 是数据结构中的一类。在一般情况下，查询效率比链表结构要高
from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.value = data
        self.parent = parent #设置父节点参数
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s"%(self.value):(self.left,self.right)},indent=1) # {根节点:左右孩子}

class BST:
    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    def __str__(self):  #打印输出函数
        return str(self.root) #根据根节点 返回树

    def __insert(self,value): #私有函数
        new_node = Node(value,None) #记录新结点
        if self.is_empty(): #首先判断tree是否为空
            self.root = new_node
        else:
            parent_node = self.root #若tree不为空,先记录根节点
            while True: #判断条件为True
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break #如果插入,立即跳出循环
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node #循环结束之后,为插入的新结点找到父节点

    def insert(self,*values): #可放多个参数
        for i in values:
            self.__insert(i) #调用私有函数

    def search(self,value):
        if self.is_empty():
            raise  Exception("The tree is empty")
        else:
            node = self.root #先记录根节点
            while node and (node.value != value): #如果node不为空,并且值不是所需要的,进行二分搜索
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right
            # print(node)
            return node #如果node是跟结点,会返回左右孩子

    def is_right(self,node):
        return node == node.parent.right

    # 重置父节点和左右孩子 (删除结点时调用)
    def reassign(self,node,new_children): #传入一个结点,以及新的孩子(重置节点以及孩子)
        if new_children is not None: #如果孩子不为空,为孩子找父节点
            new_children.parent = node.parent
        if node.parent is not None: #如果父节点不为空,为父节点找孩子(找孩子需要判断是左右结点)
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else: #针对node结点为空的状况
            self.root = new_children #针对结点为空的情况
    # 删除结点
    def remove(self,value):
        node = self.search(value) #利用search函数找到需要需要删除值所在tree中的节点
        if node is not None: #如果找到该节点,进行删除操作
            if node.left is None and node.right is None: # 如果左右孩子都为空,调用重置结点函数
                self.reassign(node, None)
            elif node.left is None: #如果左孩子为空
                self.reassign(node,node.right)
            elif node.right is None: #如果右孩子为空
                self.reassign(node,node.left)
            else: #如果左右孩子都存在
                temp = self.get_max(node.left) #先得到左边最大的节点,并且记录
                self.remove(temp.value) #然后删除最大节点
                node.value = temp.value #对所需要删除的值进行重新赋值,相当于删掉
        else:
            raise Exception("The tree is empty")

    def get_max(self,node):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right: #注意循环条件
                node = node.right
        return node

    def get_min(self,node):
        if node is None:
            node = self.root
        if self.root:
            node = self.root
            while node.left:
                node = node.left
        return node

    # 前序遍历(根左右) #递归实现
    def pre(self,node):
        if not node: #if node is None
            return None
        else:
            print(node.value,end = '-->')
            self.pre(node.left)
            self.pre(node.right)
    #前序遍历  用栈实现
    def preOrder(self,node):
        stack = [node]
        while len(stack) > 0 :
            print(node.value,end="-->")
            if node.right: #先存入右孩子(先进后出)
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    # 中序遍历(左根右) 用递归实现
    def inOrder(self, node):
        if not node:  # if node is None
            return None
        else:
            self.inOrder(node.left)
            print(node.value, end='-->')
            self.inOrder(node.right)
    #中序遍历  用栈实现
    def inOrder1(self,node):
        stack = []
        while node or len(stack) > 0:
            while node: #先收集左侧
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop() #按顺序弹出,并收集右侧
                print(node.value,end="-->")
                node = node.right

    # 后序遍历(左右根) 用递归实现
    def postOrder(self, node):
        if not node:  # if node is None
            return None
        else:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value, end='-->')
    # 后序遍历(左右根)用栈实现
    def postOrder1(self,node):
        if node is None:
            return False
        else:
            stack1 = []
            stack2 = []
            stack1.append(node)
            while stack1:
                node = stack1.pop()
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
                stack2.append(node)
            while stack2:
                node = stack2.pop()
                print(node.value,end="-->")

    def cengOrder(self,node):
        if self.root is None:
            return False
        else:
            res = [self.root]
            while res:
                node = res.pop(0)
                print(node.value,end="-->")
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)



    def levelOrder(self,node):
        from queue import Queue
        queue = Queue()
        queue.put(node)
        while not queue.empty():
            node = queue.get()
            print(node.value,end="-->")
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)



b = BST()
# b.insert(4)
# b.insert(3)
# b.insert(5)
# b.insert(6)
# b.insert(4)
# b.insert(1,2,3,4,5,6)
b.insert(8,3,10,1,6)
print(b)
aa = b.search(8)
# print(aa)
# b.remove(5)
# print(b)

b.pre(aa)
print("End")

b.preOrder(b.root)
print("End")

b.inOrder(b.root)
print("End")

b.inOrder1(b.root)
print("End")

b.postOrder1(b.root)
print("End")
b.postOrder(b.root)
print("End")

b.levelOrder(b.root)
print("End")

b.cengOrder(b.root)
print("End")