def show_money(cards):
    card = input("Enter card number: ")
    if card in cards.keys():
        password = int(input("Password: "))
        if password == cards[card]['password']:
            return cards[card]['money']
        else:
            return "Password is not correct"
    else:
        return "There is no such card number"


def change_password(cards):
    card = input("Enter card number: ")
    if card in cards.keys():
        password = int(input("Password: "))
        if password == cards[card]['password']:
            new_pass = int(input("New password: "))
            cards[card]['password'] = new_pass
            return "Your password is updated"
        else:
            return "Password is not correct"
    else:
        return "There is no such card number"


def minus_from_bank(amount: int, bank):
    while amount > 0:
        if amount >= 200000:
            amount -= 200000
            bank['200000'] -= 1

        if amount >= 100000:
            amount -= 100000
            bank['100000'] -= 1

        if amount >= 50000:
            amount -= 50000
            bank['50000'] -= 1

        if amount >= 20000:
            amount -= 20000
            bank['20000'] -= 1

        if amount >= 10000:
            amount -= 10000
            bank['10000'] -= 1

        if amount >= 5000:
            amount -= 5000
            bank['5000'] -= 1

        if amount >= 2000:
            amount -= 2000
            bank['2000'] -= 1

        if amount >= 1000:
            amount -= 1000
            bank['1000'] -= 1
    else:
        return bank


def get_money(cards, bank):
    card = input("Enter card number: ")
    if card in cards.keys():
        password = int(input("Password: "))
        if password == cards[card]['password']:
            amount = int(input("How much: "))
            if cards[card]['money'] >= amount:
                cards[card]['money'] -= amount
                back_bank = minus_from_bank(amount, bank)
                return "This is your money", back_bank
            else:
                return "You don't have enough money"
        else:
            return "Password is not correct"
    else:
        return "There is no such card number"
