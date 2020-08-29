from globals import Globals, Direction
from PIL import Image, ImageTk


class Avatar:

    def __init__(self, initX=250, initY=100, gravity=-9.8):
        self.texture = ImageTk.PhotoImage(image=Image.open("avatar.png"))
        self.displayObject = Globals.display.create_image(initX, initY, image=self.texture)
        self.posX = initX
        self.posY = initY
        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = gravity

    def move(self, direction):
        if direction == Direction.EAST:
            self.posX += 1
        elif direction == Direction.SOUTH:
            self.posY += 1
        elif direction == Direction.WEST:
            self.posX -= 1
        elif direction == Direction.NORTH:
            self.posY -= 1

        Globals.display.coords(self.displayObject, self.posX, self.posY)
        print("Moved " + str(direction.name) + " to position " + str(self.posX) + ", " + str(self.posY))

    def updatePosition(self):
        self.posX += self.velX
        self.posY -= self.velY

        self.velX += self.accX
        self.velY += self.accY

        Globals.display.coords(self.displayObject, self.posX, self.posY)