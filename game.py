import pygame
from constants import SQUARES
import board


class Game:
    def __init__(self, win):
        self.win = win
        self.board = board.Board()
        self.selected = None
    
    def draw(self):
        self.board.draw(self.win)
        pygame.display.update()

    def update(self):
        self.draw()

    def select(self, row, col):
        if min(row, col) <= -1 or max(row, col) >= 9:
            return
        self.board.select(row, col)