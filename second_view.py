import random

liczba = random.randint(1, 10)
print("Wylosowana liczba to: ", liczba)

odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")
print("Podałeś liczbę: ", odp)

if liczba == int(odp):
    print("Wygrałeś")
else:
    print("Pudło, jescze raz!!!")