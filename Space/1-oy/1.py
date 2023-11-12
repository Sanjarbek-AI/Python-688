name = tuple(input("name: "))
name = tuple(name)

more_letter = name.count(name[0])
char = ""
for letter in name:
    count = name.count(letter)
    if count > more_letter:
        more_letter = count
        char = letter
print(char, more_letter)