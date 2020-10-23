import time
#斐波那契数列
def f(i):
    if i <= 1:
        return i
    else:
        return f(i-1) + f(i-2)

start = time.time()
print(f(4))
end = time.time()
dur = end-start
print(dur)