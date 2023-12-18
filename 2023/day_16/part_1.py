file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

beams = [((0, 0), "E")]

ew_bounds = (0, len(input_stream[0])-1)
ns_bounds = (0, len(input_stream)-1)

def move_to(
        current_position:tuple, direction_of_travel:str,
        ew_bound:tuple=ew_bounds, ns_bound: tuple=ns_bounds
        )->tuple:

    x, y = current_position

    direction_instructions = {
        "N": (x, y - 1),
        "E": (x + 1, y),
        "S": (x, y + 1),
        "W": (x - 1, y)
    }

    new_location = direction_instructions[direction_of_travel]

    # make sure new location is within grid
    if (
        (new_location[0] < ew_bound[0])
        or (new_location[0] > ew_bound[1])
        or (new_location[1] < ns_bound[0])
        or (new_location[1] > ns_bound[1])
    ):
        return None

    return (new_location, direction_of_travel)

def reorient(grid:list[str], current_position:tuple, direction_of_travel:str)->list[tuple]:

    x, y = current_position
    symbol = grid[y][x]

    if symbol == ".":
        return [(current_position, direction_of_travel)]
    
    if symbol == "\\":
        if direction_of_travel == "N":
            new_direction_of_travel = "W"
        elif direction_of_travel == "S":
            new_direction_of_travel = "E"
        elif direction_of_travel == "W":
            new_direction_of_travel = "N"
        elif direction_of_travel == "E":
            new_direction_of_travel = "S"
    elif symbol == "/":
        if direction_of_travel == "N":
            new_direction_of_travel = "E"
        elif direction_of_travel == "S":
            new_direction_of_travel = "W"
        elif direction_of_travel == "W":
            new_direction_of_travel = "S"
        elif direction_of_travel == "E":
            new_direction_of_travel = "N"
    elif symbol == "-":
        if direction_of_travel in ["E", "W"]:
            return [(current_position, direction_of_travel)]
        else:
            return [(current_position, "E"), (current_position, "W")]
    else:
        if direction_of_travel in ["N", "S"]:
            return [(current_position, direction_of_travel)]
        else:
            return [(current_position, "N"), (current_position, "S")]
        

    return [(current_position, new_direction_of_travel)]

# little safeguard
counter = 0
orientations = beams.copy()
while beams != [] and counter < 100000:
    beams = [b for beam, direction in beams for b in reorient(input_stream, beam, direction)]
    beams = [move_to(beam, direction) for beam, direction in beams]
    beams = [b for b in beams if b is not None]
    beams = [b for b in beams if b not in orientations]
    orientations.extend(beams)
    counter += 1

# number of spaces visited
cells = set([c for c, _ in orientations])
print(len(cells))

