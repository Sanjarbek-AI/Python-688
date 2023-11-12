from utils import show_money, change_password, get_money

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

print("1. show-money")
print("2. get-money")
print("3. change-password")

while True:
    option = input("Option: ")
    if option == "show-money":
        money = show_money(cards)
        text = f"You have {money} sum in your card."
        print(text)

    elif option == "change-password":
        text = change_password(cards)
        print(text)
        print(cards)

    elif option == "get-money":
        result = get_money(cards, bank)
        new_bank = result[1]
        text = result[0]
        print(text)
        print(bank)
        print(cards)
