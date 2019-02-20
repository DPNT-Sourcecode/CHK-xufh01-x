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
    | F    | 10    | 2F get one F free      |
    | G    | 20    |                        |
    | H    | 10    | 5H for 45, 10H for 80  |
    | I    | 35    |                        |
    | J    | 60    |                        |
    | K    | 80    | 2K for 150             |
    | L    | 90    |                        |
    | M    | 15    |                        |
    | N    | 40    | 3N get one M free      |
    | O    | 10    |                        |
    | P    | 50    | 5P for 200             |
    | Q    | 30    | 3Q for 80              |
    | R    | 50    | 3R get one Q free      |
    | S    | 30    |                        |
    | T    | 20    |                        |
    | U    | 40    | 3U get one U free      |
    | V    | 50    | 2V for 90, 3V for 130  |
    | W    | 20    |                        |
    | X    | 90    |                        |
    | Y    | 10    |                        |
    | Z    | 50    |                        |
    +------+-------+------------------------+


    Notes:
     - The policy of the supermarket is to always favor the customer when applying special offers.
     - All the offers are well balanced so that they can be safely combined.
     - For any illegal input return -1
    """
    def test_standard_prices(self):
        """Test all of the standard item prices"""
        STANDARD_PRICES = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 80,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 30,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 90,
            "Y": 10,
            "Z": 50
        }
        for item, price in STANDARD_PRICES.items():
            self.assertEquals(checkout(item), price)

    def test_item_4A(self):
        self.assertEqual(checkout("AAAA"), 180)

    def test_item_6A(self):
        self.assertEqual(checkout("AAAAAA"), 250)

    def test_item_3B(self):
        self.assertEqual(checkout("BBB"), 75)

    def test_item_E_deal_with_B(self):
        self.assertEqual(checkout("EEEBB"), 150)

    def test_item_E_deal_without_B(self):
        self.assertEqual(checkout("EE"), 80)

    def test_item_4F(self):
        self.assertEqual(checkout("FFFF"), 30)

    def test_item_6H(self):
        self.assertEqual(checkout("H"*6), 55)

    def test_item_11H(self):
        self.assertEqual(checkout("H"*11), 90)

    def test_item_2K(self):
        self.assertEqual(checkout("K"*3), 230)

    def test_item_4N_with_2M(self):
        self.assertEqual(checkout("NNNNMM"), 175)

    def test_item_4N_without_M(self):
        self.assertEqual(checkout("N"*4), 160)

    def test_item_6P(self):
        self.assertEqual(checkout("P"*6), 250)

    def test_item_4Q(self):
        self.assertEqual(checkout("Q"*4), 250)


    def test_mixed_items(self):
        self.assertEqual(checkout("ABCDE"), 155)

    def test_no_items(self):
        self.assertEqual(checkout(""), 0)

    def test_illegal_item(self):
        self.assertEqual(checkout("ABCDEZ"), -1)


if __name__ == "__main__":
    unittest.main()



