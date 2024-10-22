while True:
    son=int(input("son kiritin:"))
    print(f"{son} ning kvadrati {son**2}")

    sovol=input("davom etamizmi (yes/no)")
    if sovol=="yes":
        continue
    elif sovol=="no":
        break
    else:
        print("siz notugri son kiritiz:")
    