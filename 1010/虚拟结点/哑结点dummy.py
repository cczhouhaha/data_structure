# 链表相关操作
# 删除某结点
# 虚拟结点:将头结点当做普通结点看待
"""
:Author:Miss zhou
:Creat : 2020/10/10 11:09

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"


class Slution:
    def __init__(self):
        self.head = None

    # 删除链表中的特定值
    def delete_element(self,head:Node,value):
        dummy = Node(0) #先设置一个虚拟变量,且将其指向原来的头结点
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.data == value:
                curr.next = curr.next.next
            else:
                curr = curr.next
        self.head = dummy.next  #此步用在repr中,重新定义头部,打印输出
        return dummy.next #返回头结点

    # 链表结点两两交换
    def change_paris(self,head:Node):
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            # 指针上岗
            slow = prev.next
            fast = prev.next.next
            # 交换位置
            prev.next = fast
            slow.next = fast.next
            fast.next = slow
            # perv前移
            prev = prev.next.next
        self.head = dummy.next #此步用在repr中,重新定义头部,打印输出
        return dummy.next  # 返回头结点
    # 合并两个有序链表  1.and方法
    def merge_twolink(self,l1:Node,l2:Node):
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
        self.head = dummy.next #此步用在repr中,重新定义头部,打印输出
        # return dummy.next
        # def __repr__(self):
        #     current = self.head
        #     llstr=""
        #     while current:
        #         llstr += f"{current}-->"
        #         current = current.next
        #     return llstr + "End"

    # 合并两个有序链表  2.or方法  若是其中一个链表是空的,将后两个if判断提前.
    def merge_twolinks(self,l1: Node, l2: Node):
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
                break  # 用or的话,一定加break
            if l2 is None:
                curr.next = l1
                break  # 用or的话,一定加break
        return dummy.next


def output(head:Node):
    curr = head
    # llstr = ""
    while curr:
        # llstr += f"{curr.data}-->"
        print(curr.data)
        curr = curr.next


ss = Slution()
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

    # print(ss.delete_element(node1,3))
    # print(ss)

    # print(ss.change_paris(node1))
    # print(ss)

    # print(ss.merge_twolink(node1,node5))
    # print(ss)

    m=ss.delete_element(node1, 3)
    print(m)
    output(m)

    # output(node1)

    # print(a)
    # print(output(a))






