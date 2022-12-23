import pygame
from objects.Board import Board
from config import *


def draw_text(screen, text) -> None:
    font_size = sum(DIMENSIONS) // 2 // 20
    font = pygame.font.SysFont('arial.ttf', font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (0, 0)
    screen.blit(text_surface, text_rect)
    if game_paused:
        is_paused_text_surface = font.render("paused", True, (255, 255, 255))
        is_paused_text_rect = is_paused_text_surface.get_rect()
        is_paused_text_rect.topleft = (0, font_size)
        screen.blit(is_paused_text_surface, is_paused_text_rect)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('theLife')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(DIMENSIONS)
    screen.fill(BG_COLOR)

    gameboard = Board(DIMENSIONS)
    gameboard.render(screen)
    game_paused = False
    generation_number = 0
    fps = 200

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif ((game_paused or gameboard.is_empty()) and
                  (event.type == pygame.MOUSEMOTION or
                   event.type == pygame.MOUSEBUTTONDOWN)):  # рисование клеток
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
                    if game_paused:
                        game_paused = False
                        fps = FPS  # опускаем fps чтобы картинка не мерцала
                    else:
                        game_paused = True
                        fps = 200  # поднимаем fps на время рисования
                elif event.key == pygame.K_c:  # очистка холста
                    game_paused = False
                    rm = gameboard.rendermode
                    del gameboard
                    gameboard = Board(DIMENSIONS)
                    gameboard.rendermode = rm
                elif event.key == pygame.K_h:  # разметка клеток
                    gameboard.change_rendermode()
                elif event.key == pygame.K_r and gameboard.is_empty():  # рандом
                    gameboard.random_matrix_generation()

        if not game_paused:
            gameboard.matrix_update()
            generation_number += 1

        if gameboard.is_empty():
            game_paused = True
            generation_number = 0
            fps = 200  # поднимаем fps на время рисования
        gameboard.render(screen)
        draw_text(screen, str(generation_number))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
