"""
1. Butun tipli, 10 ta elementdan iborat list yarating. Maksimal
elementini minimal elementi bilan joyini almashtiring.

2. 10 ta elementdan iborat butun tipli list yarating.
Juft sonlarni eng kattasini toping.

3. 10 ta elementdan iborat butun tipli list yarating.
Toq sonlarni eng kattasini toping.

4. 10 ta elementdan iborat butun tipli list yarating.
juft sonlarni yigindisidan toq sonlarni yigindisini ayiring

5. 10 ta elementdan iborat butun tipli list yarating.
toq indexda turgan sonlarni eng kattasini va juft indexda turgan eng kattasi bilan joyini almashtiring
"""

nums = [12, 44, 56, 7, 77, 65, 32]

toq = 0
juft = 0

for num in nums:
    if num % 2 == 0:
        juft += num
    else:
        toq += num
print(toq - juft)
# juft = []
#
# for num in nums:
#     if num % 2 != 0:
#         juft.append(num)
# print(max(juft))
