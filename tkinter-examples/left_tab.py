import tkinter as tk
from tkinter import ttk


class TFEnvSelectionScreen(tk.Frame):
    """
    This is where we give the user the chance to select their Terraform environment.
    Uses a drop down menu for environment selection.
    """
    def __init__(self, parent, controller):
        root = tk.Tk()

        style = ttk.Style(root)
        style.configure('lefttab.TNotebook', tabposition='wn')
        notebook = ttk.Notebook(root, style='lefttab.TNotebook')

        f1 = tk.Frame(notebook, bg="red", width=200, height=200)
        f1.__init__(self, parent)

        env_options = ['Dev', 'Stage', 'Prod']

        select_type_label = tk.Label(f1, text='Select Terraform Environment:')
        select_type_label.grid(row=0,sticky='w')
        env_var = tk.StringVar(self)
        env_menu = ttk.Combobox(f1,textvariable=env_var, values=env_options)
        env_menu.grid(row=0, column=1)

        env_menu.current(1)

        def get_env():
            print("Environment selected is: " + env_var.get())

        continue_button = tk.Button(f1, text='Continue', command=get_env)
        continue_button.grid(row=3, column=0, padx=10,sticky='w')
        continue_button.config(width=10,fg='DodgerBlue3')

        cancel_button = tk.Button(f1, text='Cancel', command=self.quit())
        cancel_button.grid(row=3, column=1, padx=10, sticky='e')
        cancel_button.config(width=10)

        env_var.set('')

        f2 = tk.Frame(notebook, bg="blue", width=200, height=200)

        notebook.add(f1, text="Environment")
        notebook.add(f2, text="Components")
        notebook.pack()
        root.mainloop()