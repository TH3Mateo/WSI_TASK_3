from board import Board
from players import Person, Random, Bot
import view
from threading import Thread
import sys

reward_4 = 400
reward_3 = 100
reward_2 = 10

width = 7
height = 7
eee = [[0,0,1,2,1],
       [0,1,2,2,2],
       [2,2,1,2,2],
       [1,1,2,2,1],
       [1,1,2,1,1]]


def game(p1,p2,board):
    while True:
        p1.move()
        if board.check_win():
            print("p1 wins")
            sys.exit()
        p2.move()
        if board.check_win():
            print("p2 wins")
            sys.exit()
        pass



def main():
    board = Board(width, height)
    P1 = Person(board, 'yellow')
    P2 = Random(board, 'purple')

    Thread(target = game, args = (P1,P2,board)).start()
    Thread(target = view.moving, args = (board,None)).start()




if __name__ == '__main__':
    main()