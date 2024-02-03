import random
import math

randomList = []

for i in range(5):
    randomList.append(random.randrange(1, 10))

randomList.sort()

randomList.reverse()

randomList.insert(5, 20)

randomList.remove(20)

randomList.pop(2)


for num in randomList:
    print(num, end=", ")
print()