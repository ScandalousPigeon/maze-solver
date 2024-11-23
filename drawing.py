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

        self._top_left = Point(x1, y1)
        self._top_right = Point(x2, y1)
        self._bottom_left = Point(x1, y2)
        self._bottom_right = Point(x2, y2)

        self._win = win

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(self._top_left, self._bottom_left)
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(self._top_right, self._bottom_right)
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(self._top_left, self._top_right)
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(self._bottom_left, self._bottom_right)
            self._win.draw_line(bottom_wall, "black")
            
