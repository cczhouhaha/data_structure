from typing import List

# =====归并排序(先拆后合)========
def merge(left, right):
    p = 0
    q = 0
    res = []
    while p < len(left) and q < len(right):
        if left[p] < right[q]:
            res.append(left[p])
            p += 1
        else:
            res.append(right[q])
            q += 1
    res.extend(left[p:])
    res.extend(right[q:])
    return res
def merge1(left,right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res

def mergeSort(nums:List):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left,right = nums[:mid],nums[mid:]
    # return merge(mergeSort(left),mergeSort(right))
    return merge1(mergeSort(left),mergeSort(right))

nums1 = [3,8,3,2,7,5,1,9,5,6,4]
# print(mergeSort(nums1))
# ==========快速排序=================
def quickSort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i < pivot]
        greater = [i for i in nums[1:] if i >= pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
# print (quickSort(nums1))

def partition(nums,start,end):
    pivot = nums[start]
    p = start+1
    q = end
    while p <= q:
        while p <= q and nums[p] < pivot:
            p += 1
        while p <= q and nums[q] >= pivot:
            q -= 1
        if p < q:
            nums[p],nums[q] = nums[q],nums[p]
    nums[start], nums[q] = nums[q], nums[start]
    return q
def quickSort1(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quickSort1(nums,start,mid-1)
    quickSort1(nums,mid+1,end)
nums2 = [4,7,3,5,6,2,3,1]
quickSort1(nums2,0,len(nums2)-1)
# print (nums2)


# 快慢指针
# 删除指定元素
def remove(nums,target):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == target:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return nums[:slow]
num = [1,2,3,3,4,5,6,7]
# print(remove(num,3))
# 移动0
def move(nums,target):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == target:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow,len(nums)):
        nums[i] = 0
    return nums
num1 = [1,3,4,5,2,0,5,0,7,0,8]
# print(move(num1,0))
# 删除重复值
def deletere(nums):
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return nums[:slow+1]
num2 = [1,1,2,3,3,3,4,5,5,5,6,7]
print(deletere(num2))
# 删除重复值,允许有2个
def deletere2(nums):
    slow = 0
    fast = 1
    count = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            count += 1
            if count == 2:
                slow += 1
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            count = 1
            fast += 1
    return nums[:slow+1]
num3 = [1,1,2,2,2,3,3,3,4,4,5,6,7]
print(deletere2(num3))

