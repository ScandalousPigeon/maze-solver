import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def setUp(self):
        """Sets up common objects for testing."""
        self.window = Window(1000, 1000)

    def test_maze_create_cells(self):
        """Tests for correct initialisation."""
        num_cols = 12
        num_rows = 10
        m1 = Maze(80, 80, num_rows, num_cols, 10, 10, self.window)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_invalid_dimensions(self):
        """Tests if Exception is raised if the Window is too small."""
        with self.assertRaises(Exception) as context:
            Maze(1000, 1000, 1000, 1000, 20, 20, self.window)
        self.assertEqual(str(context.exception), "The Window is too small for the specified dimensions.")

    def test_maze_break_entrance_and_exit(self):
        num_cols = 16
        num_rows = 10
        m1 = Maze(30, 30, num_rows, num_cols, 10, 10, self.window)
        self.assertEqual(
            m1._cells[0][0].has_top_wall or m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall or m1._cells[-1][-1].has_right_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()