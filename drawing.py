class Point:
    """Simple Point class representing a coordinate on the window."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        """Line class. Takes two Points as input, each being the endpoint of a Line."""
        self.start = start
        self.end = end

    def draw(self, canvas, fill_colour):
        """Attempts to draw a line using the input Points."""
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_colour, width=2
        )

class Cell:
    """Represents a single cell in the maze.

    Cell is modelled based on the top left and bottom right corners.

    Attributes:
        has_left_wall (bool): whether the cell has a left wall.
        has_right_wall (bool): whether the cell has a right wall.
        has_top_wall (bool): whether the cell has a top wall.
        has_bottom_wall (bool): whether the cell has a bottom wall.
        x1 (int): x coordinate of the top left corner of the cell.
        y1 (int): y coordinate of the top left corner of the cell.
        x2 (int): x coordinate of the bottom right corner of the cell.
        y2 (int): y coordinate of the bottom right corner of the cell.
        win (Window): the Window on which the cell is drawn upon.
    """
    def __init__(self, x1, y1, x2, y2, win):
        """Initialises a Cell object."""
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self._win = win
        self.visited = False

    def __repr__(self):
        """For testing purposes."""
        return f"Cell({self.has_left_wall}, {self.has_right_wall}, {self.has_top_wall}, {self.has_bottom_wall})"

    def draw(self):
        """Method responsible for graphically drawing the cell.
        
        Draws a #D9D9D9 line if the corresponding has_wall attribute is False.
        #D9D9D9 was chosen because that's what my system's tk background is.
        """
        top_left = Point(self.x1, self.y1)
        top_right = Point(self.x2, self.y1)
        bottom_left = Point(self.x1, self.y2)
        bottom_right = Point(self.x2, self.y2)
        left_wall_colour = "black"
        right_wall_colour = "black"
        top_wall_colour = "black"
        bottom_wall_colour = "black"
        if not self.has_left_wall:
            left_wall_colour = "#D9D9D9"
        left_wall = Line(top_left, bottom_left)
        self._win.draw_line(left_wall, left_wall_colour)
        if not self.has_right_wall:
            right_wall_colour = "#D9D9D9"
        right_wall = Line(top_right, bottom_right)
        self._win.draw_line(right_wall, right_wall_colour)
        if not self.has_top_wall:
            top_wall_colour = "#D9D9D9"
        top_wall = Line(top_left, top_right)
        self._win.draw_line(top_wall, top_wall_colour)
        if not self.has_bottom_wall:
            bottom_wall_colour = "#D9D9D9"
        bottom_wall = Line(bottom_left, bottom_right)
        self._win.draw_line(bottom_wall, bottom_wall_colour)
            
    def draw_move(self, to_cell, undo=False):
        if undo:
            colour = "gray"
        else:
            colour = "red"

        own_centre_x = (self.x1 + self.x2) / 2
        own_centre_y = (self.y1 + self.y2) / 2
        own_centre = Point(own_centre_x, own_centre_y)

        other_centre_x = (to_cell.x1 + to_cell.x2) / 2
        other_centre_y = (to_cell.y1 + to_cell.y2) / 2
        other_centre = Point(other_centre_x, other_centre_y)

        new_line = Line(own_centre, other_centre)

        self._win.draw_line(new_line, colour)
