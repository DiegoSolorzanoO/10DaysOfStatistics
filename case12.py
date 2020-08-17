import math

median, deviation = list(map(float, input().split(' ')))
ex1 = float(input())
ex21, ex22 = list(map(float, input().split(' ')))

def nd(d, m, x):
    i = 1 + math.erf((x-m) / (d * math.sqrt(2)))
    return 0.5 * i

prob1 = nd(deviation, median, ex1)
prob2 = nd(deviation, median, ex22)
prob3 = nd(deviation, median, ex21)

print(round(prob1, 3))
print(round(prob2-prob3, 3))