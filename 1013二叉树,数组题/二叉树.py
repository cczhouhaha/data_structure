class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Node({self.data})"


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = [self.root] #建立列表,接收所要遍历的值
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = new_node
                    return
                elif pop_node.right is None:
                    pop_node.right = new_node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)
    # def __repr__(self):
    #     curr = self.root
    #     sstr = ""
    # 根据某一元素的值,找到父节点
    def get_parent(self,data):
        if self.root.data == data:
            return None
        temp = [self.root] #接收遍历的值
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == data:
                return pop_node
            if pop_node.right.data == data:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)

    def get_parent1(self,data):
        if self.root.data == data:
            return None
        res = []
        temp = [self.root] #接收遍历的值
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == data:
                res.append( pop_node)
            if pop_node.right.data == data:
                res.append(pop_node)
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        print (res)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)
    bt.insert(8)
    bt.insert(9)
    print(bt.root.left.left)

