"""
1. So'z ortiga ham oldiga ham bir xil o'qiladimi yoq'mi topish kodini yozing.
    Buning uchun userdan bitta text so'raysiz agar usha text aytganimdagi bo'lsa ha bu bir xi o'qiadi
    deysiz agar unday bo'lmasa yo'q deysiz.

2. 2 ta ozgaruvchi yataish 1-username 2-password, va userdan ikkita malumot kiritishini sorash
    agar user kiritgan username bizdagi username va user kiritgan password bizdagi passwordga
    to'g'ri kelsa xush keoibsiz desin aks holda hayr desin.
"""

# text = input("Biror So'z kiriting: ")
#
# if text == text[::-1]:
#     print("Bir Xil O'qiladi!")
# else:
#     print("Bir Xil O'qilmaydi!")

username = "sanjarbek.ai"
password = "qwerty"

user_name = input("Username :")
pass_word = input("Password :")

if user_name == username and password == pass_word:
    print("Welcome")
else:
    print("Error")
