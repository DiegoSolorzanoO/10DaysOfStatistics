import math

median, deviation = list(map(float, input().split(' ')))
ex1 = float(input())
ex2 = float(input())

def nd(d, m, x):
    i = 1 + math.erf((x-m) / (d * math.sqrt(2)))
    return 0.5 * i

prob1 = abs(nd(deviation, median, ex1) - 1) * 100
prob2 = abs(nd(deviation, median, ex2) - 1) * 100
prob3 = abs(nd(deviation, median, ex2)) * 100

print(round(prob1, 2))
print(round(prob2, 2))
print(round(prob3, 2))