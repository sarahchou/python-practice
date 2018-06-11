import tkinter

master = tkinter.Tk()

listbox = tkinter.Listbox(master)
listbox.pack()

listbox.insert(tkinter.END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(tkinter.END, item)

lb = tkinter.Listbox(master)
b = tkinter.Button(master, text="Delete",
           command=lambda lb=lb: lb.delete(tkinter.ANCHOR))

tkinter.mainloop()