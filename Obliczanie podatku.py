podatekA = 10/100
podatekB = 20/100
podatekC = 30/100

def obliczPodatek(zarobki):
    if (zarobki < 2000):
        podatke = podatekA;
    elif (zarobki >= 2000 and zarobki < 5000):
        podatek = podatekB;
    else:
        podatek = podatekC;
        return podatek * zarobki

zarobki = int(input("podaj wysokosc swoich zarobkow: "))
wysokoscPodatkow = obliczPodatek(zarobki)
print("Wysokosc Twojego podatku to:", wysokoscPodatkow)
