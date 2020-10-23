class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class link :
    def __init__(self):
        self.head = None
        self.tail = None
    def reverse(self):
        pre = None
        curr = self.head

        while curr:
            new_node = curr.next
            curr.next = pre
            pre = curr
            curr = new_node
        self.head = pre

#反转数组
from typing import List
def reverse(nums:List):
    head = 0
    end = len(nums)-1
    while head < end:
        nums[head],nums[end] = nums[end],nums[head]
        head += 1
        end -= 1
    return nums
nums1 = [1,2,3,4]
# print(reverse(nums1))


# 两两交换链表中的结点
def change(head):
    dummy = Node(0)
    pre = dummy
    curr = head
    while curr.next:
        temp = curr.next
        pre.next = temp
        curr.next = temp.next
        temp.next = curr
        curr = temp

def change1(head):
    dummy = Node(0)
    pre = dummy
    dummy.next = head
    while pre.next and pre.next.next:
        slow = pre.next
        fast = slow.next #pre.next.next
        pre.next = fast
        slow.next = fast.next
        fast.next = slow
        # pre = fast #不能用fast 因为fast指向发生变化
        pre = pre.next.next  #pre = fast //pre.next.next
    head = dummy.next
    # return dummy.next
    curr = head
    strs = ""
    while curr:
        strs += f"{curr}-->"
        curr = curr.next
    return strs + "End"
def output(head):
    curr = head
    strs = ""
    while curr:
        strs += f"{curr}-->"
        curr = curr.next
    return strs + "End"


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = None


print(output(node1))
# a=change1(node1)
print(change1(node1))



def threesums(nums:List,target):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        while i >0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            sum1 = nums[i] + nums[left] + nums[right]
            if sum1 < target:
                left += 1
            elif sum1 > target:
                right -= 1
            else:
                res.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return res

nums2 = [1,2,-3,4,5,-6,7,8,9]
# print(threesums(nums2,0))




