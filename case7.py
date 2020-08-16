import math

# prob, rep = list(map(float, input().split(' ')))
# prob = prob/100

prob = 0.12
rep = 10

def b(x, n, p):
    nx = math.factorial(n) / (math.factorial(x) * math.factorial(n-x))
    return nx * math.pow(p,x) * math.pow(1-p,n-x)

first_prob = sum([b(i,rep,prob) for i in range(3)])
print(round(first_prob, 3))

second_prob = abs(sum([b(i,rep,prob) for i in range(2)]) - 1)
print(round(second_prob, 3))