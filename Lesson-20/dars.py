# while True:
#     try:
#         age = int(input("Age: "))
#         print(age)
#     except ValueError:
#         print("Bunday qiymat mumkin emas.")
#     except TypeError:
#         print()

# try:
#     num1 = int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     print(num1 / num2)
# except ValueError:
#     print("Bunday qiymat mumkin emas")
# except ZeroDivisionError:
#     print("Sonni 0 ga bo'lish mumkin emas")

# try:
#     names = ['ali', 'vali', 'gani']
#     index = int(input("Index: "))
#     print(names[index])
# except IndexError:
#     print("Xato index")
# except ValueError:
#     print("Bunday qiymat mumkin emas")
#
# try:
#     students = {
#         'ali': 10, 'vali': 5, 'gani': 3
#     }
#
#     name = input("Qaysi ism: ")
#     print(students[name])
# except KeyError:
#     print("Bunday ism yo'q")

# try:
#     num1 = int(input("Num1: "))
#     num2 = input("Num1: ")
#
#     print(num1 + num2)
# except TypeError:
#     print("Xato kalla")
# except ValueError:
#     print("Xato bosh")

# fruit = input("Fruit: ")
# try:
#     with open(f"{fruit}.txt", 'r') as reader:
#         print("malades bola ekansiz")
# except FileNotFoundError:
#     print("Malades bola emas ekansiz")
name = input("Name: ")

try:
    with open(f"{name}.txt", "r") as reader:
        last_name = input("last name: ")
        with open(f"{name}.txt", "a") as appender:
            appender.write(last_name + "\n")
except FileNotFoundError:
    with open(f"{name}.txt", "x"):
        pass
