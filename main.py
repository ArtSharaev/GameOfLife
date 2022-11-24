import pygame
from objects.Board import Board
from config import *


def draw_text(screen, text) -> None:
    """Рисуем счётчик поколений"""
    font_size = sum(DIMENSIONS) // 2 // 20
    font = pygame.font.SysFont('arial.ttf', font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (0, 0)
    screen.blit(text_surface, text_rect)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('theLife')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(DIMENSIONS)
    screen.fill(BG_COLOR)

    gameboard = Board(DIMENSIONS)
    gameboard.render(screen)
    game_started = False
    generation_number = 0
    fps = 200

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not game_started and \
                    (event.type == pygame.MOUSEMOTION or
                     event.type == pygame.MOUSEBUTTONDOWN):  # рисование клеток
                click = pygame.mouse.get_pressed()
                if click[0]:
                    mouse_position = mx, my = pygame.mouse.get_pos()
                    x, y = gameboard.get_cell_coords(mx, my)
                    gameboard.set_alive(x, y)
                elif click[2]:
                    mouse_position = mx, my = pygame.mouse.get_pos()
                    x, y = gameboard.get_cell_coords(mx, my)
                    gameboard.set_empty(x, y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # старт или остановка игры
                    if game_started:
                        game_started = False
                        rm = gameboard.rendermode
                        del gameboard
                        gameboard = Board(DIMENSIONS)
                        gameboard.rendermode = rm
                        fps = 200  # поднимаем fps на время рисования
                    else:
                        game_started = True
                        generation_number = 0
                        fps = FPS  # опускаем fps чтобы картинка не мерцала
                elif event.key == pygame.K_h:  # разметка клеток
                    gameboard.change_rendermode()
                elif event.key == pygame.K_r and not game_started:  # рандом
                    gameboard.random_matrix_generation()

        if game_started:
            gameboard.matrix_update()
            generation_number += 1

        if gameboard.is_empty():
            game_started = False
            fps = 200  # поднимаем fps на время рисования
        gameboard.render(screen)
        draw_text(screen, str(generation_number))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
