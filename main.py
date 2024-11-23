from window import *

def main():
    window = Window(800, 600)
    
    dead_cells = Cell(50, 50, 110, 110, window)
    dead_cells.draw()
    window.wait_for_close()

if __name__ == "__main__":
    main()