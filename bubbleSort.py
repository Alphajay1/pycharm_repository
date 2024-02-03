import random
import math

randomList = []

for i in range(5):
    randomList.append(random.randrange(1, 10))

i = len(randomList) - 1

while i > 1:

    j = 0

    while j < i:

        print("\nIs {} > {}".format(randomList[j], randomList[j + 1]))

        if randomList[j] > randomList[j + 1]:
            print("Switch")

            temp = randomList[j]
            randomList[j] = randomList[j + 1]
            randomList[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        for num in randomList:
            print(num, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for num in randomList:
    print(num, end=", ")
print()