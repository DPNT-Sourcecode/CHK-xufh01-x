import unittest

from lib.solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    def test_item_A(self):
        self.assertEquals(checkout_solution("A"), 180)


if __name__ == '__main__':
    unittest.main()

