x = int(input())
list1 = list(map(lambda x: int(x), input().split(" ")))
list2 = list(map(lambda x: int(x), input().split(" ")))

upper = 0

for i in range(x):
    upper = upper + (list1[i]*list2[i])

lower = sum(list2)

print(round(upper/lower,1))
