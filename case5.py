import math

x = int(input())
s = list(map(lambda x: int(x), input().split(" ")))

total = 0
for num in s:
    total = total + num
mean = round(total/x,1)

squared_distances = []
for num in s:
    squared_distances.append(pow(num-mean,2))

print(round(math.sqrt(sum(squared_distances)/x), 1))