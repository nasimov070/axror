print("Assalomu alekum Axrorbek ning dasturiga xuw keldiz")
# def solom_ber():
#     ism=input("isim kiritin:")
#     print(f"Assalomu alekum {ism.lower()}")

# def mawq_a():
#     ism=input("isim kiritin:")
#     print(f"ismim {ism}")
#     yow=int(input("yow kiritin:"))
#     print(f"{2024-yow}")
#     yow=int(input("yow kiritin:"))
#     print(f"{yow**2} {yow**3}")

# # mawq_a()
# from math import sqrt
# def ildiz(son):
#     print(f"siz kiritgan {son} ning {sqrt(son)} ga teng")
# ildiz(225)
# ildiz(625)
# ildiz(1000)

# def mawq_a(son , son1):
#     """katta kicikini topadi"""

#     if son > son1:
#         print(f"{son} > {son1}")
#     elif son < son1:
#         print(f"{son} < {son1}")
#     else:
#         print(f"{son1} = {son1}")
# mawq_a(1, 2)



# "imitxon"
# def ism():
#     ism=input("ism kritin:")
#     t=int(input("tugilgan yilizi kritin:"))
#     print(f"Salom {ism}, Siz {t} da tugilgansz va sz {2024-t} dasz")
# ism()

# "2"
# def sabo():
#     ism=input("ism kritin:")
#     familiya=input("familiya kritin:")
#     warif=input("warif kritin:")
#     print(f"Salom {ism}, Sizning toliq ismiz {ism} {familiya} sz {warif} oglisz")
# sabo()
# "3"
# def guli(son):
#     print(f"{son} ning kvadrati {son**2}")
# guli(5)

# def guli(son1):
#     print(f"{son1} ning kubi {son1**3}")
# guli(5)

# "4"
# x=[]
# def pr():
#     i=int(input("son kiritin:"))
#     l=list(range(0,{i} ))
#     for a in l:
#         if a%2==0:
#             x.append(a)
#             print(a)
# pr()
"1"
# from math import sqrt
# son =list(range(10, 201))
# print(son)
# for s in son:
#     if s<=100:
#         print(s**3)
#     elif s>150:
#         print(sqrt(s))
#     if s%5==0:
#         print(s)
"2"
# i=["axror","mansur"]
# a=input("ism kiritin:")
# if a==i:
#     print("gurixga xuw keldz")
# else:
#     print("gurixda borsz")
# "3"
# while True:
#     son1=input("son1 kiritin:")
#     if son1=="quit" or son1=="stop":
#         break
#     son2=input("son2 kiritin:")
#     if son2=="quit" or son2=="stop":
#         break 
#     if son1.isdigit() and son2.isdigit():
#         if son1 > son2:
#             print(f"{son1} > {son2}")
#         elif son1 < son2:
#             print(f"{son1} < {son2}")
#         else:
#             print(f"{son1} = {son2}")
# "4"
# while 1:
#     a=input("yilizi kiritin:")
#     if a=="xa" or a=="yoq":
#             break
#     if a.isdigit():
#         print(f"{2024 - int(a)}")
# Juft va toq sonlarni ajratib olish dasturi

# def ajrat(sonlar):
#     juft_sonlar = []
#     toq_sonlar = []
    
#     for son in sonlar:
#         if son % 2 == 0:
#             juft_sonlar.append(son)
#         else:
#             toq_sonlar.append(son)
    
#     return juft_sonlar, toq_sonlar





# print(len.__doc__)
# print(range.__doc__)
# print(sum.__doc__)
# print(max.__doc__)
# print(list.__doc__)

    
# max=int(input(":"))
# t=[]
# for s in range(2, max+1):
#     tub =True
    
#     for i in range(2,s):
#         if s% i==0:
#             tub=False
#             break

#     if tub:
#         t.append(s)
# print(t)

# def balgi_son(matn):
#     return len(matn)
# natija=balgi_son("salom")

                                                                            
# def doira(r):
#     pi=3.2131
#     return 2* pi *r

# natija=doira(7)

# def full_name(i,s):
#     ism = f"{i} {s}"
#     return ism

# ism= full_name("a","x")
# print(ism)
# "3"
                                                                            
# def doira(r):
#     pi=3.2131
#     return 2* pi *r

# natija=doira(7)
# "4"
# max=int(input(":"))
# t=[]
# for s in range(2, max+1):
#     tub =True
    
#     for i in range(2,s):
#         if s% i==0:
#             tub=False
#             break

"""1-mashq"""
# def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email=None, telefon=None):
#     hozirgi_yil =2024
#     yosh = hozirgi_yil - tugilgan_yil
#     malumot = {
#         "Ism": ism,
#         "Familiya": familiya,
#         "Tug'ilgan yil": tugilgan_yil,
#         "Tug'ilgan joy": tugilgan_joy,
#         "Yosh": yosh,
#         "Email": email,
#         "Telefon": telefon
#     }
#     return malumot

# print(foydalanuvchi_malumotlari("Ali", "Valiyev", 1990, "Toshkent", email="nasimovaxrors@gmail.com"))
"""2-mashq"""
# def eng_kichik_son(a, b, c):
#     if a <= b and a <= c:a
#         return a
#     elif b <= a and b <= c:
#         return b
#     else:
#         return c
# print(eng_kichik_son(5, 3, 9))
"""3-mashq"""
# import math

