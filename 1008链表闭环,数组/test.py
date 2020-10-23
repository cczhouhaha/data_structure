# a = int(input("请输入数字:") )
# if a > 5:
#     raise IndexError("数字大于5")
# else:
#     print(a)
# print("+++")

a = [1,4,7,3,8]
amin = a[0]
for i in a:
    if i < amin:
        amin = i
print(amin)

