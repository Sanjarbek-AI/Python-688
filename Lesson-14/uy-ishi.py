"""
1. Ism:Yosh qilib dict yarating. Huddi darsda qilganimizdaki qilib.
   Sizni vazifangiz eng yosh 3 tasini topish.

2. Odamni ismini key familiyasini value qilib saqlaydigan dict yarating
   va uni ichida kamida 5 ta odam bolsin. Keyin odamdan familiyasini input
   qilib sorang, agar shunaqa familiya value larni ichida bor bolsa
   True chiqsin yoq bolsa False

3. Tasavvur qiling siz o'quvchilarni matabdagi fanlardan baholarni dictda
   saqlayapsiz. Sizni vazifangiz odamdan ismini va fan nomini input qilib
   sorash. Agar shunaqa ismli bola dictni ichida bor bolsa va uni shunaqa
   fanli malumoti bor bolsa usha fandan olgan bahosini 5 qilib qoyasiz
   Agar unaqa fan yoki oquvchi yoq bolsa bunday malumot topilmadi deysiz.
"""

students = {
    "ali": {
        "kimyo": 3,
        "fizika": 5
    },
    "vali": {
        "jt": 4,
        "mehnat": 4
    },
    "gani": {
        "fizika": 2,
        "ingliz": 2
    }
}

name = input("name: ")
if name in students.keys():
    subject = input("Subject: ")
    if subject in students[name].keys():
        print(students[name][subject])
    else:
        print("bunday fan yo'q")
else:
    print("bunday mohov yo'q")

# names = {
#     "ali": "aliyev", "vali": "valiyev", "gani": "domlayev"
# }
#
# last_name = input("Enter your last name: ")
#
# if last_name in names.values():
#     print(True)
# else:
#     print(False)

# people = {"ali": 112, "vali": 2, "gani": 0, "sanjar": 22}
#
# ages = people.values()
# ages = sorted(ages)
# print(ages[:3])
