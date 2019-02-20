import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    """
    This class contains unit tests for the checkout function.

    The tests below are built based on the following criteria:
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        +------+-------+------------------------+


        Notes:
         - The policy of the supermarket is to always favor the customer when applying special offers.
         - All the offers are well balanced so that they can be safely combined.
         - For any illegal input return -1
    """

    def test_item_3A(self):
        self.assertEqual(checkout("AAAA"), 180)

    def test_item_6A(self):
        self.assertEqual(checkout("AAAAA"), 200)

    def test_item_B(self):
        self.assertEqual(checkout("BBB"), 75)

    def test_item_C(self):
        self.assertEqual(checkout("C"), 20)

    def test_item_D(self):
        self.assertEqual(checkout("D"), 15)

    def test_item_E(self):
        self.assertEqual(checkout("E"), 40)

    def test_item_E_deal_with_B(self):
        self.assertEqual(checkout("EEEBB"), 40)



    def test_mixed_items(self):
        self.assertEqual(checkout("ABCD"), 115)

    def test_illegal_input(self):
        self.assertEqual(checkout("ABCDZ"), -1)

    def test_no_items(self):
        self.assertEqual(checkout(""), 0)


if __name__ == "__main__":
    unittest.main()
