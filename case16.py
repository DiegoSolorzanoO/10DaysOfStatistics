import math

n = int(input())
strx = input().split(' ')
x = list(map(float, strx[:n-1]))
y = list(map(float, input().split(' ')))


def get_median(l, d):
    total = 0
    for x in l:
        total += x
    return round(total/len(l), d)

def get_std_dev(l, d, median):
    s = 0
    for n in l:
        s += math.pow(n-median, 2)
    return round(math.sqrt(s/len(l)), d)

def get_pcc(x, y, n, d):
    median_x = get_median(x, 2)
    std_x = get_std_dev(x, 5, median_x)
    median_y = get_median(y, 2)
    std_y = get_std_dev(y, 5, median_y)
    upper = 0
    for i in range(n):
        upper += ((x[i]-median_x)*(y[i]-median_y))
    return round(upper/(n*std_x*std_y), d) 

print(get_pcc(x,y,n,3))