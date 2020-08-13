import math

x = int(input())
numbers = list(map(lambda x: int(x), input().split(" ")))

def printMedian(list):
    l = len(list)
    median_s = l % 2
    median_list = []
    if median_s == 0:
        median_list.append(list[round(l/2)-1])
        median_list.append(list[round(l/2)])
    else:
        median_list.append(list[math.floor(l/2)])

    total_median = 0
    for num in median_list:
        total_median = total_median + num
    print(round(total_median/len(median_list)))

numbers.sort()

fs1 = 0
ss2 = 0
pair = x%2
if pair == 0:
    fs1 = round(x/2)
    ss2 = fs1
else:
    fs1 = math.floor(x/2)
    ss2 = fs1 + 1

printMedian(numbers[:fs1])
printMedian(numbers)
printMedian(numbers[ss2:])

