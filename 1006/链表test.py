from typing import List

# 创建结点node
class Node:
    def __init__(self,data,next = None):
        # 创建结点注意两点:1.保存自己的数据data 2.告诉下一个元素next
        self.data = data
        self.next = None
    def __repr__(self):
        # 返回结点数据 将对象作为字符串输出
        return "Node({})".format(self.data)
        # return "Node(%s)"%(self.data)
# n = Node(3)
# print(n)

# 创建链表linkedlist
class linkedlist:
    def __init__(self):
        self.head = None
    # 头部(在头部插入一个结点)
    def insert_head(self,data):
        new_node = Node(data)
        if self.head: #如果头部不为空,将之前的头部作为下一个元素(新头部指向旧头部)
            new_node.next = self.head
        self.head = new_node #判断完之后对头部进行重新赋值,将插入的新数据作为头部
    # 尾部(在尾部追加一个结点)
    def append(self,data):
        if self.head: #如果头部不为空,遍历链表
            temp = self.head  # 从头部开始遍历,先将头部数据赋值给一个变量.记录头部
            while temp.next: # 下一个结点不为空
                temp = temp.next
            temp.next = Node(data) #遍历完之后,将链表最后一个结点指向添加的新结点
        else:
            self.insert_head(data) #如果头部为空,调用插入头部结点函数

    # 在中间任意位置插入一个结点(p为位置)
    def insert_mid(self,p,data):
        if self.head is None :
            self.insert_head(data)
        elif p == 1:
            self.insert_head(data)
        else:
            temp = self.head #先记录头部
            pre = temp #pre代表插入之前的结点
            j = 1 #记录往前移动的步数
            while j<p:
                pre = temp #pre代表插入之前的结点
                temp = temp.next #temp代表插入之后的结点
                j = j+1
            node = Node(data)
            pre.next = node
            node.next = temp

    # 将对象作为字符串输出
    def __repr__(self):
        current = self.head #记录头部
        s = ""
        while current:
            s += "{} -->".format(current)
            current = current.next
        return s + "End"

    # 传入列表直接生成链表
    def linklist(self,object:list):
        self.head = Node(object[0]) #列表的第一个元素作为头部
        temp = self.head #记录头部
        for i in object[1:]: #遍历列表除第一位元素之后的所有元素
            node = Node(i) #先生成一个新结点
            temp.next = node #上一个结点指向新结点
            temp = temp.next #将上一个结点下移

    #删除链表头部
    def delete_head(self):
        temp = self.head #记录头部
        if temp:
            self.head = temp.next #重置头部(也可用self.head = self.head.next)

    # 删除链表尾部
    def delete_tail(self):
        temp = self.head #记录头部
        if self.head: #如果头部不为空,进一步判断
            if temp.next is None: # 如果只有头部
                self.head = None
            else: # 如果结点有多个
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            print ("此为空列表")
    # 反转链表
    def reverse(self):
        prev = None #设置前一个结点
        current = self.head #记录链表头部
        while current:
            new_node = current.next #记录链表当前结点的下一个结点
            current.next = prev # 当前结点指向前一个结点
            prev = current # 前一个结点往前移一步
            current = new_node #当前结点往前移一步
        self.head = prev #重置头部
    # 得到第几个结点(查)
    def __getitem__(self,index):
        current = self.head
        if current is None:
            raise IndexError("The link is empty")
        else:
            for _ in range(1,index):
                if current.next is None:
                    raise IndexError("The index out of range")
                current = current.next
            return current
    # def get(self,index):
    # 将某一结点改变数据(改)
    def __setitem__(self, index,data):
        current = self.head
        if current is None:
            raise IndexError("The link is empty")
        else:
            for _ in range(1,index):
                if current.next is None:
                    raise IndexError("The index out of range")
                current = current.next
            current.data = data




#实例对象
link_list = linkedlist()

#调用方法
link_list.insert_head(1)
link_list.insert_head(2)
link_list.insert_head(3)
link_list.insert_head(4)
link_list.append(5)

# 打印输出结果
# print(link_list)

link_list.insert_mid(3,8)
print(link_list)

link_list.delete_head()
print(link_list)

link_list.delete_tail()
print(link_list)

link_list.reverse()
print(link_list)

print(link_list.__getitem__(3))

link_list.__setitem__(2,21)
print(link_list)

# a = [3,4,5,6,7,8]
# link_list.linklist(a)
# print(link_list)

