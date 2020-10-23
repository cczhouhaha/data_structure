from  typing import List
# 有序数组实现二分查找
nums = [1,2,3,4,5,6,7,8]
def search(nums:List,value):
    size = len(nums)
    if size % 2 == 0:
        i = int(size/2)
        num = (nums[i] + nums[i+1])/2
    else:
        i = int((size+1)/2)
        num = nums[i]
    head = 0
    end = len(nums)-1
    while head < end:
        if nums[head] == value or nums[end] == value:
            if nums[head] == value:
                print (head)
                break
            else:
                print (end)
                break
        else:
            if value > num:
                end -= 1
            else:
                head += 1
search(nums,7)




# 反转数组

