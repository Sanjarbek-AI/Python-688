from utils import show_products_nice, add, remove, show_basket, calculate, check

products = {
    "olma": {
        "name": "Yangi suvli olma",
        "price": 2,
        "about": "Yaqinda bog'dan uzulgan, rangi qizil"
    },
    "non": {
        "name": "Shirin non",
        "price": 2,
        "about": "Yaqinda tandirdan uzulgan"
    },
    "cola": {
        "name": "Coca Cola",
        "price": 3,
        "about": "Shakarli coca cola, shirin ta'mli"
    },
    "pepsi": {
        "name": "Pepsi amerikanskiy",
        "price": 3,
        "about": "Amerikada ishlab chiqarilgan pepsi"
    },
    "uzum": {
        "name": "Qora uzum",
        "price": 4,
        "about": "Bog'dan bugun ertalab keldi"
    },
    "go'sht": {
        "name": "Mol go'sti",
        "price": 10,
        "about": "Buqani o'zim so'ydim bugun ertalab ushani go'shti"
    },
    "sabzi": {
        "name": "Sariq sabzi",
        "price": 7,
        "about": "Hamma quyonlar bu sabzilarni orzu qiladi"
    }
}

print("show-products: Hamma mahsulotlarni ko'rish")
print("show-basket: Hamma mahsulotlarni ko'rish")
print("add: Savatga nimadir qo'sish")
print("remove: Savatdan nimanidir olib tashlash")
print("calculate: Savatni hisoblash")
print("checkout: Savatga nimadir qo'sish")
print("check: Checkni chiqarib olish")
print("total: Umumiy shu paytgacha qilgan haridlarni ko'rish")
print("exit: Chiqib ketish")
res = 0
while True:
    option = input("Enter your option: ").strip().lower()
    if option == "show-products":
        res = show_products_nice(products)

    elif option == "add":
        product = input("Product: ")
        res = add(product, products)
        print(show_basket())

    elif option == "remove":
        product = input("Product: ")
        res = remove(product)
        print(show_basket())

    elif option == "calculate":
        total = calculate()
        res = f"Sizning savatingizda {total}$ lik mahsulotlar bo'ldi"

    elif option == "check":
        res = check()
        discount = int(input("Discount: "))
        total = calculate()
        cal_total = total - (total * discount / 100)
        res += f"\n\nChegirma bilan: {cal_total}$\nChegirmasiz: {total}$"

    elif option == "exit":
        print("Xayr salomat bo'ling")
        break

    print(res)
