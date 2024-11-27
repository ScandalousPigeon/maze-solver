from drawing import *
from window import Window
import tkinter as tk
import random

class Maze:
    """Maze object, Maze where the magic happens.

    Class will draw a Maze when created.

    Attributes:
        x (int): horizontal distance of the start of the Maze from the edge of the window.
        y (int): vertical distance of the start of the Maze from the edge of the window.
        num_rows (int): number of rows in the Maze.
        num_cols (int): number of columns in the Maze.
        cell_size_x (int): how wide each cell in the Maze should be, in pixels.
        cell_size_y (int): how tall each cell in the Maze should be, in pixels.
        win (Window): the Window on which the Maze should be formed.
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
        if num_rows != num_cols:
            raise Exception("Maze must be a square.")
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = None # for debugging
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        """Method responsible for the drawing of the Maze.
        
        Checks if the inputed dimensions are valid and then draws the Maze.

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
        
        Calculates the coordinates for the given cell in the Maze and then draws it.

        Args:
            i (int): which column in the Maze the cell is located.
            j (int): which row in the Maze the cell is located.
        """
        x1 = self._x + i * self._cell_size_x
        y1 = self._y + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].x1 = x1
        self._cells[i][j].y1 = y1
        self._cells[i][j].x2 = x2
        self._cells[i][j].y2 = y2
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        """Helper method for self._create_cells().

        Redraws the Window using Window.redraw(), and then introduces a 50ms delay.
        """
        self._win.redraw()
        self._win._root.after(20)
    
    def _break_entrance_and_exit(self):
        """Method that creates an entrance and exit in the Maze.
        
        'Breaks' the top wall of the top left block, and
        'breaks' the bottom wall of the bottom right block.
        """
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        """Method to create a path through the maze, by breaking walls.
        
        Args:
            i (int): the current column.
            j (int): the current row.
        """
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i < len(self._cells) - 1:
                if not self._cells[i + 1][j].visited:
                    possible_directions.append((i + 1, j))
            if 0 < i:
                if not self._cells[i - 1][j].visited:
                    possible_directions.append((i - 1, j))
            if j < len(self._cells) - 1:
                if not self._cells[i][j + 1].visited:
                    possible_directions.append((i, j + 1))
            if 0 < j:
                if not self._cells[i][j - 1].visited:
                    possible_directions.append((i, j - 1))
            if not possible_directions:
                self._cells[i][j].draw()
                return
            direction = random.randint(0, len(possible_directions) - 1)
            chosen = possible_directions[direction]
            # four cases to consider. x1y1 = x2y1 or x1y2
            # and x2y2 = x2y1 or x1y2. we use this to find which border is touching.
            if chosen == (i, j - 1):
                # then this cell is above the current cell.
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                self._cells[i][j].draw()
                self._cells[i][j - 1].draw()
                self._break_walls_r(i, j - 1)
            if chosen == (i - 1, j):
                # then this cell is to the left of the current cell.
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
                self._cells[i][j].draw()
                self._cells[i - 1][j].draw()
                self._break_walls_r(i - 1, j)
            if chosen == (i, j + 1):
                # then this cell is below the current cell.
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                self._cells[i][j].draw()
                self._cells[i][j + 1].draw()
                self._break_walls_r(i, j + 1)
            if chosen == (i + 1, j):
                # then this cell is to the right of the current cell.
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                self._cells[i][j].draw()
                self._cells[i + 1][j].draw()
                self._break_walls_r(i + 1, j)

    def _reset_cells_visited(self):
        """Method to reset the visited attributes of every Cell in the Maze to False."""
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _solve(self):
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        # Base case: reached the bottom-right cell
        if self._cells[i][j] is self._cells[-1][-1]:
            return True

        # Move up
        if not self._cells[i][j].has_top_wall and j > 0:  # Add boundary check for 'j > 0'
            if not self._cells[i][j - 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)

        # Move down
        if not self._cells[i][j].has_bottom_wall and j < self._num_rows - 1:  # Add boundary check for 'j < self._num_rows - 1'
            if not self._cells[i][j + 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

        # Move left
        if not self._cells[i][j].has_left_wall and i > 0:  # Add boundary check for 'i > 0'
            if not self._cells[i - 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)

        # Move right
        if not self._cells[i][j].has_right_wall and i < self._num_cols - 1:  # Add boundary check for 'i < self._num_cols - 1'
            if not self._cells[i + 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        return False
