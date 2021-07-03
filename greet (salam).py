import random
import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("ShoW")
root.config(background = "black")
root.geometry('1900x1280')
root.wm_attributes('-fullscreen','true')

def CreateWidgets():
    root.showLabel = Label(root, text = "As'salam wa'alaekum ☺", bg = "black", font=("Times, 95"))
    root.showLabel.grid(row = 5, column = 10, columnspan=1, padx = 00, pady = 280)

    showWish()

def showWish():
    x = format(random.randint(0, 255), '02x')
    y = format(random.randint(0, 255), '02x')
    z = format(random.randint(0, 255), '02x')

    color = "#"+str(x)+str(y)+str(z)
    root.showLabel.config(fg=color)

    root.showLabel.after(50, showWish)

CreateWidgets()
root.mainloop()



























