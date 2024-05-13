import tkinter as tk
from tkinter import ttk
from termcolor import colored

try:
    from ctypes import windll
    windll.shcore.setProcessDpiAwareness(1)
except:
    pass
clicked_count :int = 0
# user_name:str= ""

def Count_clicked():
    global clicked_count
    print(colored(f'Clicked {clicked_count} and Hello {user_name.get()}', 'white', 'on_green'))
    clicked_count += 1
    return clicked_count

def Quit():
    print(colored('Quit', 'white', 'on_red'))
    Window.destroy()

Window = tk.Tk()
# Window.geometry("600x400")
Window.title("Greeter")

Window.columnconfigure(0, weight=1)

user_name = tk.StringVar()

input_frame = ttk.Frame(Window, padding=(20,10,20,0))
input_frame.grid(row = 0, column = 0)

name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row= 0, column=0, padx=(0, 10))

name_entry = ttk.Entry(input_frame, width=15, textvariable= user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

button_frame = ttk.Frame(Window, padding=(20,10))
button_frame.grid(sticky="EW")

button_frame.columnconfigure(0, weight= 1)
button_frame.columnconfigure(1, weight=1)

click_button = ttk.Button(button_frame, text="Click", command= Count_clicked)
click_button.grid(row= 0, column= 0, sticky="EW")

quit_button = ttk.Button(button_frame, text="Quit", command=Quit)
quit_button.grid(row= 0, column= 1, sticky="EW")

Window.mainloop()