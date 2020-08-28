from globals import Globals, Direction
from avatar import Avatar
from platform import Platform

import tkinter as tk

# set up tkinter window (master) and canvas widget (display)
master = tk.Tk()
display = tk.Canvas(master, width=500, height=500)
Globals.master = master
Globals.display = display

# canvas config
display.pack()
display.focus_set()

# initialize game objects
controlAvatar = Avatar()
Globals.controlAvatar = controlAvatar
newPlatform = Platform(10, 50)

#bind controls
display.bind("<d>", lambda e: controlAvatar.move(Direction.EAST))
display.bind("<s>", lambda e: controlAvatar.move(Direction.SOUTH))
display.bind("<a>", lambda e: controlAvatar.move(Direction.WEST))
display.bind("<w>", lambda e: controlAvatar.move(Direction.NORTH))

# keep the window active (so it doesn't immediately close
master.mainloop()
