file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

def get_available_routes(grid: list[str], pos: tuple, prev: tuple=None):

    lefties =   ['-', '7', 'J']
    uppies  =   ['|', 'L', 'J']
    righties =  ['-', 'F', 'L']
    belowies =  ['|', 'F', '7']

    r, c = pos
    char = grid[r][c]

    available_routes = []

    # left-able chars: - 7 J
    if char in lefties or char == 'S':
        if (c - 1) >= 0:
            if grid[r][c - 1] in righties:
                available_routes.append((r, c-1))
    
    # up-able chars: | L J
    if char in uppies or char == 'S':
        if (r - 1) >= 0:
            if grid[r-1][c] in belowies:
                available_routes.append((r-1, c))

    # right-able chars: - L F    
    if char in righties or char == 'S':
        if (c + 1) < len(grid[0]):
            if grid[r][c+1] in lefties:
                available_routes.append((r, c+1))    

    # down-able chars: | F 7
    if char in belowies or char == 'S':
        if (r + 1) < len(grid):
            if grid[r+1][c] in uppies:
                available_routes.append((r+1, c))

    if prev is not None:
        # when the previous is S the length will be 1.
        if len(available_routes) > 1:
            available_routes.remove(prev)
        return available_routes[0]

    return available_routes

# get start position
for r, line in enumerate(input_stream):
    if 'S' in line:
        c = line.find('S')
        available_routes = get_available_routes(input_stream, (r, c))
        assert len(available_routes) == 2
        break

current_A = current_B = (r,c)
next_A, next_B = available_routes

met = False
steps = 1
while not met:
    # update previous positions for each path
    prev_A = current_A
    current_A = next_A
    next_A = get_available_routes(input_stream, current_A, prev=prev_A)
    
    prev_B = current_B
    current_B = next_B
    next_B = get_available_routes(input_stream, current_B, prev=prev_B)

    steps += 1
    met = next_A == next_B

print(steps)

# find S
# determine routes A and B
# keep traversing the loop in routes A and B until they reach the same spot
# the number of steps taken is ans. 


