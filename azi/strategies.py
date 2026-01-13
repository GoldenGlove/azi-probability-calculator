from .constants import VALUE

def strongest(cards, trump):
    trumps = [c for c in cards if c[1] == trump[1]]
    return max(trumps or cards, key=lambda c: VALUE[c[0]])

def weakest(cards, trump):
    non_trumps = [c for c in cards if c[1] != trump[1]]
    return min(non_trumps or cards, key=lambda c: VALUE[c[0]])

def middle(cards, trump):
    s = strongest(cards, trump)
    w = weakest(cards, trump)
    for c in cards:
        if c != s and c != w:
            return c
    return None
