# while True:
#     yosh=int(input("yoshizi kiritin:"))
#     print(f"{yosh} szni yoshiz")
#     sovol=input("davom etamizmi (exit):")
#     if sovol=="exit":
#         break


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

# while 1:
#     a=input("yilizi kiritin:")
#     if a=="xa" or a=="yoq":
#             break
#     if a.isdigit():
#         print(f"{2024 - int(a)}")
 

from math import sqrt
while 5:
    son=input("son kiritin:")
    if son.isdigit():
        print(f"{son} ning ildizi {int(sqrt(son))}") 
    elif son=="net":
        print("dastur tugadi:")
    break


    