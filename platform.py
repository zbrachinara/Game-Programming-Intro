from globals import Globals, Direction

class Platform:

    def __init__(self, posX, posY, length=100):
        self.posX = posX
        self.posY = posY
        self.length = length

        # tk object (line)
        self.displayObject = Globals.display.create_line(posX, posY, posX + length, posY)
