import math

x = int(input())
numbers = list(map(lambda x: int(x), input().split(" ")))
total = 0
for num in numbers:
    total = total + num
print(round(total/x,1))

numbers.sort()
median_s = x % 2
median_list = []
if median_s == 0:
    median_list.append(numbers[round(x/2)-1])
    median_list.append(numbers[round(x/2)])
else:
    median_list.append(numbers[math.ceil(x/2)])

total_median = 0
for num in median_list:
    total_median = total_median + num
print(round(total_median/len(median_list), 1))

num_dict = {}

for num in numbers:
    if num in num_dict:
        old = num_dict.get(num)
        num_dict[num] = old + 1
    else:
        num_dict[num] = 1

max = 1
for val in num_dict.values():
    if val > max:
        max = val

modes = []
for key, val in num_dict.items():
    if val == max:
        modes.append(key)

modes.sort()

print(modes[0])