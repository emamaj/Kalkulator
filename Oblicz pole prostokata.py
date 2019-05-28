import sys

print("Program obiczający pole prostokąta.")
a = int(input("Podaj długość boku a:"))
b = int(input("Podaj dlugosc boku b:"))

if(a <= 0 or b <=0):
    print("Dlugosc boku nie moze byc ujemna!")
    sys.exit()
pole = a * b
if (pole != 13):
    print("Dobrze, ze pole jest rozne od 13 bo to pechowa liczba :)")
print (pole)