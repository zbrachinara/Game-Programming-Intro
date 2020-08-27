from globals import Globals
from avatar import Avatar
from platform import Platform

from tkinter import *

master = Tk()
display = Canvas(master, width=500, height=500)
display.pack()

Globals.master = master
Globals.display = display

Globals.controlAvatar = Avatar()

master.mainloop()