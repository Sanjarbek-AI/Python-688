# # names = {'ali', 'vali', 'gani'}
# #
# # # names.add('mustafo')
# # # names.remove('vali')
# # names.discard('asassasa')
# #
# # print(names)
# family1 = {'ali', 'vali', 'gani'}
# family2 = {'ali', 'sani', 'gani', 'doni'}
#
# common = family1.intersection(family2)
# diff = family1.difference(family2)
# print(diff)
#
# name = "Sanjar"
# name = set(name)
# print(name)
# name1 = set(input("Name1: "))
# name2 = set(input("Name2: "))
#
# print(name1.intersection(name2))

# days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

# print(days[2])
# counter = days.count('monday')
# counter = days.index('wednesday')
# print(counter)
# days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
#
# day = input("day: ").strip().lower()
# if day in days:
#     index = days.index(day)
#     print(days[index - 1])
# else:
#     print("Kozga qarang")
days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

day = input("day : ").strip().lower()

if day in days:
    index = days.index(day)
    print(days[index - 1])
    print(days[index - 6])
else:
    print("None")
