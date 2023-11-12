"""
1. O'yinchilarni achkolarini hisoblaydigan dict yarating. Key ularni ismi bo'ladi value nechi achkosi borligi.
   odamdan 10 martta input sifatida ismini soraysiz va usha ismli o'yinchii achkosini birga oshirib qoyasiz, Oxirida
   dictni print qilib qo'yasiz.

2. Oila a'zolarini ismlarnikey qilib ular haqida quyidagi ma'lumotni dict qilib value qilib saqlang

"""
family = {
    "Ravshan": {
        "bo'y": 175,
        "ism": "Ravshan",
        "familiya": "Oxunov",
        "yosh": 44
    },
    "Lola": {
        "bo'y": 165,
        "ism": "Lola",
        "familiya": "Oxunova",
        "yosh": 41
    }
}

players = {
    'ali': 10,
    'vali': 1,
    'gani': 0,
}

num = 0
while num < 10:
    print(players)
    name = input("Your name: ")
    if name in players.keys():
        players[name] += 1
    else:
        players[name] = 1
    num += 1
