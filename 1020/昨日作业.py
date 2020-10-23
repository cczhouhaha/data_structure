from typing import List
# #最长回文子串
# def centertSpread(strs, left, right) -> str:
#     i = left
#     j = right
#     length = len(strs)
#     while i>= 0 and j < length:
#         if strs[i] == strs[j]:
#             i -= 1
#             j += 1
#         else:
#             break
#     return strs[i+1:j]
#
# def longestPalindrom(strs:str) -> str:
#     length = len(strs)
#     if length < 2:
#         return strs
#     maxlen = 1
#     res = strs[0]
#     for i in range(length-1):
#         odd = centertSpread(strs,i,i) #奇数
#         even = centertSpread(strs,i,i+1) #偶数
#         maxstr = odd if len(odd) > len(even) else even
#         if len(maxstr) > maxlen:
#             maxlen = len(maxstr)
#             res = maxstr
#     return res

def centerSpread(strs, left, right):
    i = left
    j = right
    length = len(strs)
    while i >= 0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i+1:j]


def longestPalindrom(strs:str) -> str:
    length = len(strs)
    if length < 2:
        return strs
    maxlen = 1 #回文子串最大长度
    res = strs[0] #最长回文子串
    for i in range(length-1): #[回文子串]长度分为奇数和偶数,需分情况考虑
        odd = centerSpread(strs,i,i) #奇数 (当[回文子串]为奇数的时候,以当前字符为中心,向两边移动进行判断)
        even = centerSpread(strs,i,i+1) #偶数(当[回文子串]为偶数时,以当前字符以及下一个字符为中心,向两边移动进行判断)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res

if __name__ == '__main__':
    str1 = "0100101002003001342"
    # print(longestPalindrom(str1))

#荷兰国旗
def sortColors(nums:List):
    a = c = 0
    b = len(nums)-1
    while c <= b:
        if nums[c] == 0:
            nums[a],nums[c] = nums[c],nums[a]
            a += 1
            c += 1
        elif nums[c] == 2:
            nums[c],nums[b] = nums[b],nums[c]
            b -= 1
        else:
            c += 1
    return nums
nums1 = [0,1,2,0,2,1,0,2,1]
print(sortColors(nums1))


