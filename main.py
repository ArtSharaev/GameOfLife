import pygame
from objects.Board import Board
from objects.AliveCell import AliveCell
from objects.BoolArray import BoolArray
from config import *

b = BoolArray()
b.append(1)
b.append(2)
print(b[0])

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('theLife')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(DIMENSIONS)
    screen.fill(BG_COLOR)

    gameboard = Board(DIMENSIONS)
    gameboard.render(screen)
    running = True
    game_started = False
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not game_started and event.type == pygame.MOUSEMOTION:
                click = pygame.mouse.get_pressed()
                if click[0]:
                    mouse_position = mx, my = pygame.mouse.get_pos()
                    print(gameboard.get_cell_coords(mx, my))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_started = True
        gameboard.render(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
