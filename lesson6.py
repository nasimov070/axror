# """
# == ten
# != ten bolmasa
# > katta 
# < kichik
# >= kata yoki teng
# <= kichik yoki teng
# or yoki
# and va

# """
# """elif"""
# s=[2,415,5,545,45,45,4,15,41515,4512,1451202,145102,0,120,214]
# for a in s:
#     if s < 5:
#         print(f"{s} 5 ")
#     if s > 5:
#         print(f"{s} 5 ")

# a1=int(input("son krit:"))
# a2=int(input("son krit:"))
# if a1 > a2:
#     print(f"{a1} > {a2}")
# elif a1 < a2:
#     print(f"{a1} < {a2}")
# else:
#  print(f"{a1} = {a2}")


# ism=["ali","vali","kamron","imron"]
# for s in ism:
#     if s=="kamron" or "imron":
#         print(f"{s} nmagap")
# else:
#    print(f"{s} o vatsab nmagap")

# m=["olma","gulos","bihi","qalampir", "osqavoq"]
# for a in m:
#     if a=="osqavoq" or a=="bihi":
#         print(f"{a.upper()}")
#     else:
#         print(f"{a.lower()}")
        
# boxo=int(input("baxoni kiritin:"))
# if boxo==5:
#     print(f"{boxo} alo")
# elif boxo==4:
#     print(f"{boxo} yaxshi")
# elif boxo==3:
#     print(f"{boxo} qoniqarli")
# elif boxo==2:
#     print(f"{boxo} qoniqarsz")
# elif boxo==1:
#     print(f"{boxo} yomon")
# else:
#     print("hato son kiritiz")
    
# print("Dokonimizga Xush kelibsiz ")
# print("Buzda quydagi mahsulotlar bor ")
# m=["olma","anor","non","shakar","tuz","qaymoq"]
# bor =[]
# yoq =[]
# n=int(input("Neshta maqsulot sotib olmoqchisiz:"))
# for s in range(n):
#     if s in m:
#         print(f"{m} shular bor")
    
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

# yosh=int(input("yoshizi kiritin:"))
# if 1<=yosh<=7:
#     print(f"{yosh}-yoshiz silaga bepul")
# elif 8<=yosh<=18:
#     print(f"{yosh}-yoshiz 5_000-sum")
# elif 19<=yosh<=69:
#     print(f"{yosh}-yoshiz 10_000-sum")
# elif 70<=yosh<=100:
#     print(f"{yosh}-yoshiz bepul")
# else:
#     print("xato yosh kiritz sz olgansz")

# parol=input("parol kiritin:")
# if len(parol)>=8:
#     paroll=input("parol:")
#     if paroll==parol:    
#         print("to'g'ri o'rnatildi")
#         paro=input("qayta parol kiritin:")
#         if paroll==paro:
#             print("tizimga to'g'ri kirdiz")
#     else:
#         print("Parol birbiriga mos tushmadi")
    
# else:
#     print("Parol Xato 8-xonalik bolishi shart")   

# cars=["toyota","gelig","gm","gentra"]
# for car in cars:
#     if car !="gm":
#         print(f"{car.upper()}")
#     else:
#         print(car.capitalize())

# yosh=int(input("yoshizi kiritin:"))
# if yosh==15:
#     o=input("ogil yoki qz bolamisz").lower()
#     if o=="qiz":
#         print("sz green da uqisz:")
#     elif o=="ogil":
#         print("sz blue da uqiysz")
# else:
#     print("15-yosh bolishiz kk ")                        


# yosh=input("yoshizi kiritin:")
# if bool(yosh):
#     print("raxmat")
# else:
#     print("yoq")



# ota={
#     "ism":"olim",
#     "yosh":98,
#     "manzil":"amerika",
#     "familiya":"pistonchiev",
# }
# print(f"otamning ismi {ota["ism"]} yoshi {ota["yosh"]} manzili {ota["manzil"]} familiyasi  {ota["familiya"]}   ")

# ona={
#     "ism":"sir",
#     "yosh":98,
#     "manzil":"amerika",
#     "familiya":"sir",
# }
# print(f"onamning ismi {ona["ism"]} yoshi {ona["yosh"]} manzili {ona["manzil"]} familiyasi  {ona["familiya"]}   ")

# uka={
#     "ism":"axi",
#     "yosh":98,
#     "manzil":"amerika",
#     "familiya":"toshpolatov",
# }
# print(f"ukamning ismi {uka["ism"]} yoshi {uka["yosh"]} manzili {uka["manzil"]}  familiyasi {uka["familiya"]}   ")
# aka={
#     "ism":"yoq",
#     "yosh":98,
#     "manzil":"amerika",
#     "familiya":"pistonchiev",
# }
# print(f"akamning ismi {aka["ism"]} yoshi {aka["yosh"]} manzili {aka["manzil"]}  familiyasi {aka["familiya"]} " )


# py={
#     "int":"butun son",
#     "inut":"sorash",
#     "float":"unlik son",
#     "del":"uciradi",
#     "print":"konsulga ciqaradi",
# }
# print(py)

# py={
#     "int":input("key kiritin"),
#     "input":input("key kiritin"),
#     "print":input("key kiritin"),
# }
# print(py)

# del py["int"]
# print(py)
# py.pop("input")


# py["kil"]="orin"
# py.update({"olim":"baliq"},)

# print(py)

# m=py.copy()
# ma=dict(py)
# for key, value in py.items():
#     print(f"{key.title()} {value.title()}" )

menu={
    "osh porsi":12000,
    "lagmon":17000,
    "seryoqli baliq":3520001211451158475213252151,
    "besh teks":3000000
}
b=int(input("3ta ovqat kiritin:"))
if b==3:
    print("xaqat 3 ta kiritin")
for k,y in b:
    if b==k:
        print(y)
    if b==y:
        print(k) 
  
if b  not in menu.keys():
    print("bizda bunday ovqat yoq")   




