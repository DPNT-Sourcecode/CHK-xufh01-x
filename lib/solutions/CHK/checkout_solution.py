

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

    ITEM_VALUES = {
        "A" : {
            "stdPrice" : 50,
            "offerPrice" : 130,
            "requiredForOffer" : 3,
        },
        "B" : {
            "stdPrice" : 30,
            "offerPrice" : 45,
            "requiredForOffer" : 2,
        },
        "C" : {
            "stdPrice" : 20,
        },
        "D" : {
            "stdPrice" : 15,
        }
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
    try:
        for item, count in itemCount.items():
            itemPrices = ITEM_VALUES[item]
            if "offerPrice" in itemPrices.keys():
                numberOfOffers = count // itemPrices["requiredForOffer"]
                totalPrice += numberOfOffers * itemPrices["offerPrice"]
                count = count % itemPrices["requiredForOffer"]
            totalPrice += count * itemPrices["stdPrice"]
    except KeyError:
        return -1
    else:
        return totalPrice





