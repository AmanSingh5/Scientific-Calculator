import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Scientific Calculator")

root.geometry("400x600")
root.resizable(0, 0)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

def show_about():
    messagebox.showinfo("About", "Scientific Calculator v1.0\nCreated using Python and Tkinter.")

def create_menu():
    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    help_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)

entry = tk.Entry(root, width=30, font=("Arial", 18), borderwidth=2, relief="solid", bg="#F0F8FF")
entry.grid(row=0, column=0, columnspan=4, pady=20)

buttons = [
    ('7', 1, 0, "#FFEBEE"), ('8', 1, 1, "#FFEBEE"), ('9', 1, 2, "#FFEBEE"), ('/', 1, 3, "#FFCDD2"),
    ('4', 2, 0, "#E3F2FD"), ('5', 2, 1, "#E3F2FD"), ('6', 2, 2, "#E3F2FD"), ('*', 2, 3, "#BBDEFB"),
    ('aman', 3, 0, "#E8F5E9"), ('2', 3, 1, "#E8F5E9"), ('3', 3, 2, "#E8F5E9"), ('-', 3, 3, "#C8E6C9"),
    ('0', 4, 0, "#FFF3E0"), ('.', 4, 1, "#FFF3E0"), ('+', 4, 2, "#FFE0B2"), ('=', 4, 3, "#FFD180"),
    ('sin', 5, 0, "#F3E5F5"), ('cos', 5, 1, "#F3E5F5"), ('tan', 5, 2, "#CE93D8"), ('sqrt', 5, 3, "#B39DDB"),
    ('log', 6, 0, "#F8BBD0"), ('exp', 6, 1, "#F8BBD0"), ('pi', 6, 2, "#F48FB1"), ('(', 6, 3, "#F06292"),
    (')', 7, 0, "#FFCCBC"), ('^', 7, 1, "#FFAB91"), ('aman/x', 7, 2, "#FF8A65"), ('clear', 7, 3, "#FF7043"),
]

for (text, row, col, color) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=evaluate).grid(row=row, column=col)
    elif text == "clear":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=clear).grid(row=row, column=col)
    elif text == "sin":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.sin(")).grid(row=row, column=col)
    elif text == "cos":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.cos(")).grid(row=row, column=col)
    elif text == "tan":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.tan(")).grid(row=row, column=col)
    elif text == "sqrt":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.sqrt(")).grid(row=row, column=col)
    elif text == "log":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.log(")).grid(row=row, column=col)
    elif text == "exp":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.exp(")).grid(row=row, column=col)
    elif text == "pi":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("math.pi")).grid(row=row, column=col)
    elif text == "aman/x":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda: button_click("aman/")).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg=color, command=lambda t=text: button_click(t)).grid(row=row, column=col)

create_menu()
root.mainloop()