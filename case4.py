import math

x = int(input())
list1 = list(map(lambda x: int(x), input().split(" ")))
list2 = list(map(lambda x: int(x), input().split(" ")))

s = []

for i in range(x):
    for j in range(list2[i]):
        s.append(list1[i])

s.sort()

def getMedian(list):
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
    return round(total_median/len(median_list), 1)

x = len(s)

fs1 = 0
ss2 = 0
pair = x%2
if pair == 0:
    fs1 = round(x/2)
    ss2 = fs1
else:
    fs1 = math.floor(x/2)
    ss2 = fs1 + 1

q1 = getMedian(s[:fs1])
q3 = getMedian(s[ss2:])

print(round(q3-q1, 1))