import math

num1, num2 = list(map(float, input().split(' ')))
prob = num1 / num2

def b(x, n, p):
    nx = math.factorial(n) / (math.factorial(x) * math.factorial(n-x))
    return nx * math.pow(p,x) * math.pow(1-p,n-x)

final_prob = sum([b(i,6,prob/(1+prob)) for i in range(3, 7)])
print(round(final_prob, 3))