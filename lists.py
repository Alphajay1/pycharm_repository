import random
import math

randList = ["string", 1.234, 28]

oneToTen = list(range(10))

randList = randList + oneToTen

print(randList[0])

first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 4 )

print("string" in first3)
print("How many string in first3?", first3.count("string"))
first3[0] = "New string"
for i in first3:
    print("{} : {}".format(first3.index(i), i))
first3.append("Another")
for i in first3:
    print("{}:{}".format(first3.index(i), i))
