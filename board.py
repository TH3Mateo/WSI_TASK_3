import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import numpy as np

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((width, height))


    def add(self, column, player):
        l = len(self.board[0])
        for i in range(l):
            if self.board[-i-1][column] == 0:
                self.board[-i-1][column] = player.symbol
                return True

    def check_win(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    if self._check_win_from_point(i, j):
                        return True
        return False

    def _check_win_from_point(self, x, y):
        player = self.board[x][y]
        if self._check_win_from_point_in_direction(x, y, 1, 0, player):
            return True
        if self._check_win_from_point_in_direction(x, y, 0, 1, player):
            return True
        if self._check_win_from_point_in_direction(x, y, 1, 1, player):
            return True
        if self._check_win_from_point_in_direction(x, y, 1, -1, player):
            return True
        return False

    def _check_win_from_point_in_direction(self, x, y, dx, dy, player):
        count = 0
        for i in range(4):
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            if self.board[x][y] != player:
                return False
            count += 1
            x += dx
            y += dy
        return count == 4

