import sys
from tkinter import *
import time

def tick():
    time_string = time.strftime("%H:%M:%S %p %A")
    clock.config(text = time_string)
    clock.after(200, tick)

root = Tk()
root.title("Digital clock")
clock = Label(root, font = ("arial", 50, "bold"), bg = "blue", fg = "white")
clock.grid(row = 0, column = 1)
tick()
root.mainloop()

