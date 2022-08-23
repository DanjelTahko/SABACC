

def calculate(hand):
    """
    for i in range(len(hand)):

        if (0 in hand[i]['num']):
            print("zero")
    """

    totti = 0

    for j in range(len(hand)):
        totti += hand[j].get_card_value()['number']

    print(totti)
