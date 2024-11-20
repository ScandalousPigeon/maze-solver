from window import *

def main():
    window = Window(800, 600)
    point1 = Point(0, 0)
    point2 = Point(40, 40)
    new_line = Line(point1, point2)
    window.draw_line(new_line, "blue")
    window.wait_for_close()

if __name__ == "__main__":
    main()