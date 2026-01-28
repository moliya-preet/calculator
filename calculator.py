import tkinter as tk

#  main window

root = tk.Tk()
root.title("Calculator")
root.geometry("300x460")
root.resizable(False, False)

expression = ""


def press(value):
    global expression
    expression += str(value)
    input_text.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def percent():
    global expression
    try:
        expression = str(eval(expression) / 100)
        input_text.set(expression)
    except:
        input_text.set("Error")
        expression = ""

def plus_minus():
    global expression
    if expression.startswith("-"):
        expression = expression[1:]
    else:
        expression = "-" + expression
    input_text.set(expression)

# display

input_text = tk.StringVar()

screen = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    bd=10,
    justify="right"
)
screen.pack(fill="both", ipady=15, padx=10, pady=10)

# buttons

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("C", clear), ("⌫", backspace), ("%", percent), ("/", lambda: press("/")),
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("*", lambda: press("*")),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-")),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+")),
    ("±", plus_minus), ("0", lambda: press("0")), (".", lambda: press(".")), ("=", equal)
]

row = 0
col = 0

for text, command in buttons:
    btn = tk.Button(
        frame,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16),
        command=command
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
