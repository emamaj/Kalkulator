szukanaLiczba = int(input("Podaj liczbe, ktora mam dla Ciebie znalezc:"))
strzal = 0
while strzal != szukanaLiczba:
    strzal = int(input("odgadnij szukana liczbe:"))
    if (strzal < szukanaLiczba):
        print("Za mala!")
        continue
    elif (strzal > szukanaLiczba):
        print("Za duza!")
        continue
    print("Ostatnie wykonanie petli!")
    print("Brawo! Wygrales")