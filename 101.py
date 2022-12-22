import random
print("Podaj imie")
imie = input()

komputer_los = ["kamien", "papier", "norzyce"]
while True:
    print("Witaj",imie, "w grze kamien, papier, norzyce")
    gracz = input("Co chcesz wylozyc : kamien, papier, norzyce  lub (zakoncz):")
    komputer = random.choice(komputer_los)
    if gracz == "zakoncz":
        print("koniec")
        break
    elif gracz == "kamien" and komputer == "norzyce":
        print(f"komputer wylozyl {komputer}")
        print("wygrales")
    elif gracz == "kamien" and komputer == "papier":
        print(f"komputer wylozyl {komputer}")
        print("przegrales")
    elif gracz == "papier" and komputer == "norzyce":
        print(f"komputer wylozyl {komputer}")
        print("przegrales")
    elif gracz == "papier" and komputer == "kamien":
        print(f"komputer wylozyl {komputer}")
        print("wygrales")
    elif gracz == "norzyce" and komputer == "kamien":
        print(f"komputer wylozyl {komputer}")
        print("przegrales")
    elif gracz == "nozyce" and komputer == "papier":
        print(f"komputer wylozyl {komputer}")
        print("wygrales")

    if gracz == "kamien" and komputer == "kamien":
        print(f"komputer wylozyl {komputer}")
        print("remis")
    elif gracz == "norzyce" and komputer == "norzyce":
        print(f"komputer wylozyl {komputer}")
        print("remis")
    elif gracz == "papier" and komputer == "papier":
        print(f"komputer wylozyl {komputer}")
        print("remis")







