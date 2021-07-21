import pygame
from cube import Cube


class Grid:
    BLACK = (0, 0, 0)

    def __init__(self, grid, width, height):
        self.grid = grid
        self.width = width
        self.height = height
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.cubes = [[Cube(grid[i][j], i, j, width // 9, height // 9)
                      for j in range(self.cols)] for i in range(self.rows)]
        self.model = None
        self.selected = None

    def draw(self, win):
        # Draw gridlines
        gap = self.width // 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            # horizontal line
            pygame.draw.line(win, self.BLACK, (0, i * gap),
                             (self.height, i * gap), thick)
            # vertical line
            pygame.draw.line(win, self.BLACK, (i * gap, 0),
                             (i * gap, self.width), thick)
        # draw cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)


if __name__ == "__main__":
    g = Grid()
