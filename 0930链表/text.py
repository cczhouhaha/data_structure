# print("hello world")

# print("nihao")
"""
Author:Miss zhou
"""
def add(x:int,y:int) -> int: #类型注解
    """
    :param x: 参数1
    :param y: 参数2
    :return: 返回两数之和
    :rtype: int
    """
    return x+y

#
# print("abc")

"""
Author:Miss zhou
"""

# print(1232345452)

# def add(x:int,y:int) -> int:
#     '''
#     :param x:
#     :type x:
#     :param y:
#     :type y:
#     :return:
#     :rtype:
#     '''
#     return x + y



# class student:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#     def sleep(self):
#         print("%s休息"%(self.name))
#     def study(self):
#         print("%s学习"%(self.name))
#
# s = student("小明","男",18)
# s.sleep()

# 创建结点node
class Node:
    def __init__(self,data,next = None):
        # 创建结点注意两点:1.保存自己的数据data 2.告诉下一个元素next
        self.data = data
        self.next = None
    def __repr__(self):
        # 返回结点数据 将对象作为字符串输出
        return "Node({})".format(self.data)
        # return "Node(%s)"%(self.data)

