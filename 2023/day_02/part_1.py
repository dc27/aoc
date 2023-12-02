file = 'input.txt'

highest_allowed = {
    'red'  : 12,
    'green' : 13,
    'blue': 14
}

sum_of_possible_ids = 0

for line in open(file, 'r'):
    line = line.strip()
    game_n, info = line.split(': ')
    
    game_n = int(game_n.removeprefix('Game '))

    pulls = info.split('; ')

    # innocent until proven guilty
    legal_game = True

    # loop through each pull in game, then loop through each cube, determine if rules broken by any cube
    for pull in pulls:
        # save some time. Once it's illegal there's no need to check the remaining pulls.
        if legal_game == False:
            break

        cubes = pull.split(', ')
        for cube in cubes:
            n, colour = cube.split(' ')
            if highest_allowed[colour] < int(n):
                legal_game = False
                break

    if legal_game:
        print(f'Game: {game_n}\nPulls: {pulls}')
        sum_of_possible_ids += int(game_n)



print(sum_of_possible_ids)


