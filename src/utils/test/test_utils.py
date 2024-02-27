import unittest
from utils import distance_point_line

class TestUtils(unittest.TestCase):
    def test_distance_point_line(self):
        point = {"x": 1, "y": 1}
        line = {"a": 1, "b": 1, "c": 1}
        self.assertEqual(distance_point_line(line["a"], line["b"], line["c"], point["x"], point["y"]), 1.4142135623730951)

if __name__ == "__main__":
    unittest.main()
