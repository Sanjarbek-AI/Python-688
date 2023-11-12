import os

if not os.path.exists('688.txt'):
    new_file = open('688.txt', 'x')
    new_file.close()
    print("File is created")

# counter = 1
#
# writer = open('688.txt', 'a')
# while counter <= 100:
#     if counter % 3 == 0:
#         writer.write(f"Sanjarbek\n")
#     else:
#         writer.write(f"{str(counter)}\n")
#     counter += 1
# writer.close()

# write_2 = open('688.txt', 'w')
# write_2.write("Uxlamanglar bollar")
# write_2.close()

# reader = open('688.txt', 'r')
# data = reader.readlines()
# for user in data:
#     print(user)
# print(data)
