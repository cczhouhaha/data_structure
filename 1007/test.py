class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def get(self,index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr
    def insert(self,index,data):
        new_node = Node(data)
        if index<0 or index >self.size:
            return  "下标越界"
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index-1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
    def remove(self,index):
        if index <0 or index >= self.size:
            return "下标越界"
        elif self.size == 0 :
            return "空链表"
        elif index == 0:
            remove_node = self.head
            self.head = remove_node.next
            remove_node.next = None
        elif index == self.size-1:
            prev = self.get(index-1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = remove_node.next
            remove_node.next = None
        self.size -= 1
    def reversr(self):
        prev = None
        curr = self.head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev.next = curr
            curr.next = new_node
    def __repr__(self):
        curr = self.head
        llstr = ""
        while curr:
            llstr += f"{curr} -->"
            curr = curr.next
        return  llstr + "End"
    def __getitem__(self, index):
        curr = self.head
        if curr is None:
            return "空链表"
        while curr:
            if curr.next is None:
                return "超出范围"
            curr = curr.next
        return curr











