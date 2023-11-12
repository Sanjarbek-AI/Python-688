from utils import send_money

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
        "password": 1212
    }
}

while True:
    option = input("Option: ")
    if option == "send-money":
        result = send_money(cards)
        print(result)
        print(cards)
    elif option == "show-history":
        pass

