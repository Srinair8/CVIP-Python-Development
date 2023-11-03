import tkinter as tk
import math

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif text == "C":
        entry.delete(0, "end")
    elif text == "√":
        try:
            num = float(entry.get())
            result = str(math.sqrt(num))
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif text == "x^2":
        try:
            num = float(entry.get())
            result = str(num ** 2)
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif text == "%":
        try:
            num = float(entry.get())
            result = str(num / 100)
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif text == "x^3":
        try:
            num = float(entry.get())
            result = str(num ** 3)
            entry.delete(0, "end")
            entry.insert("end", result)
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    else:
        entry.insert("end", text)

#Creates a Main Application Window
app = tk.Tk()
app.title("Calculator")
app.geometry("400x550")

#Creates an Entry widget for User Input
entry = tk.Entry(app, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Defines the button labels and background colors
button_info = [
    ('7', "#D3D3D3"), ('8', "#D3D3D3"), ('9', "#D3D3D3"), ('/', "#FFA07A"),
    ('4', "#D3D3D3"), ('5', "#D3D3D3"), ('6', "#D3D3D3"), ('*', "#FFA07A"),
    ('1', "#D3D3D3"), ('2', "#D3D3D3"), ('3', "#D3D3D3"), ('-', "#FFA07A"),
    ('0', "#D3D3D3"), ('C', "#FF6347"), ('=', "#90EE90"), ('+', "#FFA07A"),
    ('√', "#87CEEB"), ('x^2', "#87CEEB"), ('%', "#87CEEB"), ('x^3', "#87CEEB")
]

# Creates and places the buttons in the grid with labels and colors
row, col = 1, 0
for button_label, color in button_info:
    button = tk.Button(app, text=button_label, padx=20, pady=20, font=("Arial", 20), bg=color, borderwidth=2)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights to make the buttons expand with the window
for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(7):
    app.grid_rowconfigure(i, weight=1)

app.mainloop()
