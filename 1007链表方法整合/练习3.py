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





    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev
