#在原数组去重
from typing import List

# 删除的思想:向前移动或向后移动(进行替换)

# =====有序数组去重======
#有序数组去重,返回新数组长度
nums1 = [0,0,1,1,2,2,3,4,5]
# #方案一:利用去重以及切片
def  remove_re(nums:List) -> int:
    n = len(set(nums)) #去重后的数组长度
    i = 0
    while i < n-1:
        if nums[i] == nums[i+1]:
            temp = nums[i+1]
            nums[i+1:len(nums)-1] = nums[i+2:] # 利用切片将数组内的元素进行替换,但不影响原数组未进行替换的元素
            nums[-1] = temp # 数组最后一位重新赋值
        else:
            i += 1
    return i + 1

##方案二:双指针 快慢指针
#有序数组去重,返回新数组长度
# 快指针:找到和慢指针不同的元素,无论是否相同都要往前走一步
nums2 = [0,0,1,1,2,2,3,4,5]
def remove_deplicate(nums:List) ->int:
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            # 先走一步,在进行交换.
            slow += 1  #slow与fast之间最多差一个相同的值,必须先向前走一步,在进行替换.让其走到第二个重复元素.
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1  #fast从1开始,共走len-1步, 因此在返回长度时,slow需要加1


##=====将值0移动到末尾========
nums3 = [0,0,0,1,1,2,2,3,4,5,4,3,0,5]
# #方案一:利用切片将元组替换 (如果首位是0 会有问题)
value = 0
# def move_value(nums:List):
#     fast = 0
#     # slow = 0
#     while fast < len(nums):
#         if nums[fast] != value:
#             fast += 1
#         else:
#             nums[fast:len(nums)-1] = nums[fast+1:]
#             nums[-1] = value
#             fast += 1
#     return nums

# #方案二:利用双指针
## 快指针找到非0元素
# 移动0,将0 移动到最后
def move_value(nums:List):
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == value:
            fast += 1
        else:
            # 一定要先交换,slow后移动(因为交换时nums[slow]一定是0,如果先移动会造成0值不能被替换)
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow,len(nums)):  #fast从0开始,共走len步,因此在返回长度时slow不用加1
        nums[i] = value
    return nums

##=========删除指定元素===========
# #方案一:快慢双指针
nums4 = [1,1,1,1,2,3,4,5,6,7,5,4,3]
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
    new_nums = nums[:slow]
    return new_nums,slow

# ##=======删除(顺序数组)指定元素,元素个数允许小于等于2=======
nums5 = [1,1,1,2,2,2,3,3,4,5,1,2,1]
def remove_re2(nums:List): #duplication
    fast = 1
    slow = 0
    count = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            count += 1
            if count == 2:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        else:
            slow = slow + 1
            nums[slow] = nums[fast]
            count = 1
            fast = fast + 1
    return slow + 1,nums[:slow]










print(remove_re(nums1))
# aa = Solution()
# print(aa.remove_deplicate(numsa))
# print(remove_deplicate(nums2))

print(move_value(nums3))

print(remove_value(nums4,1))

print(remove_re2(nums5))







