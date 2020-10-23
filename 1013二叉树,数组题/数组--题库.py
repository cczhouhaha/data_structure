from typing import List

# 两数之和
# 有序数组
# 方案一:指针对撞 (返回所有满足条件的元素)
nums1 = [1,2,3,4,5,6,7,8]
def TwoSums(nums:List,target):
    head = 0
    end = len(nums)-1
    while head < end:
        sum = nums[head] + nums[end]
        if sum == target:
            print([nums[head],nums[end]])
            head += 1
            end += 1
        else:
            if sum < target:
                head += 1
            else:
                end -= 1
TwoSums(nums1,8)
print("++++++++++++++++")
# 方案二:增加空间 (利用字典,返回满足所有条件的元素下标) 时间复杂度:nlogn
def TwoSums_dic(nums:List,target):
    nums_dic = {} #存放已遍历的下标和值
    for i in range(len(nums)):
        temp = target - nums[i] #记录目标值与遍历的元素之差
        if temp in nums_dic: #判断值是否在字典中  遍历key(key为值)
            print ([i,nums_dic[temp]]) #返回两数下标
        else:
            nums_dic[nums[i]] = i # 键值对: {值:下标}
TwoSums_dic(nums1,8)
print("++++++++++++++++")
# 方案三:暴力方法 直接双循环 (返回所有满足条件的元素)
def TwoSums3(nums:List,target):
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i] + j == target:
                print([nums[i],j])
            # else:
            #     return  False
TwoSums3(nums1,8)
print("++++++++++++++++")



# 无序数组 -->转变为有序数组

# 三数之和(无序数组) 循环+对撞指针 (对撞指针用在顺序数组里面)
def ThreeSum(nums:List):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum1 = nums[i] + nums[left] + nums[right]
            if sum1 < 0:
                left += 1
            elif sum1 > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res

# 合并两个有序数组 合并成一个有序数组
def mergin_twonum(nums1:List,m:int,nums2:List,n:int):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i > 0 and j > 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        if nums1[i] < nums2[j]:
            nums1[k] = nums1[k]
            j -= 1
        k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums1[j]
            j -= 1
            k -= 1
    return nums1

# 反转数组
def reverse(nums:List):
    head = 0
    end = len(nums)-1
    while head < end:
        nums[head],nums[end] = nums[end],nums[head]
        head += 1
        end -= 1
    return nums

# 有序数组实现二分查找
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




#用递归实现 (需要测试)
def search2(nums: List[int], target: int, start, end) -> int:
    if end > 0:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return search2(nums, target, start, mid - 1)
        else:
            return search2(nums, target, mid + 1, end)
    else:
        return -1







































