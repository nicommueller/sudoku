import pygame
from constants import FPS, WIDTH, HEIGHT, SQUARE_SIZE, MARGIN
from game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y - MARGIN) // SQUARE_SIZE
    col = (x - MARGIN) // SQUARE_SIZE
    return row, col


def main():
    clock = pygame.time.Clock()
    game = Game(WIN)
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                #print(event.unicode)
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)


        game.update()
        game.draw()
        

main()