from .constants import VALUE

def who_won(card1, card2, trump):
    trump = trump[1]
    if card1[1] == card2[1]:
        if VALUE[card1[0]] > VALUE[card2[0]]:
            return card1
        else:
            return card2
    else:
        if (card1[1] == trump) or (card2[1] == trump):
            if card1[1] == trump:
                return card1
            else:
                return card2
        else:
            return card1