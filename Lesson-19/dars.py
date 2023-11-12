# import os
#
# if not os.path.exists('ismoil.txt'):
#     with open('ismoil.txt', 'x'):
#         pass
#
# with open('ismoil.txt', 'w') as writer:
#     writer.write("Ismoil")
#
# with open('ismoil.txt', 'a') as appender:
#     appender.write("Ismoil")
#
# with open('ismoil.txt', 'r') as reader:
#     data = reader.read()
#     print(data)


with open('ismoil.txt', 'r') as reader:
    fruits = reader.read()
    fruit = input("Fruit: ")
    if fruit in fruits:
        print(True)
    else:
        print(False)