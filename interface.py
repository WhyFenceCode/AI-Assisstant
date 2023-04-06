import tkinter as tk
from tkinter import *

def setWindow():

    #creating window
    window=tk.Tk()

    #getting screen width and height of display
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))

    window.title("Assistant")
    label = tk.Label(window, text="Hello Tkinter!", bg='#3C3C3C')
    label.pack()

    btn = Button(window, text='OK', bg='#FFF024')
    btn.bind('<Button-1>', homescreen)

    window['background']='#3C3C3C'
    window.mainloop()

def homescreen():

    print("good")
