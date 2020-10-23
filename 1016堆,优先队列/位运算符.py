from typing import List

def weiyu(num:int):
    count = 0
    while num != 0:
        num = num & (num-1)
        count += 1
    return count

# print(weiyu(3))


# 异或:两个相同的数异或后得0, 一个数和0 异或后得那个数.
nums = [1,2,2,4,4,1,5]
def weiyihuo(nums:List):
    res = 0
    for i in nums:
        res = res ^ i
    return res

# print(weiyihuo(nums))


# 求两个数最大公约数 利用余数(a与b的最大公约数 == a与b的余数 与 b 的最大公约数)
def getMaxcommpisor(a,b):
    if a < b:
        a, b = b, a  # 保证a大于b
    while a % b != 0:
        a, b = b, a % b
    return b

# print(getMaxcommpisor(10,50))

#最大公约数
#1.暴力做法
def max_division(x,y):
    big = max(x,y)
    small = min(x,y)
    if big % small == 0:
        return small
    else:
        for i in range(small // 2,0,-1): #small // 2:除以2向下取整
            if big % i == 0 and small % i == 0:
                return i
# print(max_division(45,24))

#2.辗转相除((a与b的最大公约数 == a与b的余数 与 b 的最大公约数))
def max_division1(x,y):
    if x < y:
        x,y = y,x
    while x % y != 0:
        x,y = y,x % y
    return y
def max_division11(x,y):
    small = min(x,y)
    big = max(x,y)
    if big % small == 0:
        return small
    return max_division(small,big % small)
#3.更相减损术 ((a与b的最大公约数 == a与b的差 与 b 的最大公约数))
def max_division2(x,y):
    if x - y == 0:
        return x
    big = max(x,y)
    small = min(x,y)
    return max_division2(small,big-small)

# print(max_division2(45,24))

#4.两者混合运算
def gcd(x,y):
    if x % y == 0:
        return y
    if x < y:
        return gcd(y,x)
    else:
        if x % 2 == 0 and y % 2 == 0:
            return gcd(x>>1,y>>1) << 1
        elif x % 2 == 0 and y % 2 != 0:
            return gcd(x >> 1, y)
        elif x % 2 != 0 and y % 2 == 0:
            return gcd(x, y >> 1)
        else:
            return gcd(x,x-y)
print(gcd(24,10))


def greatest5(a,b):
    if a==b:#当俩数相同返回本身
        return a
    if a<b:#确定a为最大值
        a,b=b,a
    else:#出口为a
        if a%2==0 and b%2==0:#当a,b都为偶数
            return greatest5(a>>1,b>>1)
        elif a%2==0 and b%2!=0:
            return greatest5(a>>1,b)
        elif a % 2 != 0 and b % 2 == 0:
            return greatest5(a,b>>1)
        else:
            return greatest5(b,a-b)
# print(greatest5(12,4))