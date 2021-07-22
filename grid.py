import pygame
from cube import Cube
from sudoku import Sudoku


class Grid:
    BLACK = (0, 0, 0)

    def __init__(self, win, grid, width, height):
        self.win = win
        self.grid = grid
        self.width = width
        self.height = height
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.cubes = [[Cube(grid[i][j], i, j, width // 9, height // 9)
                      for j in range(self.cols)] for i in range(self.rows)]
        self.model = None
        self.selected = None
        self.s = Sudoku(grid)

    def draw(self):
        # Draw gridlines
        gap = self.width // 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            # horizontal line
            pygame.draw.line(self.win, self.BLACK, (0, i * gap),
                             (self.height, i * gap), thick)
            # vertical line
            pygame.draw.line(self.win, self.BLACK, (i * gap, 0),
                             (i * gap, self.width), thick)
        # draw cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(
            self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            print(self.model)
            if self.s.isValid(row, col, val) and self.s.solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def select(self, row, col):
        # reset selects for all cubes
        for i in range(self.rows):
            for j in range(self.rows):
                self.cubes[i][i].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def get_rowcol(self, pos):
        row = pos[0] // (self.height // 9)
        col = pos[1] // (self.width // 9)

        if row > 8 or col > 8:
            return None

        return (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col] == 0:
            self.cubes[row][col].set_temp(0)
