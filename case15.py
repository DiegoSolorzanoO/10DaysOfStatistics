import math

x = int(input())
n = int(input())
median = float(input())
deviation = float(input())

def nd(d, m, x):
    i = 1 + math.erf((x-m) / (d * math.sqrt(2)))
    return 0.5 * i

sample_median = n * median
sample_deviation = math.sqrt(n) * deviation

prob = nd(sample_deviation, sample_median, x)
print(round(prob,4))