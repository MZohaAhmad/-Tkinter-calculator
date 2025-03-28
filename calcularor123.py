
import tkinter as tk

# Button click functions
def press(num):
    """Handles button press to add value to the entry."""
    expression = equation.get()
    equation.set(expression + str(num))

def equalpress():
    """Evaluates the entered expression."""
    try:
        result = eval(equation.get())
        equation.set(str(result))
    except:
        equation.set("Error")

def clear():
    """Clears the entry field."""
    equation.set("")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Equation variable to display values
equation = tk.StringVar()

# Entry widget to display input/output
entry = tk.Entry(root, textvariable=equation, font=("Arial", 18), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating buttons manually without using a for loop
btn_7 = tk.Button(root, text="7", height=2, width=8, command=lambda: press(7))
btn_7.grid(row=1, column=0)

btn_8 = tk.Button(root, text="8", height=2, width=8, command=lambda: press(8))
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(root, text="9", height=2, width=8, command=lambda: press(9))
btn_9.grid(row=1, column=2)

btn_div = tk.Button(root, text="/", height=2, width=8, command=lambda: press("/"))
btn_div.grid(row=1, column=3)

btn_4 = tk.Button(root, text="4", height=2, width=8, command=lambda: press(4))
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(root, text="5", height=2, width=8, command=lambda: press(5))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text="6", height=2, width=8, command=lambda: press(6))
btn_6.grid(row=2, column=2)

btn_mul = tk.Button(root, text="*", height=2, width=8, command=lambda: press("*"))
btn_mul.grid(row=2, column=3)

btn_1 = tk.Button(root, text="1", height=2, width=8, command=lambda: press(1))
btn_1.grid(row=3, column=0)

btn_2 = tk.Button(root, text="2", height=2, width=8, command=lambda: press(2))
btn_2.grid(row=3, column=1)

btn_3 = tk.Button(root, text="3", height=2, width=8, command=lambda: press(3))
btn_3.grid(row=3, column=2)

btn_sub = tk.Button(root, text="-", height=2, width=8, command=lambda: press("-"))
btn_sub.grid(row=3, column=3)

btn_0 = tk.Button(root, text="0", height=2, width=8, command=lambda: press(0))
btn_0.grid(row=4, column=0)

btn_dot = tk.Button(root, text=".", height=2, width=8, command=lambda: press("."))
btn_dot.grid(row=4, column=1)

btn_clear = tk.Button(root, text="C", height=2, width=8, command=clear)
btn_clear.grid(row=4, column=2)

btn_add = tk.Button(root, text="+", height=2, width=8, command=lambda: press("+"))
btn_add.grid(row=4, column=3)

btn_equal = tk.Button(root, text="=", height=2, width=18, command=equalpress, bg="#32CD32", fg="white")
btn_equal.grid(row=5, column=0, columnspan=2)

btn_exit = tk.Button(root, text="Exit", height=2, width=18, command=root.destroy, bg="red", fg="white")
btn_exit.grid(row=5, column=2, columnspan=2)

# Start the GUI event loop
root.mainloop()
