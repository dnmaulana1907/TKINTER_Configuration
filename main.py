import tkinter as tk
from tkinter import ttk
from termcolor import colored

clicked_count :int = 0
# user_name:str= ""

def Count_clicked():
    global clicked_count
    print(colored(f'Clicked {clicked_count} and {user_name.get()}', 'white', 'on_green'))
    clicked_count += 1
    return clicked_count

def Quit():
    print(colored('Quit', 'white', 'on_red'))
    Window.destroy()

Window = tk.Tk()
# Window.geometry("600x400")

user_name = tk.StringVar()

name_label = ttk.Label(Window, text="Name: ")
name_label.pack(padx=(0, 10), side="left")

name_entry = ttk.Entry(Window, width=15, textvariable= user_name)
name_entry.pack(side="left")
name_entry.focus()

click_button = ttk.Button(Window, text="Click", command= Count_clicked)
click_button.pack(side="left")

quit_button = ttk.Button(Window, text="Quit", command=Quit)
quit_button.pack(side="right")

Window.mainloop()