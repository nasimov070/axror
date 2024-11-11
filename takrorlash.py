"""001"""
# ism=input("kiritin:")
# fam=input("kiritin:")
# yosh=int(input("yosh-kiritin:"))
# ktob=input("kiritin:")
# print(type(ism))
# print(type(fam))
# print(type(yosh))
# print(type(ktob))
from math import sqrt
# """2"""
# a=4364+1233
# print(sqrt(a))
# print(round(a))
"3"
# yosh=int(input("kiritin:"))
# yosh1=int(input("kiritin:"))
# print(round(yosh**2 + yosh1**2/23))

# """4"""
# son=input("btun kiritin:")

# son = int(son)
# print(type(son))

# son = float(son)
# print(type(son))

# # "5"
# k=[]

# for a in range(5):
#     i=input(f"{a+1} ktobi nomini kiritin:")
#     k.append(i)
# print(k)


# "6"
# ismlar=["ali","vali","olim"]
# ismlar.insert(0,"klo")
# ismlar.insert(2,"aalo")
# ismlar[0]="olimtoy"



"""002"""

# "1"
from random import randrange
# a=int(input("son kiritin:"))
# s=int(input("son kiritin:"))
# print(randrange(a,s))

# "2"
# k=[]

# for a in range(5):
#     i=input(f"{a+1} ktobi nomini kiritin:")
#     k.append(i)
# print(k)

# del k[0]
# print(k)
# k.insert(0,"klo")
# print(k)
# k.insert(2,"aalo")
# print(k)

# "3"
# fanlar=["oq", "qora"]
# print(fanlar)
# fanlar.insert(0,"klo")
# print(fanlar)
# fanlar.append("axr")
# print(fanlar)
# fanlar[0]="olimtoy"
# print(fanlar)
# fanlar[0]="toy"
# print(fanlar)

# del fanlar[0]
# print(fanlar)
# fanlar.remove("axr")
# print(fanlar)
# fanlar.pop()
# print(fanlar)
# s=[]
# s=fanlar.copy()
# print(s)
# s.clear()
# print(s)

"4"
# oy=[]
# oila=int(input("oilada nechta odamszlar:"))
# for a in range(oila):
#     s=input(f"{a+1} ismilari:")
#     oy.append(s)
# print(oy)

# "5"
# m=["tiko","damas","volga","taxoe","jip"]
# print(len(m))
# m.sort()
# print(m)
# print(sorted(m))
# m.reverse()
# print(m)


"""004"""
# "1"
# son=[12,324,65,76,899,7,4687,8645,0,-54]
# print(son)
# son.sort()
# print(son)
# son.sort(reverse=True)
# print(son)

# "2"
# mevalar=["olma","nok","malina","apelsi",]
# for meva in mevalar:
#     if meva=="olma" or meva=="malina":
#         print(meva.upper())
#     else:
#         print(meva.capitalize())

"3"
# bok={
#     "ali":input("kritin:"),
#     "toib":input("kritin:"),

# }    
# bok["ali"]="yusuf"
# bok.update({"tolib":input("kritin:")})

# del bok[0]
# print(bok)
# bok.pop("yusuf")
# print(bok)
# bok.popitem()
# bok.clear()
# print(bok)
# "4"
# son=list(range(102, 2019))
# for s in son:
#     if s<=1000:
#         print(son**3)
#     elif s>1500:
#         print(s-4)

#     if s%7==0:
#         print(sqrt(s))
# "5"
# im=int(input("orin:"))
# yosh=int(input("bal kiritin:"))
# if 0<=yosh<=100:
#     if 0<=yosh<=64:
#         print(f"otmadiz")
#     elif 65<=yosh<=85:
#         print(f"otdiz")
#     elif 85<=yosh<=100:
#         if im==1:
#             print("sz 100% grand yutiz")
#         elif im==2:
#             print("sz 75% grand yutiz")
#         elif im==3:
#             print("sz 50% grand yutiz")
#         elif im==4:
#             print("sz 25% grand yutiz")
#         else:
#             print("sz gtand yoq")


# """005"""
# l={
#     "if":"agar",
#     "else":"yoki",
#     "for":"sikil",

# }
# a=input("soz kiritin:")
# for k,y in l.items():
#     if a==k:
#         print(f"{k} ning tarjimasi {y}")
#     elif a==y:
#         print(f"{y} ning tarjimasi {k}")

