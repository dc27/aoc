from collections import Counter, defaultdict

file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
values = range(14, 1, -1)
value_lookup = dict(zip(labels, values))

# 5 > 4 > 3,2 > 3 > 2,2 > 2 > 1
# thereafter first higher card wins
# e.g. 77888 > 77788 (both full house, card one is the same, card two is the same, card 3 is higher for 77888)

# selection sort?

# Here's how it works:

# Find the smallest element in the array and swap it with the first element.
# Find the second smallest element and swap with with the second element in the array.
# Find the third smallest element and swap wit with the third element in the array.
# Repeat the process of finding the next smallest element and swapping it into the correct position until the entire array is sorted.


def get_hand_rank(hand:str)->int:
    """
    
    """

    cards = Counter(hand)
    card_counts = list(cards.values())

    if len(card_counts) == 1:
        return(1)
    
    if len(card_counts) == 2:
        return(6 - max(card_counts)) # returns 2 or 3
    
    if len(card_counts) == 3:
        return(7 - max(card_counts)) # returns 4 or 5
    
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

for line in input_stream:
    hand, bid = line.split()
    rank = get_hand_rank(hand)

    n_hands_at_rank = len(ordered_hands[rank])

    if n_hands_at_rank == 0:
        ordered_hands[rank].append(dict(hand = hand, bid = bid))

    else:
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

for i, hand in enumerate(ranked_hands[::-1]):
    
    sum += (i + 1) * int(hand["bid"])

print(sum)
