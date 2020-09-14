import pygame
from constants import FPS, WIDTH, HEIGHT
import game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
game = game.Game(WIN)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise SystemExit
            print(event.unicode)
