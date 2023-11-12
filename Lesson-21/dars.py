# def find_old(names: dict):
#     old_name = ""
#     old_age = 0
#
#     for name, age in names.items():
#         if age > old_age:
#             old_age = age
#             old_name = name
#     return old_name
#
#
# people = {
#     "ali": 10, "vali": 200, "gani": 100
# }
#
# res = find_old(people)
# print(res)

# def set_test(nums: set):
#     even_nums = set()
#     for num in nums:
#         if num % 2 == 0:
#             even_nums.add(num)
#     return even_nums
#
#
# numbers = {3, 53, 6, 7745, 35, 3, 453, 2}
# res = set_test(nums=numbers)
# print(res)
#
# names = set()
# counter = 0
# while counter < 5:
#     name = input("Name: ")
#     names.add(name)
#
#     counter += 1
#
#
# def find_a(names_set: set):
#     max_a = ""
#     for name_set in names_set:
#         if name_set.count("a") > max_a.count("a"):
#             max_a = name_set
#     return max_a
#
#
# res = find_a(names_set=names)
# print(res)

def check_password(password: str):
    errors = list()

    if len(password) < 8:
        text = "Uzunligi kamida 8 ga teng bo'lsin"
        errors.append(text)
    if not password.isalnum():
        text = "Passwordda ham raqam ham harf bo'lishi shart"
        errors.append(text)
    if password == password.lower():
        text = "Kamida bitta harf katta bo'lsin"
        errors.append(text)
    return errors


res = check_password("Sca121212121")
print(res)
