from typing import  List
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    res = []
    minval = abs(nums[0] + nums[1] + nums[2] - target)
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum1 = nums[i] + nums[left] + nums[right]
            res.append(sum1)
            if sum1 == target:
                return sum1
            else:
                val = abs(sum1 - target)
                if val < minval:
                    minval = val
            left += 1
            right -= 1
    # print(minval)
    # print("++++++++")
    print(res)
    a = minval + target
    b = target - minval
    if a in res:
        print(a)
    if target - minval in res:
        print(b)

nums1 = [1,2,3,4,7]
threeSumClosest(nums1,3)