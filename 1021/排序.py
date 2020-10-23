from typing import List
# # ==========归并排序==============
#分离指针  先拆后合
def mergeSort(nums:List): #进行拆分,每次分为两部分
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left,right = nums[:mid],nums[mid:]
    return merge(mergeSort(left),mergeSort(right)) #调用合并函数,每次合并两部分

def merge(l1,l2): #合并函数,第一种用pop
    res = []
    while l1 and l2:
        if l1[0] > l2[0]:
            res.append(l2.pop(0))
        else:
            res.append(l1.pop(0))
    if l1:
        res.extend(l1)
    if l2:
        res.extend(l2)
    return res

# num1 = [1,24,3,2,6,8,7,4,35,12,14]
# print(mergeSort(num1))

def mergeSort1(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left,right = num[:mid],num[mid:]
    return merge1(mergeSort(left),mergeSort(right))

def merge1(left,right): #合并函数,第二种用分离双指针
    res = []
    p = 0
    q = 0
    while p < len(left) and q < len(right):
        if left[p] > right[q]:
            res.append(right[q])
            q += 1
        else:
            res.append(left[p])
            p += 1
    if p < len(left): #也可以直接进行追加,不用这两个判断(空列表也可直接进行追加)
        res.extend(left[p:])
    if q < len(right):
        res.extend(right[q:])
    return res

# num1 = [1,24,3,2,6,8,7,4,35]
# print(mergeSort1(num1))





# ==========快速排序============
def swap(nums, p, q):
    nums[p],nums[q] = nums[q],nums[p]
def partition(nums:List,start,end):
    pivot = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < pivot:
            p += 1
        while p <= q and nums[q] >= pivot:
            q -= 1
        if p < q:
            swap(nums,p,q)
    swap(nums,start,q) #此时,p走到q前面,因此将start与q进行调换
    return q
def quickSort(nums,start,end):
    if start >= end:
        return
    mid = partition(nums,start,end)
    quickSort(nums,start,mid-1)
    quickSort(nums,mid+1,end)

num1 = [1,2,3,2,7,8,4,6,10]
# quickSort(num1,0,len(num1)-1)
# print(num1)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# print (quicksort(num1))


# ======单指针快排=========
def partitionSingle(nums,start,end):
    pivot = nums[start]
    mark = start
    for i in range(start+1,end+1): #end为最后一个下标,range包头不包尾,需要加1
        if nums[i] < pivot: #i找到小于基数的值,然后让指针mark往前走一步,两者进行调换
            mark += 1
            nums[mark],nums[i] = nums[i],nums[mark]
    # nums[start] = nums[mark] #循环结束之后,让基数与mark的值进行调换
    # nums[mark] = pivot
    nums[start],nums[mark] = nums[mark],nums[start]
    return mark
def partitionSort(nums,start,end):
    pivot = nums[start]
    mark = start
    for i in range(start+1,end+1):
        if num[i] < pivot:
            mark += 1
            nums[mark],nums[i] = nums[i],nums[mark]
    nums[start] = nums[mark]
    nums[mark] = pivot
    return mark
def quickSortSingle(nums,start,end):
    if start >= end:
        return
    mid = partitionSingle(nums,start,end)
    quickSortSingle(nums,start,mid-1)
    quickSortSingle(nums,mid+1,end)

num = [4,7,3,5,6,2,8,1,1,3,5]
quickSortSingle(num,0,len(num)-1)
# print(num)



#计数法排序:适合计数在一定范围区间内
# 计数排序不是比较数值排序，是记录数据出现次数的一种排序算法
# 找出待排数组中最大值
# 额外一个数组记录待排数组值出现的次数
# 循环打印存储数值次数的数组下标值

def countSort(nums):
    maxvalue = max(nums) #记录需要排序的最大值
    countlen = maxvalue + 1 #考虑0,需要+1
    countList = [0] * countlen #建立记录元素出现次数的列表
    res = [] #建立空列表,接收最后结果
    for a in nums:
        countList[a] += 1 #原数组的元素,即为新列表的下标
    # for a in nums:
    #     if not countList[a]:
    #         countList[a] = 0
    #     countList[a] += 1
    for i in range(len(countList)): #新列表的下标即是原数组的元素
        while countList[i] >0:
            res.append(i)
            countList[i] -= 1
    return res
int_list = [1,8,6,5,6,6,8,4,8]
c = countSort(int_list)
# print(c)

#桶排序
#分桶,桶内排序运用其他排序方法
#1.造桶(初始化桶)2.定位桶内元素3.桶内排序4.输出
def bucketSort(nums):
    max_value = max(nums)
    min_value = min(nums)
    bucketNum = len(nums) #桶的数量即为元素个数
    d = max_value - min_value
    bucketList = [] #存放每个桶的容器
    res = []
    #初始化桶
    for i in range(bucketNum):
        bucketList.append([])
    #定位桶内元素
    for i in range(len(nums)):
        num = int((nums[i]-min_value)*(bucketNum-1)/d) #每个元素对应的每个桶的下标值
        bucket = bucketList[num]
        bucket.append(nums[i])
    #桶内排序
    for bucket in bucketList:
        bucket.sort()
    #输出
    for bucket in bucketList:
        for i in bucket:
            res.append(i)
    return res

num2 = [4.5,0.5,1.5,1.8,2.6,4,7]
print(bucketSort(num2))







