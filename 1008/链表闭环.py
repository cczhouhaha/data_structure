from typing import Optional
class Node:
    def __init__(self, data):
        self.value = data # 属性名= 属性值
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.value)

# 链表倒数第k个数
def LastK(head:Node,k):
    fast = head
    slow = head
    while k > 0:
        fast = fast.next
        k -= 1
    while fast:
        slow = slow.next
        fast = fast.next
    return slow,slow.value



#是否存在闭环  快慢指针
def is_circle(head:Node) -> bool:
    fast = head
    slow = head
    while fast and fast.next: # 无论结点奇数偶数个,均可进行判断
        fast = fast.next.next # None没有下一个结点,下一个结点可返回None
        slow = slow.next
        if fast == slow:
            return True
    return False

# 判断存在的入环点
# Optional 可选择的
def detect_circle_point(head: Optional[Node] = None):
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





# if main 主函数 代码执行入口
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = None

    print(is_circle(node1))

    # a = detect_circle_point(node1)
    # print(a)
    # print(detect_circle_point(node1))

    print(LastK(node1,3))



























