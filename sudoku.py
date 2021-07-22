class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def printGrid(self):
        for i in self.grid:
            print(i)

    def solve(self, rowcol):
        row, col = rowcol
        # solve is done
        if row == 9 and col == 0:
            return True

        # check if there is already a number in the cell
        if self.grid[row][col] > 0:
            # go to next cell
            return self.solve(self.nextCell(row, col))

        for i in range(1, 10):
            if self.isValid(row, col, i):
                self.grid[row][col] = i

                # check for next possibility with next column
                if self.solve(self.nextCell(row, col)):
                    return True
            # removing the assigned number since our assumption was wrong
            self.grid[row][col] = 0
        return False

    def nextCell(self, row, col):
        if col == 8:
            return [row + 1, 0]
        else:
            return [row, col + 1]

    def prevCell(self, row, col):
        if col == 0:
            return [row - 1, 8]
        else:
            return [row, col - 1]

    def isValid(self, row, col, val):
        # check if value is valid in row
        for i in range(9):
            if self.grid[row][i] == val:
                return False

        # check if value is valid in column
        for i in range(9):
            if self.grid[i][col] == val:
                return False

        # check if value is valid in box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == val:
                    return False

        return True

    def getGrid(self):
        return self.grid


if __name__ == "__main__":
    s = Sudoku()
    s.solve()
    s.printGrid()
