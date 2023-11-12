"""
- SET methdlarini yodlash
- TUPLE methodlarini yozlash

1. Odamdan ikkita ism sorash va ikkalsida ham bor harflarni print qilish
2. IChida 5 ism bor set yaratasiz, odamdan ismini soraysiz agar bunaqa ism
   bor bolsa bor desin yoq bolsa uni ismini qoshib qoying.
3. Odamdan qaysi davlatda yashashini sorash va uni ichida unli
 harflarni setga qoshib ketish
4. Odamdan ismini kitishini so'rang va uning ismidagi har bitta harfni alohida elemnt qilib tuple da saqlang. Va qaysi
   harf eng ko'p ishlatilganini topib bering.

"""


# city = input("City: ")
#
# unli = set()
#
# for char in city:
#     if char in "auioeAOUEI":
#         unli.add(char)
# print(unli)

name = input("Name: ")
name = tuple(name)

max_letter = name[0]
for letter in name:
    if name.count(letter) > name.count(max_letter):
        max_letter = letter
print(max_letter)