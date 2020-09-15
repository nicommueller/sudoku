import pygame

class Tile:
    def __init__(self):
        self.selected = False

    def draw(self, win, x, y):
        pygame.draw.rect(win, LIGHT_GREY, (x + i * SQUARE_SIZE + BORDER // 2, y + j * SQUARE_SIZE + BORDER // 2, SQUARE_SIZE - BORDER + 1, SQUARE_SIZE - BORDER + 1))