import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    entry_text = entry.get()

    label['text'] = entry_text
    entry['state'] = 'disabled'

def button_func1():
    label['text'] = 'some text'
    entry['state'] = 'enabled'
    entry['text'] = ''

window = tk.Tk()
window.title('Getting and setting Widgets')

label = ttk.Label(master = window, text = 'some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button1  = ttk.Button(master=window, text="Enter", command=button_func)
button1.pack()

button2 = ttk.Button(master=window, text='Reset', command=button_func1)
button2.pack()

window.mainloop()
