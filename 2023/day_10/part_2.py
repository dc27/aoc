import re

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

def replace_with_pipechar(grid:list[str], coords:tuple)->None:
    better_pipe_chars = {
        "-": "\u2550",
        "|": "\u2551",
        "F": "\u2554",
        "7": "\u2557",
        "L": "\u255A",
        "J": "\u255D",
        "S": "\u2554",
        "\u2554": "\u2554"
    }

    r, c = coords
    grid[r] = "".join((grid[r][:c], better_pipe_chars[grid[r][c]], input_stream[r][c+1:]))

    pass

def replace_with_star(grid: list[str], coords: tuple)->None:
    
    r, c = coords
    grid[r] = "".join((grid[r][:c], "*", input_stream[r][c+1:]))

    pass

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

while not met:
    # update previous positions for each path
    replace_with_pipechar(input_stream, current_A)
    prev_A = current_A
    current_A = next_A
    
    next_A = get_available_routes(input_stream, current_A, prev=prev_A)
    
    replace_with_pipechar(input_stream, current_B)
    prev_B = current_B
    current_B = next_B
    next_B = get_available_routes(input_stream, current_B, prev=prev_B)

    met = next_A == next_B


replace_with_pipechar(input_stream, current_A)
replace_with_pipechar(input_stream, current_B)
replace_with_pipechar(input_stream, next_A)

# going through the line, these characters are what indicate boundary crossers
# when encountered this is where inside gets flipped. Not sure why it's the 
# chars that block the 'south' part of the tile.

boundary_chars = ["╔", "║", "╗"]

n_inner_tiles = 0
for r, line in enumerate(input_stream):
    line = re.sub(r'[\-|FJL7.]', r'.', line)
    inside = False
    for c, char in enumerate(line):
        if inside and char == '.':
            n_inner_tiles += 1
            replace_with_star(input_stream, (r, c))

        # if outside, check to see if you're at a boundary -> if so inside
        if char in boundary_chars:
            inside = not inside
        
print(n_inner_tiles)


# part 1:
# find S
# determine routes A and B
# keep traversing the loop in routes A and B until they reach the same spot

# part 2:
# do part 1. don't need to count the steps this time. Rewrite the grid so that
# it has proper chars instead of J's and -'s.
# turn every character that is not proper pipe into .
# go through the new grid
# for each line count the number of points (tiles) within the pipe structure by
# determining if you are currently inside or outside the pipe

