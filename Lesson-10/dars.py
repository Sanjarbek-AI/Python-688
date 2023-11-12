# num = 100
#
# while num > 0:
#     print(num)
#     num = num + 1
# num = 1
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1
#
# num = 1
# son = 0
# while num <= 100:
#     if num % 4 == 0:
#         son += 1
#     num += 1
#
# print(son)

import random


num = 1
nums = []

while num <= 10:
    random_number = random.randint(1, 50)
    if random_number % 2 == 1:
        nums.append(random_number)
        num += 1
print(nums)

