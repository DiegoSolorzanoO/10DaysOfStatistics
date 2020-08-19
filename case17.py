import math

n = int(input())
strx = input().split(' ')
x = list(map(float, strx[:n]))
y = list(map(float, input().split(' ')))

def get_rank(x):
    sorted_x = list(x)
    sorted_x.sort()
    dict1 = {}
    for i in range(len(sorted_x)):
        dict1[sorted_x[i]] = i + 1
    rank_x = []
    for num in x:
        rank_x.insert(0,dict1[num])
    return rank_x

def srcc(rx, ry):
    d = []
    for i in range(len(rx)):
        d.insert(0, math.pow(rx[i] - ry[i], 2))
    upper = 6 * sum(d)
    lower = len(rx) * (math.pow(len(rx), 2) - 1)
    return round(1 - (upper/lower), 3)
    

rank_x = get_rank(x)
rank_y = get_rank(y)

print(srcc(rank_x, rank_y))