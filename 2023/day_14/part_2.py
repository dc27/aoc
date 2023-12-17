file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

def transpose(grid:list[str]):
    flipped = list(map(list, zip(*grid)))
    unlist_lines = ["".join([x for x in line]) for line in flipped]
    return unlist_lines

def roll_rocks(grid:list[str])->list[str]:
    """
    this beast of a method chain list comprehension goes through each row of grid
    and moves O characters up by replacing . chars with A and sorting for each
    set of chars after a # symbol
    """
    return [
    "#".join(
        ["".join(sorted(hsh.replace(".", "a"))).replace("a", ".") for hsh in line.split("#")]
    )
        for line in grid 
    ]

grid = input_stream.copy()

RANGE_LIM = 1_000_000_000 - 1
store = []
# really hope we don't go for 1B iterations :|
for i in range(RANGE_LIM):
    # N
    grid = transpose(roll_rocks(transpose(grid)))
    # W
    grid = roll_rocks(grid)
    # S
    grid = transpose([line[::-1] for line in roll_rocks(line[::-1] for line in transpose(grid))])
    # E
    grid = [line[::-1] for line in roll_rocks([line[::-1] for line in grid])]
    

    # keep hold of each grid seen after cycle
    if grid not in store:
        store.append(grid)
    # if we've seen it before we've entered a loop. We no longer need to find new grids
    else:
        break


# use the store of grids to find what will be the final grid
# (if we were to perform the cycles for n times in RANGE_LIM)
first_repeat = store.index(grid)

non_repeating_stored = len(store[:first_repeat])
repeating_stored = len(store) - first_repeat

final_grid = store[non_repeating_stored:][((RANGE_LIM - non_repeating_stored) % repeating_stored)]

total_load = 0
for r, line in enumerate(final_grid):
    load = line.count("O") * (len(final_grid) - r)
    total_load += load

print(total_load)