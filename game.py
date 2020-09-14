import pygame
from constants import SQUARES

class Game:
    def __init__(self, win):
        self.win = win
        self.board = [[None for _ in range(SQUARES)] for _ in range(SQUARES)]
        print(self.board)