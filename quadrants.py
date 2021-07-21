import sys


class Quad(QWidget):
    def __init__(self, values: list, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.layout = QGridLayout()
        self.values = values
        self.create()

    def create(self):
        row = 0
        col = 0
        self.squares = []
        for val in self.values:
            if val == 0:
                square = QLineEdit()
            else:
                square = QLabel(str(val))
            square.setFixedSize(90, 90)
            self.squares.append(square)
            self.layout.addWidget(square, row, col)
            col += 1
            if col == 3:
                row += 1
                col = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    val = [3, 0, 6,
           5, 2, 0,
           0, 8, 7]
    s = Quad(val)
    s.show()
    sys.exit(app.exec_())
