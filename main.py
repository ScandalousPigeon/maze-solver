from window import *
from maze import Maze

def main():
    window = Window(940, 1000)
    
    """
    dead_cells = Cell(50, 50, 110, 110, window)
    second_cell = Cell(150, 150, 400, 400, win1dow)
    dead_cells.draw()
    second_cell.draw()
    dead_cells.draw_move(second_cell, True)
    """
    maze = Maze(40, 40, 30, 30, 25, 25, window)
    maze._solve()
    window.wait_for_close()

if __name__ == "__main__":
    main()