import pygame


class Cube:
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("Arial", 40)

        # position the cubes in the correct placement
        x = self.col * self.width
        y = self.row * self.width

        # if only a number is hovered but not entered
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, self.GRAY)
            win.blit(text, x + 5, y + 5)
        elif self.value != 0:
            text = fnt.render(str(self.value), 1, self.BLACK)
            win.blit(text, (x + (self.width - text.get_width()) //
                     2, y + (self.height - text.get_height()) // 2))
            if self.selected:
                pygame.draw.rect(
                    win, self.RED, (x, y, self.width, self.height), 3)

    def set(self, value):
        self.value = value

    def set_temp(self, value):
        self.temp = value
