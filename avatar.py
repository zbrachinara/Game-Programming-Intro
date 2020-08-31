from globals import Globals, Direction
from PIL import Image, ImageTk


class Avatar:

    def __init__(self, initX=250, initY=100):
        self.texture = ImageTk.PhotoImage(image=Image.open("avatar.png"))
        self.displayObject = Globals.display.create_image(initX, initY, image=self.texture)
        self.posX = initX
        self.posY = initY
        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = Globals.gravity

    def move(self, direction):
        if direction == Direction.EAST:
            self.velX += 1
        elif direction == Direction.SOUTH:
            self.velY -= 1
        elif direction == Direction.WEST:
            self.velX -= 1
        elif direction == Direction.NORTH:
            self.velY += 1

        Globals.display.coords(self.displayObject, self.posX, self.posY)
        print("Moved " + str(direction.name) + " to position " + str(self.posX) + ", " + str(self.posY))

    def updatePosition(self):
        self.posX += self.velX * Globals.step
        self.posY -= self.velY * Globals.step

        self.velX += self.accX * Globals.step
        self.velY += self.accY * Globals.step

        self.velX -= Globals.surfaceFriction * (1 if self.velX > 0 else -1) * Globals.step
        self.velY -= Globals.surfaceFriction * (1 if self.velY > 0 else -1) * Globals.step

        Globals.display.coords(self.displayObject, self.posX, self.posY)
        print(self.velY)
        print(self.velX)