# def aylana_malumotlari(radius):
#     diametr = 2 * radius
#     uzunlik = 2 * math.pi * radius
#     yuza = math.pi * (radius ** 2)
#     malumot = {
#         "Radius": radius,
#         "Diametr": diametr,
#         "Perimetr": uzunlik,
#         "Yuza": yuza
#     }
#     return malumot
# print(aylana_malumotlari(5))
"""4-mashq"""
# def tub_sonlar(oraliq_min, oraliq_max):
#     tub_sonlar = []
#     for n in range(max(2, oraliq_min), oraliq_max + 1):
#         is_tub = True
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 is_tub = False
#                 break
#         if is_tub:
#             tub_sonlar.append(n)
#     return tub_sonlar

# print(tub_sonlar(1, 100))

"1"
# def brinci(matn):
#     """brinci xarifi katta qilib beradi"""
#     matn=matn.title()
#     return matn
# natija=brinci("salom")
# print(natija)
# "2"
# def soni(son):
#     """uzatilgan sonnig toq juft ligi"""
#     if son%2==0:
#         natija= f"{son} -juft son"
#     else:
#         natija= f"{son} -toq son"
#     return natija
# s=soni(2)
# print(s)
# s2=soni(3)
# print(s2)

# "3"
# son=[1546,51121,21,4140,14,2410,0,-112]
# def our_min(son):
#     son=min(son)
#     return son
# natija=our_min(son)
# print(natija)

# "4"
# son=[1546,51121,21,4140,14,2410,0,-112]
# def s(sonlar):
#     """uzatilgan """
#     ajratib=[]
#     for sa in sonlar:
#         if sa >0:
#             if sa%2==0:
#                 ajratib.append(sa)
#     return ajratib
# natija=s(son)
# print(natija)
# "5"
# def malumot_ber(b,m,p,old,orqa,y):
#     malumot={
#         "brend":b,
#         "model":m,
#         "prosesir":p,
#         "old kamera":old,
#         "orqa kamera":orqa,
#         "yil":y
#     }
#     return malumot

# natija=malumot_ber("samsun","a7","ddr7","201","120m.p","2001")
# for k,y in natija.items():
#     print(f"{k}:{y}")


# def baxola(ismlar):
#     baxolar={}
#     while ismlar:
#         ism = ismlar.pop()
#         baxo=input(f" baxosi {ism.title()}")
#         baxolar[ism]=baxo
#     return baxolar
# ta=["Ali","valli"]
# baxolar=baxola(ta)
# print(baxolar)
"""1"""
# def parolar(parol:str,paroll:str) ->str:
#     if paroll==parol:    
#         if len(parol)>=8:
#             return "kuchli parol"
#         else:
#             return "kuchsiz parol va 8tada kam"
#     else:
#         return "teng emas"   
# natija=parolar('123456789','123456789')
# print(natija)
"2"
# def malumot_ber(baxo:str,b:int,baxo1:str,m:int)-> dict:
#     malumot={
#         baxo:b,
#         baxo1:m,

  
#     }
#     return malumot

# natija=malumot_ber("axror",30,"axmad",24)
# for k,y in natija.items():
#     print(f"{k}:{y}")



# """MISOLLARR"""
# def my_sum(*sonlar:int)->int:
#     """ """
#     summa=0
#     for son in sonlar:
#         summa=summa +son
#     return summa
# x=my_sum(24,541,65120,5,456,-123)
# y=my_sum(24,54,456,-123)
# z=my_sum(24,541,)
# print(x,y,z)
# "2-mawq"
# ismlar=[]
# def my_sum(*ism:str)->str:
#     """ """
#     for isimlar in ism:
#         ismlar.append(isimlar.lower())   
#     return ismlar
# x=my_sum("axror","mansuR","asedqwadADAS")

# print(x)

# def my_sum(*sonlar:int)->list:
#     """ """
#     summa=0
#     for son in sonlar:
#         summa=summa +son
#     return summa/len(sonlar)
# x=my_sum(24,541,65120,5,456,123)

# print(x)



# Sonlarni tartiblab eng kattasini topish uchun funksiya
def eng_katta_son(numbers):
    # Ro'yxatni tartiblash (kattadan kichikkaga)
    numbers.sort(reverse=True)
    
    # Tartiblangan ro'yxatdan birinchi element eng katta son bo'ladi
    return numbers[0]

# Foydalanuvchidan sonlar ro'yxatini olish
n = int(input("Nechta son kiritmoqchisiz? "))
numbers = []

for i in range(n):
    number = int(input(f"{i+1}-sonni kiriting: "))
    numbers.append(number)

# Eng katta sonni topish
result = eng_katta_son(numbers)

# Natijani chiqarish
print(f"Eng katta son: {result}")




"""funksiya"""
def function_name(yil:int ,name:str):
    """funksiya xaqida malumot"""
    j=f" yowim {yil} ismim {name}"
    return j
print(function_name(2022,"aasd"))