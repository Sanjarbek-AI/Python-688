# print("1. Hammasini kichkina qilish.")
# print("2. Hammasini kotta qilish.")
# print("3. Hammasini kichkinami tekshirish.")
# print("4. Replace.")
# print("5. Hammasini kichkina qilish.")
# print("6. Hammasini kichkina qilish.")
# print("7. Hammasini kichkina qilish.")
# print("8. Hammasini kichkina qilish.")
# print("9. Hammasini kichkina qilish.")
# print("10. Hammasini kichkina qilish.")
#
#
# while True:
#     text = input("Text: ")
#     choose = int(input("Enter your choose: "))
#
#     if choose == 1:
#         print(text.lower())
#     elif choose == 2:
#         print(text.upper())
#     elif choose == 4:
#         old = input("Old: ")
#         new = input("New: ")
#         print(text.replace(old, new))


names = ['ketmonbek', 'teshavoy', 'mahpirat', 'quvondiq']
names2 = ['ali', 'vali']

# names.remove('ketmonbek')
# names.pop(2)
# names[2] = "Odil"

# names.append('yangi')
# names.insert(1, 'nimadir')
# names.extend(names2)

# names.clear()
# count = names.count('ketmonbek')
# index = names.index('mahpirat')
# names.reverse()
# names.sort()
# print(names)
fruits = ['olma', 'behi', 'nok']

while True:
    print(fruits)
    choose = int(input("Choose: "))

    if choose == 1:
        name = input("Name: ")
        fruits.remove(name)
    elif choose == 2:
        index = int(input("Index: "))
        fruits.pop(index)
