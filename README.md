# python_reports
#### raporty z Jiry - Plan

> zalogować się do Jira

> z Jira pobrać raport w formacie CSV:
- API
- odpowiednie wartości z wybranych kolumn

> zapisać `er.csv` w folderze `C:\rap`

> wstawić ręcznie dzisiejszą/wybraną datę `e.g 2018-11-22`
- domyślnie pobrać dzisiejszą datę

> wstawić numer sprintu
- domyślnie pobrać numer aktualnego sprintu

> uruchomić `moduł.jar` (generator raportu html)

> w folderze C:\rap automatycznie zapisze się wygenerowany report.html

> wysłać maila z załącznikiem `report.html`
- wysłąć maila z załącznikiem i obrazkiem (png?) w treści maila lub w załączniku

> po wysłąniu maila zrobić backup danych zmieniając nazwę (dodać datę i czas generowania raportu w nazwie)


http://www.effbot.org/tkinterbook/tkinter-index.htm

http://www.wykop.pl/ramka/4125379/python-gui-examples-tkinter-tutorial-like-geeks/



```python
master = tkinter.Tk()

def callback():
    print(f"click!")

b = tkinter.Button(master, text="OK", command=callback)
b.pack()
tkinter.mainloop()
```
![Alt text](.\snip_images\click.PNG "title")

`[]` operator tworzenia listy:
```python
lista = [1,2,3,4,5]
```
lub operator dostępu do elementów listy, krotki lub słownika:
```python
lista = [1, 2, 3, 4, 5]
a = lista[2]
```
`{}` operator tworzenia słownika:
```python
slownik = {"Ala":"kot","Jarek":"pies"}
slownik["Ala"]
```
