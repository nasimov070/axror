# yosh=int(input("yoshizi kiritin:"))
# y=int(input("yilizi krit:"))
# a=yosh+y+10
# print(a)

#2
from math import sqrt
# c=(sqrt(9876))
# t=(c+23)**2
# m=(t/21)
# print(round(m, 3))
# #3
# x=int(input("x:"))
# y=4*(x-3)**5-7*(x-3)**3+2
# print(round(y))

#4
# a=int(input("son kritin:"))
# b=int(input("son kritin:"))
# c=int(input("son kritin:"))
# d=int(input("son kritin:"))
# s=(a**b)/c
# print(round(s, d))
#5
# a=sqrt(round(67365/32, 2 ))
# print(a)
#6
# b=[]
# b.append("olma")
# b.append("torvuz")
# b.append("nok")
# b.append("sabzi")
# print(b)

# b="Hello, word"
# print(b[:5])

# b="He'llo, word"
# print(b[:5])

# b="Hello, word"
# print(b[2:])

# b="Hello, word"
# print(b[-2:5])
# """replace"""
# b="Hello, word"

# """split()"""
# b="Hello, word"
# print(b.split("w"))
# """
# \' belgilash uchun
# \" belgilash ucun
# \n yangi qator
# \r yangi qator
# \t tab tashlab beradi
# \b boshqilni yoqatib beradi
# """
# """sonlarni turlari"""

# x=1 #int
# y=2.2 #float
# z=1j# complex

# """butun son turlari"""
# a=15
# b=-8
# c=0
# print(a)
# print(type(a))

# """onlik son"""
# x=35e2
# y=12E4
# z=14.76
# print(z)
# print(type(z))

# from math import pow
# print(pow(3, 4))

# print(3**4)

# print(round(120525.24850 , 2))

1#
# a=int(input("yoshizi kiritin:"))
# c=2024-a
# print(c)

2#
# a=int(input("son kirit:"))
# print(a**2)
# print(a**3)

3#
# a=int(input("son kirit:"))
# p=a*4
# s=a**2
# print(p, s)

4#
from math import sqrt
# a=int(input("son kirit:"))
# b=int(input("son kirit:"))
# print(round(sqrt(a**2+b**2)))

5#
# a=int(input("son kirit:"))
# pi=int(input("son kirit:"))
# r=int(input("son kirit:"))

# a=2*pi*r
# pi=3.14
# r=a+pi
# print(a)

# x=int(input("son kirit:"))
# y=4*(x-3)**5-7*(x-3)**3+2
# print(y)

# a=int(input("son kirit:"))
# b=int(input("son kirit:"))
# s=a
# a=b
# b=s
# print(a)
# print(b)

# print(231/4.7)

# mevalar=["olma","glos","orik","olcha"]
# print(mevalar)

# son=[2,6,-5]
# print(son[0]*son[2])
# x=son[0]+son[1]
# print(x)
1#
ismlar=[]
ismlar.append("axmad")
ismlar.append("yusuf")
ismlar.append("nuri")
ismlar.append("mansur")
print(ismlar)
for ism in ismlar:
    print(f"salom dostim {ism}")
2#
son=[2, 6, -5, 25, 22, -333]
print(son[0] * son[2])
print(son[1] + son[2])
print(son[2] - son[2])
son[-1]=63
print(son)
3#
mevalar=["olma","glos","orik","olcha"]
evalar=["lma","los","rik","lcha"]
mevalar.extend(evalar)
print(evalar)

del mevalar[1]
print(mevalar)
4#
s=["mur","sur","chur"]


print(s)
print(sorted(s))
print(sorted(s, reverse=True))

s.reverse()
print(s)

dav=["namangan","anjon","lola","jamashu","amerika","istanbul"]
print(dav)
print(sorted(dav))
print(sorted(dav, reverse=True))
print(len(dav))
dav.sort()
print(dav)


for ism in ismlar:
    print(f"salom dostim {ism}")



