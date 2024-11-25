import unittest
from grid import Grid
from window import Window

class Tests(unittest.TestCase):
    def setUp(self):
        """Sets up common objects for testing."""
        self.window = Window(1000, 1000)
    def test_grid_create_cells(self):
        """Tests for correct initialisation."""
        num_cols = 12
        num_rows = 10
        m1 = Grid(0, 0, num_rows, num_cols, 10, 10, self.window)
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
            Grid(1000, 1000, 1000, 1000, 20, 20, self.window)
        self.assertEqual(str(context.exception), "The Window is too small for the specified dimensions.")

if __name__ == "__main__":
    unittest.main()