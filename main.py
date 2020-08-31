from globals import Globals, Direction
from avatar import Avatar
from platform import Platform

import tkinter as tk

master = tk.Tk()
display = tk.Canvas(master, width=500, height=500)
Globals.master = master
Globals.display = display

display.pack()
display.focus_set()

controlAvatar = Avatar()
Globals.controlAvatar = controlAvatar
newPlatform = Platform(10, 50)

display.bind("<d>", lambda e: controlAvatar.move(Direction.EAST))
display.bind("<s>", lambda e: controlAvatar.move(Direction.SOUTH))
display.bind("<a>", lambda e: controlAvatar.move(Direction.WEST))
display.bind("<w>", lambda e: controlAvatar.move(Direction.NORTH))


# update function which is called for every [Globals.step] ms
def update():
    controlAvatar.updatePosition()
    display.after(Globals.step, update)


display.after(2000, update) # begin updating

master.mainloop()
