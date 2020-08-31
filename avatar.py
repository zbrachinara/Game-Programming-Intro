from globals import Globals, Direction
from PIL import Image, ImageTk


class Avatar:

    def __init__(self, initX=250, initY=100):
        # add tk object
        self.texture = ImageTk.PhotoImage(image=Image.open("avatar.png"))
        self.displayObject = Globals.display.create_image(initX, initY, image=self.texture)

        self.posX = initX
        self.posY = initY
        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = Globals.gravity

    # bound to <d>, <s>, <a>, <w>
    def move(self, direction):
        if direction == Direction.EAST:
            self.posX += 1
        elif direction == Direction.SOUTH:
            self.posY += 1
        elif direction == Direction.WEST:
            self.posX -= 1
        elif direction == Direction.NORTH:
            self.posY -= 1

        # reposition object on [display] after coords are updated
        Globals.display.coords(self.displayObject, self.posX, self.posY)
        print("Moved " + str(direction.name) + " to position " + str(self.posX) + ", " + str(self.posY))

    def updatePosition(self):
        self.posX += self.velX * Globals.step / 1000
        self.posY -= self.velY * Globals.step / 1000

        self.velX += self.accX * Globals.step / 1000
        self.velY += self.accY * Globals.step / 1000

        Globals.display.coords(self.displayObject, self.posX, self.posY)
        print(self.velY)