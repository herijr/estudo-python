from tkinter import *
import random


tk = Tk()

canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")

canvas.pack()

canvas.create_line(10, 10, 50, 50)
#canvas.create_rectangle(100, 100, 250, 250, fill="blue")
#canvas.create_oval(10, 10, 50, 50, fill="green")
#canvas.create_polygon(400, 10, 300, 300, 500, 300,fill="purple")
    
canvas.mainloop()
