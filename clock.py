import random
import tkinter as tk
from tkinter import *
import threading
import datetime
now = datetime.datetime.now()
#print ("Current date and time : ")
#print ()

def Time():
    
    root.TimeLabel = Label(root, text = now.strftime("%H:%M:%S"), bg = "white",fg="blue", font=("Times, 200"))
    root.TimeLabel.grid(row = 2, column = 3, columnspan=5, padx = 250, pady = 250)
    root.after(10, Time)
    
def showTime():
    x = format(random.randint(0, 255), '02x')
    y = format(random.randint(0, 255), '02x')
    z = format(random.randint(0, 255), '02x')
    x = 0
    y = 0
    z = 0

    color = "#"+str(x)+str(y)+str(z)
    root.TimeLabel.config(fg=color) 
    root.TimeLabel.after(1, showTime)


root = tk.Tk()
root.title("ShoW")
root.wm_attributes('-fullscreen','true')
root.config(background = "black")
root.after(15000, lambda: root.destroy())
root.geometry('1900x1280')
Time()
mainloop()

