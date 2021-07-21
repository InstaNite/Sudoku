import time
import pygame
from sudoku import Sudoku
from grid import Grid

pygame.font.init()

WHITE = (255, 255, 255)


def redraw_window(win, board):
    win.fill(WHITE)
    board.draw(win)


def main():
    WIN = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Sudoku")
    sudoku_grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                   [5, 2, 0, 0, 0, 0, 0, 0, 0],
                   [0, 8, 7, 0, 0, 0, 0, 3, 1],
                   [0, 0, 3, 0, 1, 0, 0, 8, 0],
                   [9, 0, 0, 8, 6, 3, 0, 0, 5],
                   [0, 5, 0, 0, 9, 0, 6, 0, 0],
                   [1, 3, 0, 0, 0, 0, 2, 5, 0],
                   [0, 0, 0, 0, 0, 0, 0, 7, 4],
                   [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    board = Grid(sudoku_grid, 900, 900)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_1:
                    key = 1
                if event.type == pygame.K_2:
                    key = 2
                if event.type == pygame.K_3:
                    key = 3
                if event.type == pygame.K_4:
                    key = 4
                if event.type == pygame.K_5:
                    key = 5
                if event.type == pygame.K_6:
                    key = 6
                if event.type == pygame.K_7:
                    key = 7
                if event.type == pygame.K_8:
                    key = 8
                if event.type == pygame.K_9:
                    key = 9
        redraw_window(WIN, board)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
