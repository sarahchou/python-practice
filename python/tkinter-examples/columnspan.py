import tkinter

master = tkinter.Tk()
tkinter.Label(master, text="Input:").grid(row=0)

e1 = tkinter.Entry(master, width = 100)
e1.grid(row=0, column=1, columnspan=30)

tkinter.Button(master, text='Q').grid(row=3, column=2)

tkinter.Button(master, text='C').grid(row=3, column=1)

tkinter.Button(master, text='Confirm').grid(row=3, column=0)
tkinter.mainloop()