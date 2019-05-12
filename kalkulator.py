print("Prosty kalkulator")
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = int(input("Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 5 - potegowanie: "))
if (c == 1):
    wynik = a + b
elif (c == 2):
    wynik = a - b
elif (c == 3):
    wynik = a * b
elif (c == 4):
    wynik = a / b
elif (c == 5):
    wynik = a ** b

else:
    print("Dodawanie zlego wyboru!")

print("Wynik dzialania to: ", wynik)