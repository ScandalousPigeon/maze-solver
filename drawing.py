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
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        

        self._win = win

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall, "black")
            
    def draw_move(self, to_cell, undo=False):
        if undo:
            colour = "gray"
        else:
            colour = "red"

        own_centre_x = (self._x1 + self._x2) / 2
        own_centre_y = (self._y1 + self._y2) / 2
        own_centre = Point(own_centre_x, own_centre_y)

        other_centre_x = (to_cell._x1 + to_cell._x2) / 2
        other_centre_y = (to_cell._y1 + to_cell._y2) / 2
        other_centre = Point(other_centre_x, other_centre_y)

        new_line = Line(own_centre, other_centre)

        self._win.draw_line(new_line, colour)
