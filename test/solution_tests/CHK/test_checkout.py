import unittest

from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    """
    This class contains unit tests for the checkout function.

    The tests below are built based on the following criteria:
    +------+-------+---------------------------------+
    | Item | Price | Special offers                  |
    +------+-------+---------------------------------+
    | A    | 50    | 3A for 130, 5A for 200          |
    | B    | 30    | 2B for 45                       |
    | C    | 20    |                                 |
    | D    | 15    |                                 |
    | E    | 40    | 2E get one B free               |
    | F    | 10    | 2F get one F free               |
    | G    | 20    |                                 |
    | H    | 10    | 5H for 45, 10H for 80           |
    | I    | 35    |                                 |
    | J    | 60    |                                 |
    | K    | 70    | 2K for 120                      |
    | L    | 90    |                                 |
    | M    | 15    |                                 |
    | N    | 40    | 3N get one M free               |
    | O    | 10    |                                 |
    | P    | 50    | 5P for 200                      |
    | Q    | 30    | 3Q for 80                       |
    | R    | 50    | 3R get one Q free               |
    | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | U    | 40    | 3U get one U free               |
    | V    | 50    | 2V for 90, 3V for 130           |
    | W    | 20    |                                 |
    | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
    +------+-------+---------------------------------+


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
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21
        }
        for item, price in STANDARD_PRICES.items():
            setattr(self, "test_item_{}".format(item), self.assertEquals(checkout(item), price))

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
        self.assertEqual(checkout("K"*3), 190)

    def test_item_4N_with_2M(self):
        self.assertEqual(checkout("NNNNMM"), 175)

    def test_item_4N_without_M(self):
        self.assertEqual(checkout("N"*4), 160)

    def test_item_6P(self):
        self.assertEqual(checkout("P"*6), 250)

    def test_item_4Q(self):
        self.assertEqual(checkout("Q"*4), 110)

    def test_item_4R_with_3Q(self):
        self.assertEqual(checkout("RRRRQQQ"), 260)

    def test_item_4R_without_Q(self):
        self.assertEqual(checkout("R"*4), 200)

    def test_item_5U(self):
        self.assertEqual(checkout("U"*5), 160)

    def test_item_2V(self):
        self.assertEqual(checkout("VV"), 90)

    def test_item_4V(self):
        self.assertEqual(checkout("VVVV"), 180)

    def test_all_items(self):
        self.assertEqual(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 837)

    def test_no_items(self):
        self.assertEqual(checkout(""), 0)

    def test_illegal_item(self):
        self.assertEqual(checkout("!"), -1)


class TestSTXYZ(unittest.TestCase):
    """ Test buy any 3 of (S,T,X,Y,Z) for 45 """
    def test_items_STX(self):
        self.assertEqual(checkout("STX"), 45)

    def test_items_STXYZZ(self):
        """ Check the deal applies more than once """
        self.assertEqual(checkout("STXYZZ"), 90)

    def test_items_STXYZ(self):
        """ Check price is given by deal """
        self.assertEqual(checkout("STXYZ"), 82)

if __name__ == "__main__":
    unittest.main()






