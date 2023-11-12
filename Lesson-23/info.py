"""
Uyga vazifa:

Bankamat ko'dini yozib kelish, uni quyidagi funsksiyalari bo'lishi kerak
Dastlab bankamat uchun biror bir o'zgaruvchi yaratib pullarni quyidagicha saqlab oling

bank = {
    "1000": 100,
    "2000": 130,
    "5000": 345,
    "10000": 10,
    "20000": 23,
    "50000": 45,
    "100000": 67,
    "200000": 77,
}

bu holatda key lar bu pul qanaqaligi value lar esa ularni bankamotda nechta borligi

cards = {
    "8888999977774444": {
        "name": "Sanjarbek Tursunov",
        "money": 100000,
        "date": "10/25",
        "number": 8888999977774444,
        "password": 1232,
    },
    "8888994577774444": {
        "name": "Alijon Valijanov",
        "money": 500000,
        "date": "1/27",
        "number": 8888994577774444,
        "password": 1112,
    },
    "8888988977774444": {
        "name": "Qahhor Namozov",
        "money": 300000,
        "date": "11/28",
        "number": 8888988977774444,
        "password": 1212,
    }
}

bu esa sizda odamlarni kartalarini malumot sifatida saqash usuli

sizni vazifangiz quyidagicha odamdan input sifatida karta raqam soraysiz, agar
shunday karta raqam cards ni ichida bor bo'lsa unga huddi bankamatdagi imkoniyatlar ni korsatasiz
yani kartadagi summani korish, pul yechish, parolni o'zgartirish

- show-money
- get-money
- change-password

show-money ni bosganda unga kartasida qancha pul borligini korsatasiz
get-monye bossa undan qancha pul kerakligini soraysiz va unga pulni
   quyidagi korinishda berasiz
Masalan:

odam sizdan 148 000 ming berishni so'radi
siz unga eng katta summada pastga qarab tushib kelgan holda pulni berasiz yani

100 000 - 1 ta
20 000  - 2 ta
5 000   - 1 ta
2 000   - 1 ta
1 000   - 1 ta

keyin esa bank degan dict ni ichida nechtadan ishlatgan bo'lsangiz shunchadan olib tashlaysiz

change-password: bu kamandani ishga tushirsa dastlab odamdan eski parolni kiritishini soraysiz
agar eski parolni togri kiritsa yangi parolni kiritishini soraysiz va parolni o'zgartirib qo'yasiz
agar notogri kiritsa parol notogri deysiz

"""



