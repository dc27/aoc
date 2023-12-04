import re
from collections import defaultdict

file = 'input.txt'

lines = [line.strip() for line in open(file, 'r')]

def number_string_to_list(number_string:int)->list:
    """
    Turns a string representation of a 'list' of numbers into a list object.

    " 1 2 3 4 5" -> [1, 2, 3, 4, 5]
    """

    return list(map(int, re.findall(r'\d+', number_string)))

# store card instances as a dictionary. There will be times when the keys don't exist yet --> use defaultdict 
card_instances = defaultdict(int)

for line in lines:
    
    # 1. parse (split) line into components: game no. , [winning numbers], [player numbers]:
    card_no, lottery_numbers = line.split(': ')
    # file uses spaces to pad --> use regex (ew)
    card_no = int(re.findall(r'\d+', card_no)[0])
    card_instances[card_no] += 1
    winning_numbers, player_numbers = lottery_numbers.split('| ')
    winning_numbers = number_string_to_list(winning_numbers)
    player_numbers = number_string_to_list(player_numbers)

    # 2. score the current card
    score = 0

    for n in player_numbers:
        if n in winning_numbers:
            score += 1

    # need to repeat the process for each instance of the card:
    # "Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4."
    # "Your copy of card 2 also wins one copy each of cards 3 and 4."
    for i in range(0, card_instances[card_no]):
        # process applies to the NEXT card --> start at 1
        for next_card in range(1, score+1):
            card_instances[card_no+next_card] += 1

    
print(sum(card_instances.values()))