# noinspection PyUnusedLocal
# skus = unicode string

def apply_A_deals(itemCounts, totalPrice=0):
    """ For offers buy 5A for 200, 3A for 130"""
    OFFER_PRICE_FOR_5A = 200
    OFFER_PRICE_FOR_3A = 130
    if "A" in itemCounts.keys():
        # Apply 5A deal first
        if itemCounts["A"] >= 5:
            totalOfferPrice = itemCounts["A"] // 5 * OFFER_PRICE_FOR_5A
            totalPrice += totalOfferPrice
            itemCounts["A"] = itemCounts["A"] % 5
        if itemCounts["A"] >= 3:
            # Apply 3A deal
            totalOfferPrice = itemCounts["A"] // 3 * OFFER_PRICE_FOR_3A
            totalPrice += totalOfferPrice
            itemCounts["A"] = itemCounts["A"] % 3
    return itemCounts, totalPrice


def apply_B_deal(itemCounts, totalPrice=0):
    """ For offer buy 2B for 45"""
    OFFER_PRICE = 45
    REQUIRED_FOR_OFFER = 2
    if "B" in itemCounts.keys() and itemCounts["B"] >= REQUIRED_FOR_OFFER:
        totalOfferPrice = itemCounts["B"] // REQUIRED_FOR_OFFER * OFFER_PRICE
        totalPrice += totalOfferPrice
        itemCounts["B"] = itemCounts["B"] % REQUIRED_FOR_OFFER
    return itemCounts, totalPrice


def apply_E_deal(itemCounts, totalPrice=0):
    """ For offer buy 2E get one B free"""
    if "E" in itemCounts.keys()\
            and "B" in itemCounts.keys():
        offerCount = itemCounts["E"] // 2
        itemCounts["B"] -= offerCount
    return itemCounts, totalPrice


def apply_F_deal(itemCounts, totalPrice=0):
    """ For offer buy 2F get one F free (i.e. for every 3F you buy, one of those 3 is free)"""
    if "F" in itemCounts.keys():
        itemCounts["F"] -= itemCounts["F"] // 3
    return itemCounts, totalPrice


def checkout(skus):
    """
    This function accepts a string containing items and returns the total value as iteger.
    The value of each item is listed below:

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

    STD_PRICES = {
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

    itemCount = {}

    # Count the number of occurences all items in skus
    for item in skus:
        if item in itemCount:
            itemCount[item] += 1
        else:
            itemCount[item] = 1

    # Total the number of items from the itemCount
    totalPrice = 0

    itemCount, totalPrice = apply_E_deal(itemCount, totalPrice)
    itemCount, totalPrice = apply_A_deals(itemCount, totalPrice)
    itemCount, totalPrice = apply_B_deal(itemCount, totalPrice)
    itemCount, totalPrice = apply_F_deal(itemCount, totalPrice)

    # Iterate over any remaining items in itemCount
    try:
        for item, count in itemCount.items():
            totalPrice += STD_PRICES[item] * count
    except KeyError:
        return -1
    else:
        return totalPrice

