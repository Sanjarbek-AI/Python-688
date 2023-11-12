def send_money(cards: dict):
    card = input("Enter card number: ")
    if card in cards.keys():
        password = int(input("Password: "))
        if password == cards[card]['password']:
            card_to = input("Enter card number: ")
            if card_to in cards.keys():
                amount = int(input("Amount: "))
                percent = amount / 100
                amount += percent
                if cards[card]['money'] >= amount:
                    cards[card]['money'] -= amount
                    cards[card_to]['money'] += amount
                    file = open('data.txt', 'a')
                    file.write(f"{card}${card_to}${amount}${percent}\n")
                    file.close()

                    return "Money is sent"
                else:
                    return "You don't have enough money"
            else:
                return "There is no such card number"
        else:
            return "Password is not correct"
    else:
        return "There is no such card number"


def show_history(cards: dict, card_number):
    text = ""
    with open('data.txt', 'r') as reader:
        payments = reader.readlines()

        return text
