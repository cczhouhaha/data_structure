from typing import List
from pprint import pformat


# 有序数组
def TwoSum(nums:List,value):
    head = 0
    end = len(nums)-1
    while head < end:
        sum = nums[head] + nums[end]
        if sum == value:
            print([nums[head],nums[end]])
            head += 1
            end -= 1
        else:
            if sum > value:
                end -= 1
            elif sum < value:
                head += 1

def TwoSum2(nums:List,value):
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i] + j == value:
                print([nums[i],j])


def TwoSum3(nums:List,value):
    nums_dic = {} #值:下标
    for i in range(len(nums)):
        temp = value - nums[i]
        if temp in nums_dic:
            print(i,nums_dic[temp]) #两数下标
        else:
            nums_dic[nums[i]] = i

# 二叉树
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Node({self.data})"


class Tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = [self.root]
            while temp:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = new_node
                if pop_node.right is None:
                    pop_node.right = new_node
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)


    def get_parent(self,data):
        res= []
        if self.root is None:
            raise Exception("The tree is empty")
        if self.root.data == data:
            return "无父节点"
        else:
            temp = [self.root]
            while temp:
                pop_node = temp.pop(0)
                if pop_node.left.data == data:
                    res.append(pop_node)
                if pop_node.right.data == data:
                    res.append(pop_node)
                else:
                    if pop_node.left is not None:
                        temp.append(pop_node.left)
                    if pop_node.right is not None:
                        temp.append(pop_node.right)
        return res

# 二叉排序树
class Node1:
    def __init__(self,data,parent):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is None:
            return self.data
        return pformat({"%s"%(self.data):(self.left,self.right)})

class BST:
    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root is None:
            return True
        return False

    def insert(self,data):
        new_node = Node1(data,None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while  True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def search(self,value):
        if self.is_empty() :
            raise Exception("The tree is empty")
        else:
            node = self.root
            while node and node.value != value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right
            # print(node)
            return node #如果node是跟结点,会返回左右孩子

    def is_right(self,node):
        return node == node.parent.right


    def reassign(self,node,new_child):
        if new_child is not None:
            new_child.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child



























