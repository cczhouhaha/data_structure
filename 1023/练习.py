from typing import List
#快速排序(双指针快排和单指针快排)
def partition(nums,start,end):
    pivot = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < pivot:
            p += 1
        while p <= q and nums[q] >= pivot:
            q -=  1
        if p < q:
            nums[p],nums[q] = nums[q],nums[p]
    nums[start],nums[q] = nums[q],nums[start]
    return q
def quickSort(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quickSort(nums,start,mid-1)
    quickSort(nums,mid+1,end)

def patitionSingle(nums,start,end):
    pivot = nums[start]
    mark = start
    for i in range(start+1,end+1):
        if nums[i] < pivot:
            mark += 1
            nums[mark],nums[i] = nums[i],nums[mark]
    nums[start],nums[mark] = nums[mark],nums[start]
    return mark
def quickSortSingle(nums,start,end):
    if start >= end:
        return
    mid = patitionSingle(nums,start,end)
    quickSortSingle(nums,start,mid-1)
    quickSortSingle(nums,mid+1,end)
num1 = [4,3,6,7,3,2,1]
quickSort(num1,0,len(num1)-1)
# print(num1)
num2 = [4,3,6,7,3,2,1]
quickSortSingle(num2,0,len(num1)-1)
# print(num2)

def quickSort1(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    less = [i for i in nums[1:] if i < pivot]
    greater = [i for i in nums[1:] if i >= pivot]
    return quickSort1(less) + [pivot] + quickSort1(greater)
num3 = [4,3,6,7,3,2,1]
# print(quickSort1(num3))

#计数排序 (将出现次数放入一个新列表,其对应的下标为原列表元素值)
def countSort(nums):
    max_value = max(nums)
    countlen = max_value+1
    countlist = [0] * countlen
    res  = []
    for i in nums:
        countlist[i] += 1
    for i in range(len(countlist)) :
        while countlist[i] > 0:
            res.append(i)
            countlist[i] -= 1
    return res

num4 =  [4,3,6,7,3,2,1]
# print(countSort(num4))



#字典树
class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False
    def __repr__(self):
        return str(self.data)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            # child = node.data[char]
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True
    def search(self,word):
        node = self.root
        for char in word:
            node = node.data[char]
            if node is None:
                return False
        return node.is_word
    def searchPre(self,prefix):
        node = self.root
        for char in prefix:
            node = node.data[char]
            if not node:
                return False
        return True



if __name__ == '__main__':
    tt = Trie()
    tt.insert("someone")
    tt.insert("some")
    tt.insert("someday")
    # print(tt.root)
    # print(tt.search("some"))
    # print(tt.searchPre("so"))



