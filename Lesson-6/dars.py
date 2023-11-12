number = input("Enter number: ")

num1 = int(number[0])
num2 = int(number[-1])
summa = num1 + num2

if summa % 2 == 0:
    print("Juft son")
else:
    print("Toq son")
