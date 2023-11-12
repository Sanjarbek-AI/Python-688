# def add():
#     num1 = int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     result = num1 + num2
#     return result
#
#
# res = add()
# print(res)
print("1. Hammasini katta qilish")
print("2. Hammasini kichkina qilish")
print("1. Hammasini katta qilish")
print("1. Hammasini katta qilish")


def upper(text):
    return text.upper()


data = input("text: ")
option = int(input("Nima qilay bu textni: "))

if option == 1:
    res = upper(data)
    print(res)
elif option == 2:
    res = lower(data)
    print(res)
