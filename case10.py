import math

y = float(input())
k = float(input())
e = 2.71828

def p(k, y):
    upper = math.pow(y, k) * math.pow(e, -y)
    lower = math.factorial(k)
    return upper/lower

print(round(p(k,y), 3))