

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    This function accepts a string containing items and returns the total value as iteger.
    The value of each item is listed below:

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

    STANDARD_ITEM_VALUES = {
        "A" : {
            "stdVal" : 50,
            "dealVal" : 130,
            "requiredForDeal" : 3,
            
        }
    }

