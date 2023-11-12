# def add(num1: int, num2: int):
#     result = num1 + num2
#     return result
#
#
# number1 = int(input("Num1: "))
# number2 = int(input("Num2: "))
#
# res = add(number1, number2)
# print(res)

#
# def step(num1: int, num2: int):
#     result = num1 ** 2 + num2 ** 2
#     return result
#
#
# number1 = int(input("Num1: "))
# number2 = int(input("Num2: "))
#
# res = step(number1, number2)
# print(res)

# def multiply(num: int, text: str):
#     counter = 0
#     for letter in text:
#         if letter in "auoieAOUIE":
#             counter += 1
#     return counter * num
#
#
# number = int(input("Num: "))
# user_text = input("Text: ")
#
# res = multiply(number, user_text)
# print(res)


def find_max(num1: int, num2: int, num3: int):
    return max(num1, num2, num3)


number1 = int(input("Num1: "))
number2 = int(input("Num2: "))
number3 = int(input("Num3: "))

res = find_max(number1, number2, number3)
print(res)
