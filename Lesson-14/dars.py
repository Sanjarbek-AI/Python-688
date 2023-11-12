ages = {
    "ali": 20, "vali": 12, "gani": 100
}

teenagers = dict()
adults = dict()

for name, age in ages.items():
    if age >= 18:
        adults[name] = age
    else:
        teenagers[name] = age
print(teenagers)
print(adults)
# num = 1
#
# while num <= 3:
#     print(ages)
#     name = input("Name: ")
#     age = int(input("Age: "))
#
#     if name not in ages.keys():
#         ages[name] = age
#     else:
#         print("Bunday ismli odam bor")
#
#     num += 1


# keys = ages.keys()
# values = ages.values()
# items = ages.items()
#
# print(keys)
# print(values)
# print(items)
