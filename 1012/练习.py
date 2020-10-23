class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

def merge_twolinks(l1:Node,l2:Node):
    dummy = Node(0)
    curr = dummy
    while l1 or l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        if l1 is None:
            curr.next = l2
            break  #用or的话,一定加break
        if l2 is None:
            curr.next = l1
            break #用or的话,一定加break
    return dummy.next

def merge_twolink(l1:Node,l2:Node):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 =l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1 is None:
        curr.next = l2
    if l2 is None:
        curr.next = l1
    return dummy.next

def output(head:Node):
    curr = head
    llstr = ""
    while curr:
        llstr += f"{curr}-->"
        curr = curr.next
    return llstr + "End"




if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    node5 = Node(1)
    node6 = Node(3)
    node7 = Node(3)
    node8 = Node(6)
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = None

    # a = merge_twolinks(node1,node5)
    # b = merge_twolink(node1,node5)
    # print(a)
    # print(b)
    # print(output(a))
    # print(output(b))
    # print(output(node1))


#用数组实现栈
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self,data):
        self.stack.append(data)
        self.size += 1
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.size -= 1
        else:
            raise Exception("The stack is empty")
    def peek(self):
        temp = self.stack[-1]
        return temp
# 用链表实现栈
class LinkStack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.top = new_node
        else:
            raise Exception("The stack is empty")
    def pop(self):
        if self.top is None:
            raise Exception("The stack is empty")
        else:
            temp = self.top
            self.top = temp.next
















