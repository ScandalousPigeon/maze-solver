class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_colour, width=2
        )