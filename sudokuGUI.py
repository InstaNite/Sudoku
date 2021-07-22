import time
import pygame
from sudoku import Sudoku
from grid import Grid

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

MAX_STRIKES = 5

TIME_FONT = pygame.font.SysFont("Arial", 40)


def redraw_window(win, board, play_time, strikes):
    win.fill(WHITE)

    # display time played
    time_str = time.strftime("%M:%S", time.gmtime(play_time))
    time_text = TIME_FONT.render(time_str, 1, BLACK)
    win.blit(time_text, (900 - time_text.get_width() -
             5, 950 - time_text.get_height()))

    strikes_text = TIME_FONT.render("X " * strikes, 1, RED)
    win.blit(strikes_text, (0, 950 - strikes_text.get_height()))
    board.draw()


def main():
    WIN = pygame.display.set_mode((900, 950))
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

    board = Grid(WIN, sudoku_grid, 900, 900)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  # when a button is pressed
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if not board.place(board.cubes[i][j].temp):
                            strikes += 1

            if event.type == pygame.MOUSEBUTTONDOWN:    # when mouse clicks
                pos = pygame.mouse.get_pos()
                rowcol = board.get_rowcol(pos)

                if rowcol:
                    board.select(rowcol[0], rowcol[1])
                    key = None
        # if a cube has been selected and key has been entered
        if board.selected and key:
            board.sketch(key)

        redraw_window(WIN, board, play_time, strikes)
        if strikes == MAX_STRIKES:
            run = False
        pygame.display.update()

        if board.isFinished():
            print("Game over!")
    pygame.quit()


if __name__ == "__main__":
    main()
