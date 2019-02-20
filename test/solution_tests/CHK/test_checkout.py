import unittest

from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_item_A(self):
        self.assertEquals(checkout("A"), 180)


if __name__ == '__main__':
    unittest.main()