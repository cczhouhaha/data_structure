class Array:  #数组是连续的.
    def __init__(self, capacity):
        self.array = [None] * capacity #初始化数组(数组形式为列表)//array为属性名
        self.size = 0 #有效值长度
    def __repr__(self):
        return f"{self.array}"

    def insert(self,index,element):
        if index<0 or index > self.size: #数组是连续的,不能空着几个元素然后插入另外元素.
            raise  IndexError("索引越界")
        if self.size >= len(self.array) or index >= len(self.array): #一般size不能大于容量.最高为相等
            self.addcapacity() #调用增大扩容函数
        for i in range(self.size-1,index-1,-1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2  #*2可以自己定义,但不要太大,占空间.
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array #重新更改属性


    def remove(self,index):
        if index<0 or index >= self.size:
            raise IndexError("索引越界")
        if self.size >= len(self.array) or index >= len(self.array):
            self.addcapacity() #调用增大扩容函数 如果size满了,需要调用一下扩容
        for i in range(index,self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1
    def output(self):
        for i in range(self.size):
            print(f"{self.array[i] }" +"-->" )


if __name__=='__main__':
    aa = Array(10)
    aa.insert(0, 1)
    aa.insert(0, 2)
    aa.insert(0, 3)
    aa.insert(0, 4)
    aa.output()

    aa.remove(2)
    aa.output()

    aa.addcapacity()
    aa.output()


# def removeDuplicates(self, nums: List[int]) -> int:
#     for i in nums:

