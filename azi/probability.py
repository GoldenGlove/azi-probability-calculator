import random 
from itertools import combinations
from .constants import CARDS, VALUE
from .core import who_won

I_WIN = 1
OPPONENT_WIN = 0
NUMBER_OF_CARDS = 27

cards_selected = random.sample(range(NUMBER_OF_CARDS), 7)
                     

def opponent_possible_cards(my_cards, trump, all_cards):
    remaining_cards = all_cards.copy()
    remaining_cards.remove(trump)
    for x in my_cards:
        remaining_cards.remove(x)
    return list(combinations(remaining_cards, 3))


def all_possible_outcomes(my_cards, opp_cards, trump, my_turn):
    trump = trump
    cards1_stage1 = my_cards
    cards2_stage1 = opp_cards
    stage1 = []
    stage2 = []
    stage3 = []
    if my_turn:
        for x1 in cards1_stage1:
            mark = x1[1]
            available_1 = []

            for check in cards2_stage1:
                if check[1] == mark:
                    available_1.append(check)
            if len(available_1) != 0:
                available_1 = available_1 
            else:
                available_1 = [x for x in cards2_stage1 if x[1] == trump[1]]

                if len(available_1) != 0:
                    available_1 = available_1
                else:
                    available_1 = [x for x in cards2_stage1]
            
            for avail in available_1:
                stage1.append([x1, avail])
                
    else:
        for x1 in cards2_stage1:
            mark = x1[1]
            available_1 = []

            for check in cards1_stage1:
                if check[1] == mark:
                    available_1.append(check)
            if len(available_1) != 0:
                available_1 = available_1 
            else:
                available_1 = [x for x in cards1_stage1 if x[1] == trump[1]]

                if len(available_1) != 0:
                    available_1 = available_1
                else:
                    available_1 = [x for x in cards1_stage1]
            
            for avail in available_1:
                stage1.append([x1, avail])
                

    for stage in stage1:

        cards1_stage2 = my_cards.copy()
        cards2_stage2 = opp_cards.copy()
        available_2 = []
        for card in stage:
            if card in my_cards:
                cards1_stage2.remove(card)
            else:
                cards2_stage2.remove(card)


        if who_won(stage[0], stage[1], trump) in my_cards:

            for x1 in cards1_stage2:
                available_2 = []
                mark = x1[1]

                for check in cards2_stage2:
                    if check[1] == mark:
                        available_2.append(check)

                if len(available_2) != 0:
                    available_2 = available_2.copy()
                else:
                    available_2 = [x for x in cards2_stage2 if x[1] == trump[1]]

                    if len(available_2) != 0:
                        available_2 = available_2.copy()
                    else:
                        available_2 = [x for x in cards2_stage2]
                
                for avail1 in available_2:
                    stage2.append([stage, x1, avail1])

        elif who_won(stage[0], stage[1], trump) in opp_cards:

            for x1 in cards2_stage2:
                available_2 = []
                mark = x1[1]

                for check in cards1_stage2:
                    if check[1] == mark:
                        available_2.append(check)
                if len(available_2) != 0:
                    available_2 = available_2.copy() 
                else:
                    available_2 = [x for x in cards1_stage2 if x[1] == trump[1]]

                    if len(available_2) != 0:
                        available_2 = available_2.copy()
                    else:
                        available_2 = [x for x in cards1_stage2]

                for avail1 in available_2:
                    stage2.append([stage, x1, avail1])
    for i in range(len(stage2)):
        stage2[i] = stage2[i][0][0], stage2[i][0][1], stage2[i][1], stage2[i][2]


    for stage in stage2:
        cards1_stage3 = my_cards.copy()
        cards2_stage3 = opp_cards.copy()
        for card in stage:
            if card in my_cards:
                cards1_stage3.remove(card)
            else:
                cards2_stage3.remove(card)
        if who_won(stage[-2], stage[-1], trump) in my_cards:
            stage3.append([stage, cards1_stage3[0], cards2_stage3[0]])
        else:
            stage3.append([stage, cards2_stage3[0], cards1_stage3[0]])
    for i in range(len(stage3)):
        stage3[i] = list(stage3[i][0]) + [stage3[i][1], stage3[i][2]]
    return stage3



def chance_to_win(my_cards, outcomes, trump):
    my_wins = []
    trump = trump[1]
    score = []
    results = []
    for outcome in outcomes:
        for i in range(0,6, 2):
            if outcome[i][1] == outcome[i+1][1]:
                if VALUE[outcome[i][0]] > VALUE[outcome[i + 1][0]]:
                    score.append(1 if outcome[i] in my_cards else 0)
                else:
                    score.append(0 if outcome[i] in my_cards else 1)
            else:
                if (outcome[i][1] == trump) or (outcome[i+1][1] == trump):
                    if outcome[i][1] == trump:
                        score.append(I_WIN if outcome[i] in my_cards else OPPONENT_WIN)
                    else:
                        score.append(OPPONENT_WIN if outcome[i] in my_cards else I_WIN)
                else:
                    score.append(I_WIN if outcome[i] in my_cards else OPPONENT_WIN)
        if score.count(1) > score.count(0):
            results.append(1)
            my_wins.append(outcome)
        else:
            results.append(0)
        score = []
    chance_to_win = round((results.count(1)/ len(outcomes) * 100), 2)
    results = []

    return chance_to_win

    

def overall_probability_towin(my_cards, trump, 
                              first_move, 
                              my_first_turn):
    chance = []

    set_of_cards = opponent_possible_cards(my_cards, trump, CARDS)
    for x in set_of_cards:
        outcomes = all_possible_outcomes(my_cards, list(x), trump, my_first_turn)  
        if first_move != None:
            chosen_card = first_move 
            outcomes = [o for o in outcomes if o[0] == chosen_card]
        chance.append(chance_to_win(my_cards, outcomes, trump))

        prob = (round(sum(chance)/ len(chance), 2))

    return prob





