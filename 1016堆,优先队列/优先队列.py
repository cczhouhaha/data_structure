#普通队列：先进先出，后进后出
#优先队列：出队顺序和入队顺序无关，和优先级有关.在优先队列中，元素被赋予优先级。当访问元素时，具有最高优先级的元素最先删除。
# 优先队列具有最高级先出 （first in, largest out）的行为特征。通常采用堆数据结构来实现。
# (优先队列的接口和普通队列的接口是完全相同的，只是在出队和查看队首的实现方式会不同（优先级最高的在队首）)

# 用堆的思想实现优先队列
class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self, data): #入队操作
        self.array.append(data)
        self.size += 1
        self.heapify_up() #堆化

    def dequeue(self): #出队操作
        if self.size <= 0:
            raise Exception('空队列')
        remove_data = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapify_down()
        return remove_data

    def heapify_up(self): #最大堆 (进行插入操作,从最后一个结点开始判断)(从下往上)
        child_index = self.size - 1 #最后一个孩子下标(新插入的最后一个叶子)
        parent_index = (child_index - 1) >> 1 #父亲下标
        temp = self.array[child_index] #记录插入的孩子值
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]  # 孩子结点重新赋值 (替换)(父亲和孩子也可以进行交换)
            child_index = parent_index  # 孩子结点上移,向着 0 移动
            parent_index = (child_index - 1) >> 1  # 父结点上移
        self.array[child_index] = temp

    def heapify_down(self): #(进行删除操作)从新的第一个结点开始判断(从上往下)
        total_index = self.size - 1  # 数组的长度
        index = 0
        # maxvalue_index = index ##此步放在循环外也可
        while True:
            maxvalue_index = index  #最大值下标
            if 2 * index + 1 <= total_index and self.array[2 * index + 1] > self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 1  # 如果左孩子结点大于当前最大节点,最大值索引等于左孩子索引
            if 2 * index + 2 <= total_index and self.array[2 * index + 2] > self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 2  # 如果右孩子结点大于当前最大结点,最大值索引等于右孩子结点
            if maxvalue_index == index:  # 如果
                break
            self.array[index],self.array[maxvalue_index] = self.array[maxvalue_index],self.array[index] #(交换)
            # self.swap(index, maxvalue_index)  # 交换最大值和和当前值
            index = maxvalue_index  # 当前值等于这一轮的最大值结点

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(5)
    pq.enqueue(6)
    pq.enqueue(10)
    pq.enqueue(8)
    pq.enqueue(3)
    pq.enqueue(4)
    pq.enqueue(3)
    pq.enqueue(5)
    pq.enqueue(9)

    print(pq.array)
    print(pq.dequeue())
    print(pq.array)