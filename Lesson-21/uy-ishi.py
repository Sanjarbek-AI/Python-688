"""
Uyga vazifa:

1. Odamdan gmail soraash va uni gmail ekanligini tekshirib beradigan funksiya yozing.
   sanjarebksocial@gmail.com => True
   sanjasacasas => False
   sanjarbek@sanjarbek.xom => False

   Faqatgina oxiri @gmail.com bilan tugashi, va ichida faqat bitta @ bolishi kerak.
   oxirni tekshirish uchun string kesib olsangiz boladi, ichida @ nechtaligini topish
   uchun strning ni count() degan metodini ishlatsa boladi.
"""


def check_gmail(email: str):
    errors = list()
    if not email.endswith("@gmail.com"):
        errors.append("Oxiri @gmail.com bilan tugashi kerak")
    if email.count("@") != 1:
        errors.append("Bitta @ bo'lishi kerak")
    if len(email) == 10:
        errors.append("Uzunligi kamida 11 bo'lsin")
    return errors


gmail = input("Gmail: ")
res = check_gmail(email=gmail)
print(res)
