import pygame
from objects.Board import Board
from config import *


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
    fps = 200
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not game_started and\
                    (event.type == pygame.MOUSEMOTION or
                     event.type == pygame.MOUSEBUTTONDOWN):
                click = pygame.mouse.get_pressed()
                if click[0]:
                    mouse_position = mx, my = pygame.mouse.get_pos()
                    x, y = gameboard.get_cell_coords(mx, my)
                    gameboard.set_alive(x, y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_started:
                        game_started = False
                        fps = 200
                        rm = gameboard.rendermode
                        del gameboard
                        gameboard = Board(DIMENSIONS)
                    else:
                        game_started = True
                        fps = FPS
                elif event.key == pygame.K_h:
                    gameboard.change_rendermode()
                elif event.key == pygame.K_r and not game_started:
                    gameboard.random_matrix_generation()

        if game_started:
            gameboard.matrix_update()
        if gameboard.is_empty():
            game_started = False
            fps = 200
        gameboard.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
