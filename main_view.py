import tkinter

# top = tkinter.Tk()
#
# f = top.Frame(master, height=32, width=32)
# f.pack_propagate(0) # don't shrink
# f.pack()
#
# b = Button(f, text="Sure!")
# b.pack(fill=BOTH, expand=1)


master = tkinter.Tk()

def callback():
    print(f"click!")

b = tkinter.Button(master, text="OK", command=callback)
b.pack()
tkinter.mainloop()