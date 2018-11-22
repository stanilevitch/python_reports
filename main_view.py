import tkinter
from tkinter import messagebox as tkMessageBox

top = tkinter.Tk()


def close_window():
    tkMessageBox.showinfo("tytuł", "tekst wewnątrz drugiego okna")


B1 = tkinter.Button(top, text="B1", command=close_window)
B1.pack()

B2 = tkinter.Button(top, text="B2")
B2.pack()

top.mainloop()
