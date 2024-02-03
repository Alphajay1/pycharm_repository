import random
import math

numList = [1, 2, 3, 4, 5]

powerList = [[math.pow(num, 2), math.pow(num, 3), math.pow(num, 4)]for num in numList]

for i in powerList:
    print(i)
