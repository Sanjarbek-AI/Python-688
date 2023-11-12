"""
1. for va range orqali 3 va 5 ga bo'linadigan sonalarni yangi list ochib ushanga qo'shib boradiagn funksiya yozing

2. ichida 5 ta meva nomi bor list yarating va o'zingiz yoqtirmagan mevani uni ichidan olib tashlaydigan funksiya yozing

3. ichida 10 ta son bor list yarating va o'zingiz yoqtirgan sonning indexini topib beradigan funksiya yozing

4. ichida 5 ta ism bor list yarating va 0-indexga o'zingizni ismingizni qo'shib beradigan funksiya yarating

5. ichida 10 son bor list yarating va eng kichkina va eng katta sonni o'rnini almashtirib beragigan funksiya yozing

"""

# numbers = [12, 4, 1, 3, 3232, 4, 3, 23, 0]
#
#
# def replace_max_min():
#     max_num = max(numbers)
#     min_num = min(numbers)
#     max_index = numbers.index(max_num)
#     min_index = numbers.index(min_num)
#     numbers[min_index], numbers[max_index] = max_num, min_num
#     return numbers
#
#
# result = replace_max_min()
# print(result)
# def app():
#     list1 = list()
#
#     for num in range(1,100):
#         if num % 3 == 0 and num % 5 == 0:
#             list1.append(num)
#     return list1
#
# app1 = app()
# print(app1)

# mevalar = ["Anor", "Shaftoli", "Anjir", "Tarvuz", "Qovun"]
#
#
# def chopar():
#     meva = input("Meva: ")
#     if meva in mevalar:
#         mevalar.remove(meva)
#         return mevalar
#     else:
#         return "Bunday meva yo'q"
#
#
# res = chopar()
# print(res)

# numbers = [12, 4, 3, 31, 3, 4, 34, 7]
#
#
# def find_index():
#     number = int(input("Number: "))
#     if number in numbers:
#         return numbers.index(number)
#     else:
#         return "Bunday son yo'q"
#
#
# res = find_index()
# print(res)

names = ['ali', 'vali', 'gani']


def name_adder():
    name = input("Name: ")
    names.insert(0, name)
    return names


res = name_adder()
print(res)
