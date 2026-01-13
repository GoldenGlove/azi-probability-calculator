from azi import overall_probability_towin
from azi.strategies import weakest, strongest, middle

my_cards = [('9', 'S'), ('Q', 'D'), ('6', 'H')]
trump = ('A', 'S')

first_card = strongest(my_cards, trump)

probability = overall_probability_towin(
    my_cards=my_cards,
    trump=trump,
    first_move=None,
    my_first_turn=False
)

print("My cards:", my_cards)
print("Trump:", trump)
print("Win probability:", probability)
