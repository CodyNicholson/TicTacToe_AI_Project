class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.minimaxValue = 0

    def getX(self) -> int:
        return self.x

    def setX(self, x: int) -> None:
        self.x = x

    def getY(self) -> int:
        return self.y

    def setY(self, y: int) -> None:
        self.y = y

    def getMinimaxValue(self) -> int:
        return self.minimaxValue

    def setMinimaxValue(self, score: int):
        self.minimaxValue = score

    def __repr__(self):
        return "(" + self.x + ", " + self.y + ")"
