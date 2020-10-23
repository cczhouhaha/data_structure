
# 队列先进先出
# 用数组实现队列
class Queue:
    def __init__(self):
        self.entrise = [] #entrise
        self.size = 0
    def __repr__(self):
        printed = "<" + str(self.entrise)[1:-1] + ">"
        return printed
    def enqueue(self,data):
        self.entrise.append(data)
        self.size += 1
    def dequeue(self): #先进先出 去掉第一个元素
        if self.entrise:
            temp = self.entrise[1]
            self.entrise = self.entrise[1:]
            self.size -= 1
            return temp
        else:
            raise Exception("The queue is empty")
    def get(self,index):
        if index < 0 or index >= self.size:
            raise Exception("The index out of range")
        else:
            temp = self.entrise[index]
            return temp
    def set(self,index,data):
        if index < 0 or index >= self.size:
            raise Exception("The index out of range")
        else:
            self.entrise[index] = data
    def inverse1(self):
        self.entrise.reverse()
    def inverse2(self):
        self.entrise = self.entrise[-1::-1]



# qq = Queue()
# qq.enqueue(1)
# qq.enqueue(2)
# qq.enqueue(3)
# qq.enqueue(4)
# print(qq)
# qq.dequeue()
# print(qq)
# print(qq.get(2))
# qq.set(2,9)
# print(qq)
# qq.inverse1()
# print(qq)
# qq.inverse2()
# print(qq)

# print(r)
# print(qq.enqueue(2))
# print(qq.enqueue(3))
# print(qq.enqueue(4))




# 用链表实现队列(先进先出)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class LinkQueue:
    def __init__(self):
        self.head = None  #front
        self.tail = None  #rear
        self.size = 0
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None: # if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
    def is_empty(self):
        return self.head is None
    def __repr__(self):
        curr =  self.head
        enstr = ""
        while curr:
            enstr += f"{curr} ->"
            curr = curr.next
        return enstr + "End"
    def dequeue(self): #先进先出 删除头结点
        if self.head is None:
            raise Exception("The linkqueue is empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.size -= 1
        return temp
    def get(self,index):
        if index< 0 or index > self.size:
            raise Exception("The index out of range")
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr



lq = LinkQueue()
lq.enqueue(3)
lq.enqueue(4)
lq.enqueue(5)
lq.enqueue(6)
lq.enqueue(7)
print(lq)
a = lq.dequeue()   #函数里面有return,需要用变量接收,然后打印变量
print(a)
lq.dequeue() #若想打印整个队列,不需要用变量接收,直接调用函数,然后打印对象,利用类里面的repr打印返回值
print(lq)
b = lq.get(1)   #函数里面有return,需要用变量接收,然后打印变量
print(b)
# if __name__ == '__main__':