# if a  not in l.keys() and a not in l.values():
#     print("bizda bunday soz yoq")   



# "2"
# menu={
#     "osh porsi":12000,
#     "lagmon":17000,
#     "seryoqli baliq":3520001211451158475213252151,
#     "besh teks":3000000
# }

# for k in menu.keys():
#     print(k)

# for k,y in menu.items():
#     print(f"{k} - {y}")

"3"
# yosh=int(input("yoshizi kiritin:"))
# if 1<=yosh<=6:
#     print(f"{yosh}-boxcha")
# elif 7<=yosh<=17:
#     print(f"{yosh}-mak")
# elif 18<=yosh<=30:
#     print(f"{yosh}-unvr")
# elif 31<=yosh<=100:
#     print(f"{yosh}-olgansz")
# else:
#     print("xato yosh kiritz sz olgansz")

# "4"
# ota={
#     "ism":"olim",
#     "yosh":98,
#     "manzil":"amerika",
#     "familiya":"pistonchiev",
# }
# print(f"otamning ismi {ota["ism"]} yoshi {ota["yosh"]} manzili {ota["manzil"]} familiyasi  {ota["familiya"]}   ")


"g 003"

# "1"
from random import randrange
# a=int(input("son kiritin:"))
# s=int(input("son kiritin:"))
# print(randrange(a,s))

# "2"
# k=[]

# for a in range(5):
#     i=input(f"{a+1} ktobi nomini kiritin:")
#     k.append(i)
# print(k)

# del k[0]
# print(k)
# k.insert(0,"klo")
# print(k)
# k.insert(2,"aalo")
# print(k)

# "3"
# fanlar=["oq", "qora"]
# print(fanlar)
# fanlar.insert(0,"klo")
# print(fanlar)
# fanlar.append("axr")
# print(fanlar)
# fanlar[0]="olimtoy"
# print(fanlar)
# fanlar[0]="toy"
# print(fanlar)

# del fanlar[0]
# print(fanlar)
# fanlar.remove("axr")
# print(fanlar)
# fanlar.pop()
# print(fanlar)
# s=[]
# s=fanlar.copy()
# print(s)
# s.clear()
# print(s)
        
"4"
# oy=[]
# oila=int(input("oilada nechta odamszlar:"))
# for a in range(oila):
#     s=input(f"{a+1} ismilari:")
#     oy.append(s)
# print(oy)

# "5"
# m=["tiko","damas","volga","taxoe","jip"]
# print(len(m))
# m.sort()
# print(m)
# print(sorted(m))
# m.reverse()
# print(m)


"004"
# m=[]
# a=int(input("son kiritin:"))
# s=int(input("son kiritin:"))
# b=int(input("son kiritin:"))
# m.append(s)
# m.append(b)
# m.append(a)

# print(max(m))
# print(min(m))
# print(sum(m))
"2"
# son=[12,324,65,76,899,7,4687,8645,0,-54]
# print(son)
# son.sort()
# print(son)
# son.sort(reverse=True)
# print(son)
"3"
# mevalar=["olma","nok","malina","apelsi",]
# for meva in mevalar:
#     if meva=="olma" or meva=="malina":
#         print(meva.upper())
#     else:
#         print(meva.capitalize())
"4"
# m=[]
# son=int(input("neshta:"))
# for s in range(son):
#     l=input(f"{s+1} mevani nomi:")
#     m.append(l)
# print(m)

# "5"
# a=int(input("son kiritin:"))
# s=int(input("son kiritin:"))
# if a>s:
#     print(f"{a} > {s}")
# elif a<s:
#     print(f"{a} < {s}")
# else:
#     print(f"{a} = {s}")

"""005"""
son=list(range(3,873,2))   
print(son)
for s in son:
    print(sqrt(s))
"3"
# "4"
# son=list(range(102, 2019))
# for s in son:
#     if s<=1000:
#         print(son**3)
#     elif s>1500:
#         print(s-4)

#     if s%7==0:
#         print(sqrt(s))
"4"
# son=list(range(-3,-323,2))   
# print(son)
# for s in son:
#     print(f"{s**7} {s**5}")
# "5"
# a=int(input("son kiritin:"))
# s=int(input("son kiritin:"))
# if a>s:
#     print(f"{a} > {s}")
# elif a<s:
#     print(f"{a} < {s}")
# else:
#     print(f"{a} = {s}")


