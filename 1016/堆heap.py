#堆是完全二叉树,又分为最大堆(根>左右孩子)和最小堆(根<左右孩子)
class Heap:
    def __init__(self):
        self.data_list = []  #用数组实现
    # 得到父节点的下标
    def get_parent_index(self,index):
        if index < 0 or index >= len(self.data_list):
            raise IndexError("The index out of range")
        else:
            return (index-1) >> 1   #孩子结点坐标(二进制)右移一位得到父节点坐标

    def swap(self,child_index,parent_index): #孩子结点与父节点相互交换
        self.data_list[child_index],self.data_list[parent_index]=self.data_list[parent_index],self.data_list[child_index]

    def insert(self,data):
        self.data_list.append(data)
        index = len(self.data_list)-1
        parent_index = self.get_parent_index(index)
        while self.data_list[parent_index] < data and parent_index >= 0: #如果插入数值大于父节点值,进行循环替换操作
            self.swap(index,parent_index) #先让两者的值进行交换
            index = parent_index #下标进行交换
            parent_index = self.get_parent_index(index) #找到新下标的父节点
    def __repr__(self):
        return str(self.data_list)

    def pop(self): #删除堆顶
        remove_data = self.data_list[0] #记录要删除的堆顶
        self.data_list[0] = self.data_list[-1] #将堆顶的值替换为最后一个元素的值
        del self.data_list[-1] #删除最后一个元素的值
        self.heapify(0) #然后堆化 (即重新排序)
        return remove_data

    def heapify(self,index): #堆顶化 即重新排序
        size = len(self.data_list)-1 #整个长度的范围
        max_index = index #最大值下标max_index
        while True:
            if 2*index+1 <= size and self.data_list[max_index] < self.data_list[2*index+1]: #如果最大值发生变化,需要进行移位变换
                max_index = 2*index+1
            if 2*index+2 <= size and self.data_list[max_index] < self.data_list[2*index+2]:
                max_index = 2*index+2
            if max_index == index:
                break
            self.swap(index,max_index)
            index = max_index






h = Heap()
h.insert(10)
h.insert(7)
h.insert(8)
h.insert(9)
h.insert(6)
print(h)
h.insert(11)
print(h)
h.insert(5)
print(h)
h.pop()
print(h)


