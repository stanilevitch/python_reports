import tkinter
master = tkinter.Tk()

def callback():
    print("click!")

b = tkinter.Button(master, text="OK", command=callback)
b.pack()
tkinter.mainloop()
---------------------------------------------------------
name = input("Podaj swoje imie: ")

print("Witaj {name} w świecie pythona!".format(name=name))
print(f"Witaj {name} w świecie pythona!")
print("Witaj {0} w świecie Pythona!".format(name))
print("Witaj " + name + " w świecie Pythona!")
print("Witaj", name, "w świecie Pythona!")

---------------------------------------------------------
name = input("Podaj swoje imie: ")
age = int(input("Podaj swój wiek: "))

print("Witaj {name} w świecie pythona! Masz {age} lat.".format(name=name, age=age))
print("Witaj {name} w świecie pythona! Masz {age:8} lat.".format(name=name, age=age))

>>> Podaj swoje imie: aaa
>>> Podaj swój wiek: 123
>>> Witaj aaa w świecie pythona! Masz 123 lat.
>>> Witaj aaa w świecie pythona! Masz      123 lat.
---------------------------------------------------------
a = input("A: ")
b = input("B: ")

if a == b:
    print("a = b")
elif a > b:
    print("a > b")
else:
    print("a < b")

---------------------------------------------------------
text = "jakiś tekst"

dl = len(text)

for letter in text:
    print(letter, end='/')

print("Rozmiar tekstu: {dl} ".format(dl=dl))

---------------------------------------------------------
lista = [10, 'coś tam', 56.66]
for i in lista:
    print(i)
---------------------------------------------------------
WHILE:
w = 0
while w == 0:
    w = int(input("Podaj liczbe wieksza od zera: "))
    if w == 0:
        print("Hej! Miała być większa od zera!")
    else:
        print("Twój szczęśliwy numerek to {number}.\nKoniec programu!".format(number=w))
---------------------------------------------------------
DŁUGOŚĆ TEKSTU:
text = "0123456789"
print(len(text))

print("Jakiś tekst".__len__())
print("Jakiś tekst".__len__())
---------------------------------------------------------
SPLIT:
text = "Jaką liczbę od 1 do 10 mam na myśli? ".split()
print(text)
text = "Jaką\nliczbę\nod 1 do 10\nmam na myśli? ".split("\n")
print(text)
---------------------------------------------------------
WYCINANIE TEKSTU
text = "Jaką liczbę od 1 do 10 mam na myśli? "[6:11]
print(text)
---------------------------------------------------------
OBRACANIE TEKSTU:
text = "Jaką liczbę od 1 do 10 mam na myśli? "[::-1]
print(text)
-------------------------
OBRACANIE TEKSTU - PALINDROM:
text = input("Czy dany tekst jest palindromem: ")
if text == text[::-1]:
    print(f"Podany wyraz '{text}' jest palindromem")
else:
    print("To nie jest palindrom, bo od końca brzmi: '{text}'".format(text=text[::-1]))
--------------------------------------------------------
WYSZUKAJ TEKST:
text = "Jakiś tekst przykładowy"
print(text.find("tekst"))
print(text.index("Jakiś"))
---------------------------------------------------------
DUŻE DRUKOWANE LITERY
print(text.upper())
---------------------------------------------------------
MAŁE
print(tekst.lower())
---------------------------------------------------------
Zamiana pierwszych liter wyrazów na duże
print(tekst.title())
---------------------------------------------------------
Zliczanie liczby wystąpień tekstu w tekście
print(tekst.count("tekst"))
---------------------------------------------------------
Wypośrodkowanie tekstu
print(tekst.center(70)) # liczba 70 oznacza liczbę znaków dla pojedynczej linii tekstu
---------------------------------------------------------
Zamiana tekstu w tekście
tekst = "Jakiś tam przykładowy text"
print(tekst.replace("text", "tekst")
print(text.replace("a", "@"))
---------------------------------------------------------
Formatowanie w stylu wersji Pythona < 3.0:

name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")
age = int(input("Podaj wiek: "))
weight = float(input("Podaj wagę [kg]: "))

print("%s\nImię: %s\nNazwisko: %s\n%s\nWiek: %3d\nWaga [kg]: %5.1f"%("="*70,name, surname, "=" * 70, age, weight))
W powyższym kodzie użyto następujących znaczników:

\n - znacznik łamania linii tekstu;
%s - znacznik wstawiania tekstu;
%3d - znacznik wstawiania do tekstu wartości liczbowej całkowitej (to mówi oznaczenie d), natomiast cyfra przed tymże oznaczeniem mówi ile znaków zostanie zarezerwowane na wyświetlenie liczby (w tym przypadku 3);
%5.1f - znacznik wstawiania do tekstu wartości liczbowej zmiennoprzecinkowej (to mówi oznaczenie f), natomiast cyfra przed znakiem . mówi ile miejsca ma być zarezerwowane na liczbą, natomiast cyfra po . mówi ile miejsc ma być zarezerwowanych na liczby po przecinku.

---------------------------------------------------------
Formatowanie w stylu wersji Pythona >= 3.0
Listing 19ZwińKopiuj
name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")
age = int(input("Podaj wiek: "))
weight = float(input("Podaj wagę [kg]: "))

print("{line}\nImię: {name}\nNazwisko: {surname}\n{line}\nWiek: {age:3d}\nWaga [kg]: {weight:5.1f}".format(line="="*70,name=name, surname=surname, age=age, weight=weight))
Wstawianie znaków specjalnych
W tekście można wstawiać następujące znaczniki znaków specjalnych:

\n - znacznik nowej linii;
\t - znacznik tabulatora;
\" - znacznik wstawiania cudzysłowu;
\' - znacznik wstawiania apostrofu;
---------------------------------------------------------


---------------------------------------------------------
