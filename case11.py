import math

data = list(map(float, input().split(' ')))
a, b = data[0], data[1]

e = 2.71828

def p(k, y):
    upper = math.pow(y, k) * math.pow(e, -y)
    lower = math.factorial(k)
    return upper/lower

def costA(x):
    return 160 + 40 * math.pow(x, 2)

def costB(x):
    return 128 + 40 * math.pow(x, 2)

a_repairs = sum([costA(i) * p(i, a) for i in range(20)])
b_repairs = sum([costB(i) * p(i, b) for i in range(20)])

print(round(a_repairs, 3))
print(round(b_repairs, 3))
