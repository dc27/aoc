import re

file = 'input.txt'

lines = [line.strip() for line in open(file, 'r')]

def number_string_to_list(number_string:int)->list:
    return list(map(int, re.findall(r'\d+', number_string)))

# init cumsum. total score of cards
total_score = 0

for line in lines:
    
    # 1. parse (split) line into components: game no. , [winning numbers], [player numbers]:
    game_no, lottery_numbers = line.split(': ')
    winning_numbers, player_numbers = lottery_numbers.split('| ')
    winning_numbers = number_string_to_list(winning_numbers)
    player_numbers = number_string_to_list(player_numbers)

    score_mod = -1

    for n in player_numbers:
        if n in winning_numbers:
            score_mod += 1

    card_score = 2 ** score_mod
    # cheeky: 2 ^ -1 = 0.5 so can round that down to 0
    total_score += int(card_score)
    
print(total_score)