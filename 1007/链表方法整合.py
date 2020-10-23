class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        # return "Node({})".format(self.data)
        # return ""
        return f"Node({self.data})"


# 链表方法整合

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 获得某一个结点(index从0开始)
    def get(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr
    def set(self,index,data):
        set_node = Node(data)
        set_node = self.get(index)
        return set_node

    # 插入
    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("下标越界")
        else:
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
            elif index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index == self.size:
                self.tail.next = new_node
                self.tail = new_node
            else:
                prev = self.get(index - 1)
                new_node.next = prev.next
                prev.next = new_node
            self.size += 1

    def __repr__(self):
        current = self.head
        llstr = ""
        while current:
            llstr += f"{current}-->"
            current = current.next
        return llstr + "End"

    # 删除(遇到return以及错误后面的程序不执行)
    def remove(self, index):
        remove_node = self.get(index)
        if index < 0 or index >= self.size:
            raise Exception("下标越界")
        if self.size == 0:
            return"空链表"
        elif index == 0:
            remove_node = self.head
            self.head = remove_node.next
            remove_node.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = remove_node.next
            remove_node.next = None
        self.size -= 1
        return remove_node.data

    # 反转链表
    def reverse(self):
        prev = None
        curr = self.head
        self.tali = curr
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        self.head = prev

    #是否存在闭环
    def is_curcle(head):
        prev = head
        curr = head
        while curr and curr.next:
            curr = curr.next.next
            prev = prev.next
            if prev == curr:
                return True
        return False






    # 找到倒数第K个元素
    def reversek(self,k):
        index = self.size - k
        get_node = self.get(index)
        return get_node



ll = linkedlist()
ll.insert(0, 1)
ll.insert(1, 2)
ll.insert(2, 3)
ll.insert(2, 1)
ll.insert(4, 4)
print(ll)
print(ll.remove(2))

ll.reverse()
print(ll)

# print(ll.get(2))
# a=ll.reversek(1)
# print(a)

print(ll.is_curcle())


