import tkinter as tk
from tkinter import ttk
from termcolor import colored


def Helloworld():
    print(colored('Clicked', 'white', 'on_green'))
    return

def Quit():
    print(colored('Quit', 'white', 'on_red'))
    Window.destroy()

Window = tk.Tk()

button1 = ttk.Button(Window, text="Click", command= Helloworld)
button1.pack(side="left", fill="both", expand=True)

quit_button = ttk.Button(Window, text="Quit", command=Quit)
quit_button.pack(side="bottom")

Window.mainloop()