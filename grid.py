from drawing import *
from window import Window
import tkinter as tk

class Grid:
    """Grid object, grid where the magic happens.

    Class will draw a grid when created.

    Attributes:
        x (int): horizontal distance of the start of the grid from the edge of the window.
        y (int): vertical distance of the start of the grid from the edge of the window.
        num_rows (int): number of rows in the grid.
        num_cols (int): number of columns in the grid.
        cell_size_x (int): how wide each cell in the grid should be, in pixels.
        cell_size_y (int): how tall each cell in the grid should be, in pixels.
        win (Window): the Window on which the grid should be formed.
    """
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        """Method responsible for the drawing of the grid.
        
        Checks if the inputed dimensions are valid and then draws the grid.

        Raises:
            Exception if the inputed dimensions do not fit the self._win object.
        """
        if self._win._width < self._num_rows * self._cell_size_x + self._x * 2 or \
           self._win._height < self._num_cols * self._cell_size_y + self._y * 2: 
            raise Exception("The Window is too small for the specified dimensions.")
        self._cells = [[Cell(0, 0, 0, 0, self._win) for row in range(self._num_rows)] for column in range(self._num_cols)]
        # Cell(0, 0, 0, 0, self._win) are placeholder cells that will be mutated with self._draw_cell().
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        """Helper method for self._create_cells().
        
        Calculates the coordinates for the given cell in the grid and then draws it.

        Args:
            i (int): which column in the grid the cell is located.
            j (int): which row in the grid the cell is located.
        """
        x1 = self._x + i * self._cell_size_x
        y1 = self._y + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        new_cell = Cell(x1, y1, x2, y2, self._win)
        new_cell.draw()
        self._animate()

    def _animate(self):
        """Helper method for self._create_cells().

        Redraws the Window using Window.redraw(), and then introduces a 50ms delay.
        """
        self._win.redraw()
        self._win._root.after(50)