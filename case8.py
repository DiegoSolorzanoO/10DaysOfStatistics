import math

# n, d = list(map(int, input().split(' ')))
# inspection = int(input())

u = 1
d = 3
inspection = 5

def g(n,p):
    q = abs(p-1)
    return math.pow(q, n-1) * p 

print(round(g(inspection, u/d),3))