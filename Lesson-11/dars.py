# students = {
#     "abror": 16,
#     "umar": 10,
#     "names": ["ali", "vali", "gani"],
#     "score": 10.7,
#     "are_male": True
# }
#
# umar_age = students['umar']
# print(umar_age)

teams = {
    "real": 0, "barca": -1
}

num = 1
while num <= 10:
    print(teams)
    team = input("Team: ")
    if team in teams.keys():
        teams[team] += 1
    else:
        teams[team] = 121
        print("There is no like that team")
    num += 1

# print(teams.keys())
# print(teams.values())
# print(teams.items())
# print(teams.pop('real'))
# print(teams.get('real'))
# print(teams['real'])
