# SUM OF ALL ARGS ON THE COMMAND LINE
import sys

sum_of_num = 0
for i in range(1, len(sys.argv)):
    sum_of_num += int(sys.argv[i])
print("Sum is = ", sum_of_num)
