from constants import SQUARES, WHITE, LIGHT_GREY, SQUARE_SIZE, MARGIN, BLACK, GREY, DARK_GREY, BLUE, RED, BOARD_LENGTH, THINN_INNER_BORDER, THICK_INNER_BORDER, OUTER_BORDER
import pygame
from tile import Tile

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [[Tile() for _ in range(SQUARES)] for _ in range(SQUARES)]
        return self.board

    def draw(self, win):
        win.fill(WHITE)
        x = MARGIN
        y = MARGIN
        pygame.draw.rect(win, BLACK, (x, y, BOARD_LENGTH, OUTER_BORDER))
        y += OUTER_BORDER
        for i in range(SQUARES):
            self._draw_line(win, x, y)
            y += SQUARE_SIZE
            if i == 8:
                pygame.draw.rect(win, BLACK, (x, y, BOARD_LENGTH, OUTER_BORDER))
            elif (i + 1) % 3 == 0:
                self._draw_inner_line(win, x, y, True)
                y += THICK_INNER_BORDER
            else:
                self._draw_inner_line(win, x, y, False)
                y += THINN_INNER_BORDER


    def _draw_inner_line(self, win, x, y, thick):
        if thick:
            self._draw_inner_border_line(win, x, y, THICK_INNER_BORDER, BLACK)
        else:
            self._draw_inner_border_line(win, x, y, THINN_INNER_BORDER, GREY)

    def _draw_inner_border_line(self, win, x, y, height, color):
        pygame.draw.rect(win, BLACK, (x, y, OUTER_BORDER, height))
        x += OUTER_BORDER
        for _ in range(3):
            pygame.draw.rect(win, color, (x, y, 2 * THINN_INNER_BORDER + 3 * SQUARE_SIZE, height))
            x += 2 * THINN_INNER_BORDER + 3 * SQUARE_SIZE
            pygame.draw.rect(win, BLACK, (x, y, THICK_INNER_BORDER, height))
            x += THICK_INNER_BORDER
        x -= THICK_INNER_BORDER
        pygame.draw.rect(win, BLACK, (x, y, OUTER_BORDER, height))

    def _draw_line(self, win, x, y):
        pygame.draw.rect(win, BLACK, (x, y, OUTER_BORDER, SQUARE_SIZE))
        x += OUTER_BORDER
        for _ in range(3):
            for i in range(3):    
                pygame.draw.rect(win, LIGHT_GREY, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                x += SQUARE_SIZE
                pygame.draw.rect(win, GREY, (x, y, THINN_INNER_BORDER, SQUARE_SIZE))
                x += THINN_INNER_BORDER
            x -= THINN_INNER_BORDER
            pygame.draw.rect(win, BLACK, (x, y, THICK_INNER_BORDER, SQUARE_SIZE))
            x += THICK_INNER_BORDER
        x -= THICK_INNER_BORDER
        pygame.draw.rect(win, BLACK, (x, y, OUTER_BORDER, SQUARE_SIZE))



    def select(self, row, col):
        self.board[row][col].selected = True