# Declare two classes:
#
# Cell - to represent a cell of the game board;
# GamePole - to manage the game board of size N x N cells.
#
# Using the Cell class, individual cells can be created with the command:
#
# c1 = Cell(around_mines, mine)
# Here around_mines is the number of mines around the current cell; mine is a boolean value (True/False),
# indicating the presence of a mine in the current cell. In each object of the Cell class,
# the following local properties must be created:
#
# around_mines - the number of mines around the cell (initially 0);
# mine - the presence of a mine in the current cell (True/False);
# fl_open - open/closed cell - boolean value (True/False). Initially, all cells are closed (False).
#
# Using the GamePole class, it should be possible to create a square game board with N x N cells:
#
# pole_game = GamePole(N, M)
# Here N is the size of the board; M is the total number of mines on the board.
# Each cell is represented by an object of the Cell class,
# and all objects are stored in a two-dimensional
# list of N x N elements - the local property pole of the GamePole class object.
#
# The GamePole class should also implement the following methods:
#
# init() - initialize the board with a new arrangement of M mines
# (randomly across the game board, each mine must be in a separate cell).
# show() - display the board in the console as a table of open cell numbers
# (if the cell is not open, the # symbol is displayed).
#
# When creating an instance of the GamePole class, the init()
# method should be called in its constructor for the initial initialization of the game board.
#
# The GamePole class may have other auxiliary methods.
#
# Create an instance pole_game of the GamePole class with a board size of N = 10 and a number of mines M = 12.
#
# P.S. Nothing needs to be displayed on the screen in the program.

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False  # change for hide


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: "#" if not x.fl_open else x.around_mines if not x.mine else "*", row))


pole_game = GamePole(10, 12)