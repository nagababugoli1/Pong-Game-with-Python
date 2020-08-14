# importing only  those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
import tkinter
from time import strftime

# creating tkinter window
root = Tk()
root.title('PONG GAME')
root.geometry('250x250')

Label(root, text = "Start").pack(side=TOP, pady=10)
B = tkinter.Button()
Label(B, text = 'Start')


# Allowing root window to change
# it's size according to user's need
root.resizable(True, True)

mainloop()