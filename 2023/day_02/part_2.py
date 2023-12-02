import math

file = 'input.txt'

# absolute minimum requirements
min_requirments = {
    'red'  : 0,
    'green' : 0,
    'blue': 0
}

sum_of_power = 0

for line in open(file, 'r'):
    line = line.strip()
    game_n, info = line.split(': ')

    game_n = int(game_n.removeprefix('Game '))
    pulls = info.split('; ')

    # start with the same min requirements each time
    m_reqs = min_requirments.copy()

    for pull in pulls:

        cubes = pull.split(', ')
        for cube in cubes:
            n, colour = cube.split(' ')
            
            if m_reqs[colour] < int(n):
                m_reqs[colour] = int(n)

    power = math.prod(m_reqs.values())
    # print(f'Game: {game_n}\nMin Requirements: {m_reqs}\nPower: {power}')
    sum_of_power += power

print(sum_of_power)


