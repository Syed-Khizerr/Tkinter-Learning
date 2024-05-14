import tkinter as tk
import ttkbootstrap as ttk

def check_uncheck():
    print(check_var.get())
    check_var.set(False)


window = tk.Tk()
window.title('Buttons and shit')
window.geometry('600x400')

check_var = tk.BooleanVar()
radio_var = tk.StringVar()

radio_button1 = ttk.Radiobutton(
    window,
    text = 'Radio Button 1',
    value = 'A',
    variable = radio_var,
    command = check_uncheck
)
radio_button1.pack()

radio_button2 = ttk.Radiobutton(
    window,
    text = 'Radio Button 2',
    value = 'B',
    variable=radio_var,
    command= check_uncheck
)
radio_button2.pack()

check_button = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    variable = check_var,
    command= lambda: print(radio_var.get()),
    onvalue=True,
    offvalue=False
)
check_button.pack()

window.mainloop()
