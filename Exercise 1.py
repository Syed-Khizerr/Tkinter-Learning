import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print("This is a button")

def hello():
    print("Hello")

# Creating a window

window = tk.Tk()
window.title("Window and Widgets")
window.geometry('800x500')

# Creating a label
text_Label = ttk.Label(master = window, text = "This is a test")
text_Label.pack()

# Creating a text box
text = ttk.Text(master = window)
text.pack()

# ttk entry

entry = ttk.Entry(master = window )
entry.pack()

# Text label two

text_Label2 = ttk.Label(master= window, text = "My Label")
text_Label2.pack()


# Original button 
button = ttk.Button(master = window, text = "Button", command=button_func)
button.pack()

# A button that prints hello
hello_button = ttk.Button(master = window, text = "Hello", command= hello)
hello_button.pack()

# run
window.mainloop()
