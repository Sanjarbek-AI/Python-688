import os

if not os.path.exists('nom.txt'):
    new_file = open('nom.txt', 'x')
    new_file.close()

text = input("Text: ")
writer = open('nom.txt', 'w')
writer.write(text)
writer.close()

reader = open('nom.txt', 'r')
data = reader.read()
alpha = ""
numbers = ""

for letter in data:

    if letter.isalpha():
        alpha += letter
    elif letter.isdigit():
        numbers += letter
reader.close()

print(alpha, numbers)
