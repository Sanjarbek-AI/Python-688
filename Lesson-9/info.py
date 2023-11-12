"""
Bugungi mavzular:

- Barcha mavzularni bitta katta takrorlash qilish

- list bilan ishlashni davom ettirish
- listni yangilashi yaxshilab tushuntirish
- printni qachon qilish kerakligini bollarga yaxshilab tushuntirish
- code yozish stillari va o'zgaruvchilarga nom berishni qo'llash


1. Malumot turlari int, str, float, complex, bool, list
2. Operatorlar: Arifmetik, Taqqoslash, Mantiqiy, A'zolik, Assignment
3. Methodlar, string methodlari, list methodlari
4. for va range, print, input, type, casting, string slicing
"""

"""
Masalalar:

1. Elementlari 14 ta butun son bo`lgan list yarating. Qiymati juft 
bo`lgan elementlari sonini toping. 

2. Elementlari 12 ta butun son bo`lgan list yarating. 5-elementini shu 
list elementlarini eng kattasi bilan alishtirib qo'ying.

3. numbers = [-1, 12, -4, 12, 22, 44, -89, -65, 12, 22, 444, -876, 21]
Ushbu list ichidan faqatgina 0 dan katta bo'lganlarini alohida listga olib chiqing.

4. numbers = [-1, 12, -4, 12, 22, 44, -89, -65, 12, 22, 444, -876, 21]
Ushbu list ichidagi 0 dan kichkina bo'lgan sonlarni yig'indisini toping.

5. Butun tipli, 10 ta elementdan iborat list yarating. Maksimal 
elementini birinchi elementi bilan joyini almashtiring. 

"""
"""
numbers = [-1, 12, -4, 12, 22, 44, -89, -65, 12, 22, 444, -876, 21]

numbers.append(1212)  # listning oxiriga yangi element qo'shadi
numbers.insert(0, 1212)  # yangi elementni index bo'yicha qo'shadi
numbers.index(-1)  # o'ziga berilgan elementni qidiradi topsa indexini qaytaradi
numbers.remove(-1)  # o'ziga berilgan elementni nomi bo'yicha o'chiradi
numbers.pop(0)  # o'ziga berilgan elementni index bo'yicha o'chiradi, agar hech nima bermasa oxiridan o'chiradi
numbers.count(-1)  # o'ziga berilgan elementni list ichida nechta ekanligini sanab qaytaradi

numbers.extend(numbers)  # ikkita list ichidagi elementlarni birlashtiradi
numbers.clear()  # listni barcha elementlarini o'chirib tashlaydi
numbers.sort()  # list ichida sonlar bo'lsa tartib bo'yicha harflar bo'lsa alifbe bo'yicha tartiblab beradi
numbers.reverse()  # listni teskari qilib beradi
numbers.copy()  # listni o'zidan nusxa yasaydi va qaytaradi

"""

"""
name = name.lower() # hammasini kichkina harf qilib beradi
name = name.upper() # hammasini katta qilib beradi
name = name.capitalize() # faqatgina birinchi harfni katta qiladi
name = name.title() # textdagi hamma so'zlarni boshini katta qiladi
name = name.index('MEN') # o'ziga berilgan so'zni nechinchi index ekanligini topib beradi

name = name.count('o') # o'ziga berilgan so'zni string ichida nechta ekanligini sanab beradi
name = name.replace('o', 'Ayubxon') # o'ziga berilgan birinchi element string ichida qidiradi
                                    agar topsa ikkinchi berilgan elementga aylantirib qo'yadi
name = name.strip() # orqa va oldidan bosh joylarni olib tashlaydi
name = name.rstrip() # o'ng tomondan bosh joylarni olib tashlayd
name = name.lstrip() # chap tomondan bosh joylarni olib tashlaydi

name = name.split() # o'ziga berilgan so'z bo'yicha string kesadi va uni list holatda qaytaradi,
                        agar hech nima berilmasa bo'sh joy bo'yicha kesadi
name = name.isalpha() # string faqat harflardan tashkil topganmi yo'qmi tekshiradi
name = name.isdigit() # string faqat sonlardan tashkil topganmi yo'qmi tekshiradi
name = name.isalnum() # string faqat raqam va harflardan tashkil topganmi yo'qmi tekhiradi
name = name.islower() # stringni hamma harflari kichkinami yoki yo'qmi tekshiradi
name = name.isupper() # stringni hamma harflari kattami yoki yo'qmi tekshiradi
name = name.find('elon') # o'ziga berilgan so'zni indexini topadi agar topa olmasa -1 qaytaradi
"""
