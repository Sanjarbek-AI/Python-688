basket = dict()


def show_products_nice(products: dict):
    text = ""
    for name, values in products.items():
        text += f"{name} \t | "
        for value in values.values():
            text += f"{value} \t| "

        text += "\n"
    return text


def add(product: str, products: dict):
    if product in products.keys():
        price = products[product]['price']
        name = products[product]['name']
        print(f"Narxi: {price}")
        kg = int(input("Qancha sotib olmoqchisiz: "))
        basket[product] = {
            "name": name,
            "price": price,
            "kg": kg,
            "total": kg * price
        }
        return "Savatga qo'shildi"
    else:
        return "Bunday mahsulot mavjud emas !"


def remove(product: str):
    if product in basket.keys():
        basket.pop(product)
        return "Mahsulot chopildi"
    else:
        return "Savatda bunday mahsulot mavjud emas."


def show_basket():
    text = ""
    for name, values in basket.items():
        for value in values.values():
            text += f"{value} \t| "
        text += "\n"
    return text


def calculate():
    total = 0
    for value in basket.values():
        total += value['total']
    return total


def check():
    text = ""
    counter = 1
    for value in basket.values():
        text += f"{counter}) {value['name']} -- {value['kg']} ta -- {value['price']}$ -- {value['total']}$ \n"
        counter += 1
    return text