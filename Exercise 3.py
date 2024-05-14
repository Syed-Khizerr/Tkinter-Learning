import tkinter as tk
import ttkbootstrap as ttk


window = tk.Tk()
window.title('Getting and setting Widgets')

string_var = tk.StringVar(value='text')


label = ttk.Label(master = window, text = 'some text', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

entry2  = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()

window.mainloop()
