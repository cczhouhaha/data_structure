class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        # return "Node({})".format(self.data)
        # return ""
        return f"Node({self.data})"


class linkedlist:
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
        if index <0 or index > self.size:
            return "下标越界"
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head =  new_node
        elif index == self.size -1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index-1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
    def remove(self,index):
        if index<0 or index>=self.size:
            return"下标越界"
        elif self.size ==0:
            return "空列表"
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
            prev = self.get(index-1)
            remove_node = prev.next
            prev.next = remove_node.next
            remove_node.next = None
            self.size -= 1
            return remove_node.data












    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = None
            prev = current
            current = new_node
        self.head = prev
    def __getitem__(self, index):
        current = self.head
        if current is None:
            raise IndexError("The link is empty")
        for _ in range(1,index):
            if current.next is None:
                raise IndexError("The index out of range")
            current = current.next
        return current
    def __setitem__(self,index,data):
        current = self.head
        if current is None:
            raise IndexError("The link is empty")
        for _ in range(1,index):
            if current.next is None:
                raise IndexError("The index out of range")
            current = current.next
        current.data = data




