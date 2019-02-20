import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    """
    This class contains unit tests for the checkout function.

    The tests below are built based on the following criteria:
        +------+-------+----------------+
        | Item | Price | Special
        offers |
        +------+-------+----------------+
        | A | 50 | 3A for 130 |
        | B | 30 | 2B for 45 |
        | C | 20 | |
        | D | 15 | |
        +------+-------+----------------+

        Notes:
        - For any illegal input return -1
    """

    def test_item_A(self):
        self.assertEqual(checkout("AAAA"), 180)

    def test_item_B(self):
        self.assertEqual(checkout("BBB"), 75)

    def test_item_C(self):
        self.assertEqual(checkout("C"), 20)

    def test_item_D(self):
        self.assertEqual(checkout("D"), 15)

    def test_mixed_items(self):
        self.assertEqual(checkout("ABCD"), 115)

    def test_illegal_input(self):
        self.assertEqual(checkout("ABCDZ"), -1)

    def test_no_items(self):
        self.assertEqual(checkout(""), 0)


if __name__ == "__main__":
    unittest.main()

