print("obliczanie pol figur plaskich")

#definiujemy funkcje odpowiedzialna za wyswietlanie wyniku
def wyswietl(wynik):
    print(wynik)
    return
# W linii 9 wywolujemy funkcje wyswietl i przekazujemy do niej wartosc pola trojkata obliczona w nawiasie
def poleTrojkata(a, h):
    return wyswietl(0.5 * a * h)

a = int(input("Podaj dlugosc podstawy trojkata: "))
h = int(input("Podaj wysokosc trojkata: "))
poleTrojkata(a, h)