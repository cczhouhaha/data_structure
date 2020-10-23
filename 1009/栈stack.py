
# 用数组(形式与列表类似)实现栈
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self,data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise IndexError("The stack is empty")
        return temp
    # def __repr__(self):
    #     return f"{self.stack}"
    def __str__(self):
        return str(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[-1]
    def sizes(self):
        return self.size
    def is_empty(self):
        return not bool(self.stack)


# s = Stack()
# s.push(2)
# for i in range(10):
#     s.push(i)
# print(s)
# s.pop()
# print(s)
# print(s.peek())
# print(s.size) #调用方法不加括号
# print(s.sizes())




# 用链表实现栈.每插入一个节点便是栈顶.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"


class LinkStack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top #每插入一个节点便是栈顶.
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self): #栈顶是最后插入的一个数,因此删除最后一个数便是删除栈顶
        if self.top is None:
            raise IndexError("Pop from empty stack")
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
        return temp.data

    def __repr__(self):
        current = self.top
        llstr = ""
        while current:
            llstr += f"{current}-->"
            current = current.next
        return llstr + "End"



    # def __repr__(self):
    #     return

ls = LinkStack()
ls.push(2)
print(ls)

for i in range(10):
    ls.push(i)
print(ls)

print(ls.pop())
a = ls.pop()
print(a)



