from typing import List
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)


class linkedlist:
    def __init__(self):
        self.head = None
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
            temp.next = Node(data)
        else:
            self.insert_head(data)


    def insert_mid(self,p,data):
        if self.head is None or p == 1:
            self.insert_head(data)
        else:
            temp = self.head
            pre = temp
            j = 1
            while j <p:
                pre = temp
                temp = temp.next
                j = j+1
            node = Node(data)
            pre.next = node
            node.next = temp
    def linklist(self,object:list):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next
    def __repr__(self):
        current = self.head
        str = ""
        while current:
            str += "{}-->".format(current)
            current = current.next
        return str + "End"

    def delete_head(self):
        temp = self.head
        if temp:
            self.head = temp.next


    def delete_tail(self):
        temp = self.head
        if temp:
            if temp.next is None:
                temp = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            print("此为空链表")


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

link_list.delete_head()
print(link_list)

link_list.delete_tail()
print(link_list)