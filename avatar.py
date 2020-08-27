from globals import Globals, Direction
from PIL import Image, ImageTk

class Avatar:

    def __init__(self, initX = 250, initY = 100):
        self.texture = ImageTk.PhotoImage(image=Image.open("avatar.png"))
        self.displayObject = Globals.display.create_image(initX, initY, image=self.texture)

