import random

def randomList(n):
    randomList = []
    for i in range(n):
        randomList.append(random.randint(1,100))
    return randomList
if __name__ == '__main__':
    print(randomList(10))