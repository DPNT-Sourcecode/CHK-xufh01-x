# noinspection PyUnusedLocal
# skus = unicode string

def deal_for_better_price(itemCount, totalPrice, numberRequired, dealPrice):
    """ For offers such as buy 3A for 130
        This also works for offers like buy 3A get one A free, as this is the same as saying buy 4A for the price of 3
    """
    if itemCount >= numberRequired:
        dealCount = itemCount // numberRequired
        itemCount = itemCount % numberRequired
        totalPrice += dealCount * dealPrice
    return itemCount, totalPrice


def deal_for_different_item_free(itemCounts, item, numberRequired, freeItem):
    """ For offers such as buy 3A get one B free """
    if item in itemCounts.keys() and freeItem in itemCounts.keys():
        offerCount = itemCounts[item] // numberRequired
        itemCounts[freeItem] -= offerCount
    return itemCounts


def apply_STXYZ_deal(itemCounts, totalPrice):
    """ For offers buy any of (S, T, X, Y, Z) for 45"""
    VALID_ITEMS = ("Z", "S", "T", "Y", "X")
    totalCount = 0
    for item in VALID_ITEMS:
        if item in itemCounts.keys():
            totalCount += itemCounts[item]
    if totalCount >= 3:
        totalPrice += totalCount // 3 * 45
        itemsToRemove = totalCount - totalCount % 3
        for item in VALID_ITEMS:
            if itemsToRemove == 0:
                break
            elif item in itemCounts.keys():
                amountRemoving = min(itemsToRemove, itemCounts[item])
                itemCounts[item] -= amountRemoving
                itemsToRemove -= amountRemoving
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

    DEALS_FOR_DIFFERENT_ITEM_FREE = [
        ( "E", 2, "B" ),
        ( "N", 3, "M" ),
        ( "R", 3, "Q" )
    ]

    DEALS_FOR_BETTER_PRICE = [
        ( "A", 5, 200 ),
        ( "A", 3, 130 ),
        ( "B", 2, 45 ),
        ( "F", 3, 20 ),
        ( "H", 10, 80 ),
        ( "H", 5, 45 ),
        ( "K", 2, 150 ),
        ( "P", 5, 200 ),
        ( "Q", 3, 80 ),
        ( "U", 4, 120 ),
        ( "V", 3, 130 ),
        ( "V", 2, 90 ),
    ]

    itemCounts = {}

    # Count the number of occurences all items in skus
    for item in skus:
        if item in itemCounts:
            itemCounts[item] += 1
        else:
            itemCounts[item] = 1

    # Total the number of items from the itemCount
    totalPrice = 0

    # Iterate over deals for free items:
    for deal in DEALS_FOR_DIFFERENT_ITEM_FREE:
        requiredItem = deal[0]
        numberRequired = deal[1]
        freeItem = deal[2]
        itemCounts = deal_for_different_item_free(itemCounts,
                                                  requiredItem,
                                                  numberRequired,
                                                  freeItem)

    # Iterate over deals for better price:
    for deal in DEALS_FOR_BETTER_PRICE:
        item = deal[0]
        if item in itemCounts.keys():
            numberRequired = deal[1]
            dealPrice = deal[2]
            itemCounts[item], totalPrice = deal_for_better_price(itemCounts[item],
                                                                 totalPrice,
                                                                 numberRequired,
                                                                 dealPrice)

    itemCounts, totalPrice = apply_STXYZ_deal(itemCounts, totalPrice)

    # Iterate over any remaining items in itemCount
    try:
        for item, count in itemCounts.items():
            totalPrice += STD_PRICES[item] * count
    except KeyError:
        return -1
    else:
        return totalPrice





