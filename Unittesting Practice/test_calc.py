import unittest
import calc


class TestCalc(unittest.TestCase):

    # all tests must begin with the word test
    # example: "test_"

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # assertRaises method checks if a certain value is raised
        # in this case we are using the syntax below to confirm that our
        # divide function would indeed raise a ValueError when passing in (10,0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


if __name__ == "__main__":
    unittest.main()
