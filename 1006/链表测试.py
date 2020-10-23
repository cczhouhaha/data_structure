from typing import List

# 1.创建结点
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)
# 2.创建链表
class linkedlist:
    def __init__(self):
        self.head = None

    #增(链表的方法:头部,尾部,中间)
    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
    def append(self,data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next =Node(data)
        else:
            self.insert_head(data)
    def insert_mid(self,p,data):
        if self.head is None:
            self.insert_head(data)
        elif p == 1:
            self.insert_head(data)
        else:
            temp = self.head
            pre = temp
            j = 1
            while j<p:
                pre = temp
                temp = temp.next
                j = j+1
            node = Node(data)
            pre.next = node
            node.next = temp
    # 将对象作为字符串输出
    def __repr__(self):
        current = self.head
        str = ""
        while current:
            str += "{}-->".format(current)
            current = current.next
        return str + "End"
    # 列表转链表
    def linklist(self,object:list):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next
    # 删:头部,尾部
    def delete_head(self):
        temp = self.head
        if temp:
            self.head =temp.next
    def delete_tail(self):
        temp = self.head
        if self.head:
            if temp.next is None:
                temp = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            print("为空链表")



#实例对象
link_list = linkedlist()
#调用方法
link_list.insert_head(1)
link_list.insert_head(2)
link_list.insert_head(3)
link_list.insert_head(4)
link_list.append(5)
# 打印输出结果
print(link_list)

link_list.insert_mid(3,8)
print(link_list)

a = [3,4,5,6,7,8]
link_list.linklist(a)
print(link_list)

link_list.delete_head()
print(link_list)

link_list.delete_tail()
print(link_list)




