from tkinter import *


def main():
    root = Tk()
    root.grid_columnconfigure(1,weight=1) # the text and entry frames column
    root.grid_rowconfigure(0,weight=1) # all frames row

    buttonframe = Frame(root)
    buttonframe.grid(row=0, column=0, sticky="nswe")
    entry_text_frame = Frame(root)
    entry_text_frame.grid(row=0, column=1, sticky="nswe")
    entry_text_frame.grid_columnconfigure(0,weight=1) # the entry and text widgets column
    entry_text_frame.grid_rowconfigure(1,weight=1) # the text widgets row

    button1 = Button(buttonframe, text='one', width=8)
    button1.grid(row=0, column=0, sticky='nswe')
    button2 = Button(buttonframe, text='two', width=8)
    button2.grid(row=1, column=0, sticky='nswe')

    entry1 = Entry(entry_text_frame)
    entry1.grid(row=0, column=0, sticky='nswe')

    text1 = Text(entry_text_frame, highlightbackground='black', highlightthickness=1)
    text1.grid(row=1, column=0, sticky='news')

    root.geometry("300x400")

if __name__ == '__main__':
    main()