class Array:
    def __init__(self,capacity):
        self.Array = [None] * capacity
        self.size = 0

    def __repr__(self):
        return f"{self.Array}"


    def insert(self,index,element):
        if index<0:
            raise IndexError ("下标越界")
        if self.size >= len(self.Array) or index >= len(self.Array):
            self.addcapacity()
        else:
            for i in range(self.size-1,index-1,-1):
                self.Array[i+1] = self.Array[i]
            self.Array[index] = element
            self.size += 1
    def addcapacity(self):
        new_array = [None] * len(self.Array) * 2
        for i in range(len(self.Array)):
            new_array[i] = self.Array[i]
        self.Array = new_array
    def remove(self,index):
        if index<0 or index >= self.size:
            raise IndexError("下标越界")

        else:
            for i in range(index,self.size):
                self.Array[i] = self.Array[i+1]
            self.size -= 1

    # def addcapacity(self):
    #     new_array = [None] * len(self.Array) * 2
    #     for i in range(len(self.Array)):
    #         new_array[i] = self.Array[i]
    #     self.Array = new_array




if __name__ == '__main__':
    aa = Array(5)
    print(aa)
    aa.insert(0,1)
    print(aa)




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def  __repr__(self):
        return "Node({})".format(self.data)

def is_circle(head:Node):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
def CirclePoint(head:Node):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == '__main__':
    node1 =  Node(1)
    node2 =  Node(2)
    node3 =  Node(3)
    node4 =  Node(4)
    node5 =  Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3

    # print(is_circle(node1))
    # print(CirclePoint(node1))



