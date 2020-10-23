from typing import List
from randomList import randomList
#====从小到大==========
#=======冒泡排序===========
def bubble(nums:List):
    for i in range(len(nums)-1): #每一次循环将最大值排到最后
        for j in range(len(nums)-i-1): #之前排过的最大值不需再次排列
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        # print("第%s轮排序结果:"%(i+1),end=" ")
        # print(nums)
    return nums
# nums1 = [4,6,7,5,3,2,10,8,7,4,5,11,14,15]
a = randomList.randomList(10)
# print(bubble(a))
#=======选择排序============
#选择排序 (将列表中的每一个元素和后面所有的元素比较,如果前面的元素比后面的元素大,则交换两个元素位置)
def selectSort(nums:List):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums
b = randomList.randomList(9)
# print(selectSort(b))
#(将列表中的每一个元素和后面所有的元素比较,如果前面的元素比后面的元素大,则交换两个元素位置)
def selectSort1(nums:List):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[min_index],nums[i] = nums[i],nums[min_index]
    return nums
c = randomList.randomList(8)

#(将列表中的每一个元素和后面所有的元素比较,如果前面的元素比后面的元素大,则交换两个元素位置)
def selectionSort(iList: List[int]) -> List:
    if len(iList) <= 1:
        return iList
    for i in range(len(iList)-1):
        minindex = i
        for j in range(i+1, len(iList)):
            if iList[j] < iList[minindex]:
                minindex = j
        iList[i], iList[minindex] = iList[minindex],iList[i]
        print("第{}轮排序结果".format(i), end="")
        print(iList)
    return iList

# print(selectSort1(b))

# hui("adb")
#======插入排序===========
# 插入排序 一个序列分为左右两部分:左边是已经排好序的,右边是待排序的
def insertSort(nums:List):
    length = len(nums)
    if length <= 1:
        return nums
    for right in range(1,len(nums)): #外层循环为未排序的
        target = nums[right]
        for left in range(0,right):#内层循环为已经排好的 (将外层中每一个元素与内层已排好的元素进行对比)
            if nums[left] > target:
                nums[left+1:right+1] = nums[left:right]
                nums[left] = target
                break
    return  nums

s = randomList.randomList(8)
# print(s)
# print(insertSort(s))

# ===链表插入排序=====

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
def insertSortList(head:Node):
    dummy = Node(0)
    pre = dummy
    curr = head
    while curr:
        temp = curr.next
        while pre.next and pre.next.data < curr.data:
            pre = pre.next
        curr.next = pre.next
        pre.next = curr
        curr = temp
        pre = dummy
    return dummy.next

def output(head):
    curr = head
    strs = ""
    while curr :
        strs += f"{curr}-->"
        curr = curr.next
    return strs + "End"
if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(4)
    node4 = Node(2)
    node5 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    # print(output(node1))
    # a = insertSortList(node1)
    # print(output(a))







