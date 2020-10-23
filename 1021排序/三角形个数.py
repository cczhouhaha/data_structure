from typing import List
def triangle(nums:List):
    nums.sort()
    count = 0
    for i in range(len(nums)-2):
        left = i+1
        right =len(nums)-1
        while left < right:
            if nums[i] + nums[left] <= nums[right]:
                right -= 1
            else:
                count += right-left
                left += 1
                right = len(nums) - 1
    return count


num1 = [24,3,82,22,35,84,19]
# print(triangle(num1))




#滑动窗口



# 合并两个有序数组  使用新的空列表进行接收 倒叙
# def merginTwo(l1:List,m:int,l2:List,n:int):








