import tkinter as tk
import os
import sys

sys.path.insert(0, os.getcwd())
from exr_shopping_cart.authentication import render_register, render_login
from exr_shopping_cart.products import render_products

def render_main_screen(screen: tk.Tk):
    """
    """
    tk.Button(screen, text='Login', background='green', foreground='white',
              command=lambda: render_login(screen, on_success=lambda: print('Login successful'))).grid(row=0, column=0)

    tk.Button(screen, text='Register', background='yellow', foreground='black',
              command=lambda: render_register(screen, on_success=render_main_screen)).grid(row=0, column=1)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('My App')
    window.geometry('600x600')

    render_main_screen(window)

    window.mainloop()
