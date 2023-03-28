from customtkinter import *

app = CTk()

def button_on_click():
    print("vamos a aprender Python")

button = CTkButton(master=app, text="Click Me ", command=button_on_click)
button.grid()

app.mainloop()
