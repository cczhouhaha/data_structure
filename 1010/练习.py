from typing import List
# 有序数组去重
# 1.去重
nums1 = [1,1,1,1,2,3]
# 方案一:利用切片
def remove_re(nums:List):
    n = len(set(nums))
    i = 0
    while i < n-1:
        if nums[i] == nums[i+1]:
            temp = nums[i+1]
            nums[i+1:len(nums)-1] = nums[i+2:]
            nums[-1] = temp
        else:
            i = i+1
    return i + 1,nums[:i+1]


# 方案二:利用快慢指针
nums11 = [1,1,1,1,2,3]
def remove_rep(nums:List):
    fast = 1
    slow = 0
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1,nums[:slow+1]


nums2 = [1,1,2,2,3,4,5,6,6,6,6,7,7]
# 2.去重保留2个相同
def remove_re2(nums:List):
    fast = 1
    slow = 0
    count = 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            count += 1
            if count == 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            count = 1
            fast += 1
        # fast += 1
    return slow+1 ,nums[:slow+1]


nums3 = [0,0,3,4,2,1,0,5]
# 3.移动0
def move_zero(nums:List):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow,len(nums)):
        nums[i] = 0
    return slow,nums


nums4 = [1,1,1,1,2,3,4,5,6,7,5,4,3]
# 4.删除特定值
def remove_value(nums:List,value):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == value:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return slow,nums[:slow]


print(remove_re(nums1))
print(remove_rep(nums11))
print(remove_re2(nums2))
print(move_zero(nums3))
print(remove_value(nums4,4))



# 栈
# 用数组实现栈
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self,data):
        self.stack.append(data)
        self.size += 1
    def pop(self):
        if self.stack is None:
            raise Exception ("The stack is empty")
        else:
            self.stack.pop()
            self.size -= 1
    def peek(self):
        if self.stack is None:
            raise Exception ("The stack is empty")
        else:
            temp = self.stack[-1]
            return temp
    def __str__(self):
        return str(self.stack)

# 用链表实现栈
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
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    def pop(self):
        if self.top is None:
            raise Exception("The stack is empty")
        else:
            temp = self.top
            self.top = temp.next
            temp.next =  None
        return temp







