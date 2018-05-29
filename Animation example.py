from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Boucing Ball")
canvas.pack()

class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(10, 10, 60, 60, fill="orange")
        self.xspeed = 4
        self.yspeed = 5

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed
newball = Ball()

while True:
    newball.move()
    tk.update()
    time.sleep(0.01)
    
tk.mainloop()
