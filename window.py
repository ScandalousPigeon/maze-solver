from tkinter import Tk, BOTH, Canvas
from drawing import *

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.geometry(f"{width}x{height}")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self._root, width=width, height=height)
        self.__canvas.pack(fill='both', expand=True)
        self.__running = False
        
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        """Continually redraws Window as long as self.__running is True."""
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        """Closes the Window."""
        self.__running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)