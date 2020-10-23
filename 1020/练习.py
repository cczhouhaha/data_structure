from typing import List
import random

#冒泡排序
def bubbleSort(nums:List):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

#选择排序
def selectionSort(nums):
    for i in range(len(nums)-1):
        minindex = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minindex]:
                minindex = j
        nums[i], nums[minindex] = nums[minindex],nums[i]
    return nums

def randomList(n):
    randomList = []
    for i in range(n):
        randomList.append(random.randint(1,100))
    return randomList

# a = randomList(10)
# print(a)
#   head = 0
#     end = len(nums)-1
#     while head < end:
#         if nums[head] == value:
#             return head
#         elif nums[end] == value:
#             return end
#         else:
#             mid = (head + end) // 2
#             if value > nums[mid]:
#                 head = mid
#             if value < nums[mid]:
#                 end = mid


# 有序数组二分查找
def search(nums,value):
    head = 0
    end = len(nums)-1
    while head < end:
        if nums[head] == value:
            return head
        elif nums[end] == value:
            return end
        else:
            mid = (head + end) // 2
            if value > nums[mid]:
                head = mid
            if value < nums[mid]:
                end = mid
nums1 = [1,2,3,4,5,6,7,8,9]
# print(search(nums1,6))


def BinarySearch(nums:List,value):
    head = 0
    end = len(nums)-1
    while head < end:
        if nums[head] == value:
            return head
        elif nums[end] == value:
            return end
        else:
            mid = (head + end) // 2
            if value > nums[mid]:
                head = mid
            if value < nums[mid]:
                end = mid
            else:
                return mid

print(BinarySearch(nums1,8))


