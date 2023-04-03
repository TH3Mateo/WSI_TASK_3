import random
import utils as u
colors = {
    'red': 1,
    'blue': 2,
    'green': 3,
    'yellow': 4,
    'purple': 5,
    'orange': 6,
    'black': 7,
    'pink': 8,
}


class uniPlayer:
    def __init__(self, board, color):
        self.color = color
        self.board = board
        self.symbol = colors.get(color)


class Bot(uniPlayer):

    def minimax(self, depth,situation):
        if depth == 0 or self.board.check_win() == True:
            return u.evaluate(self.board.board, self.symbol)
        for i in []

    def move(self):

        pass


class Person(uniPlayer):
    def move(self):
        Error = True
        while Error:
            c = int(input("Choose the column to put your token: "))
            if 0 in [row[c - 1] for row in self.board.board]:
                self.board.add(c - 1, self)
                print(self.board.board)
                Error = False
            else:
                print(f"No more slots in {c} column, choose another one!")


class Random(uniPlayer):
    def move(self):
        self.board.add(random.randint(0, self.board.width - 1), self)
