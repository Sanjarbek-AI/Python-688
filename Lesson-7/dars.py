# numbers = [12, 4, 5, 5, 31, 3, 5, 3, 23, 5, 6, 3423]
# if ... in numbers:
#     pass
# numbers[2] = "Saidaloxon"
# # index = numbers.index(23)
# # numbers.append(23423456765456)
# # numbers.remove(31)
# # numbers.pop(-1)
#
# print(numbers)

fruits = ["apple", "mango", "orange", "ananas", "banana"]

fruit = input("Enter fruit: ")

if fruit in fruits:
    print(fruits)
    fruits.remove(fruit)
    print(fruits)
else:
    print("Wrong fruit name.")