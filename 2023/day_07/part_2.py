from collections import Counter, defaultdict

file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
values = range(14, 1, -1)
value_lookup = dict(zip(labels, values))

# 5 > 4 > 3,2 > 3 > 2,2 > 2 > 1
# thereafter first higher card wins
# e.g. 77888 > 77788 (both full house, card one is the same, card two is the same, card 3 is higher for 77888)


def get_hand_rank(hand:str)->int:
    """
    
    """
    jokers = hand.count("J")
    cards = Counter(hand.replace('J', ''))
    card_counts = list(cards.values())

    # sneaky edge case if they are all jokers!
    if len(card_counts) <= 1:
        return(1)
    
    if len(card_counts) == 2:
        return(6 - (max(card_counts) + jokers)) # returns 2 or 3
    
    if len(card_counts) == 3:
        return(7 - (max(card_counts) + jokers)) # returns 4 or 5
    
    if len(card_counts) == 4:
        return(6)
    
    # high card
    return(7)

def beats_hand(hand:str, ref:str)->bool:
    for c, d in zip(hand, ref):
        if c!=d:
            return(value_lookup[c] > value_lookup[d])
        
    return None


ordered_hands = defaultdict(list)

# go through input, put each hand in it's according position.
for line in input_stream:
    hand, bid = line.split()
    rank = get_hand_rank(hand)

    n_hands_at_rank = len(ordered_hands[rank])

    # no hands have been placed at that rank (e.g. no full houses yet)
    if n_hands_at_rank == 0:
        ordered_hands[rank].append(dict(hand = hand, bid = bid))

    # bit more complicated, need to put that hand in the correct position for hands of
    # its rank
    else:
        # until it's been put in, keep trying places. if it's smaller than the current value,
        # put it before it. if it's not smaller than any existing value, put it at the end.

        # starting positions
        i = 0
        end_i = n_hands_at_rank - 1
        hand_placed = False
        while not hand_placed:
            if beats_hand(hand, ordered_hands[rank][i]["hand"]):
                ordered_hands[rank].insert(i, dict(hand = hand, bid = bid))
                hand_placed = True
            
            elif i == end_i:
                ordered_hands[rank].append(dict(hand = hand, bid = bid))
                hand_placed = True

            i += 1

# nested lists give me nightmares
ranked_hands = [hand for k, v in sorted(ordered_hands.items()) for hand in v]

sum = 0

# need to reverse the list (best hand is last)
for i, hand in enumerate(ranked_hands[::-1]):
    # print(i, hand)
    sum += (i + 1) * int(hand["bid"])

print(sum)

