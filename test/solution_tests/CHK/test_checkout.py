import unittest

from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    """
    This class contains unit tests for the checkout function

    The tests below are built 
    """
    def test_item_A(self):
        self.assertEquals(checkout("AAA"), 180)


if __name__ == '__main__':
    unittest.main()
