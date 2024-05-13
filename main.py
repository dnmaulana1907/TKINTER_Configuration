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

input_frame = ttk.Frame(Window, padding=(20,10,20,0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(padx=(0, 10), side="left")

name_entry = ttk.Entry(input_frame, width=15, textvariable= user_name)
name_entry.pack(side="left")
name_entry.focus()

button_frame = ttk.Frame(Window, padding=(20,10))
button_frame.pack(fill="both")

click_button = ttk.Button(button_frame, text="Click", command= Count_clicked)
click_button.pack(side="left", fill="x", expand= True)

quit_button = ttk.Button(button_frame, text="Quit", command=Quit)
quit_button.pack(side="right", fill="y", expand= True)

Window.mainloop()