file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

# ----- galaxy expansion ----- 
def transpose(grid:list[str]):
    return list(map(list, zip(*grid)))

def expand(grid:list[str]):

    expanded_rows = []
    for line in grid:

        if line.count(".") == len(line):
            expanded_rows.append("A"*len(line))
        
        expanded_rows.append(line)

    input_stream_t = transpose(expanded_rows)

    expanded_input_t = []

    for line in input_stream_t:

        if line.count(".") + line.count("A") == len(line):
            expanded_input_t.append(list("A" * len(line)))
        
        expanded_input_t.append(line)
    

    return transpose(expanded_input_t)

universe = expand(input_stream)

# get the positions of all the galaxies
galaxies = []

# manually keep track of how many rows passed
r = 0
for line in universe:
    if line.count("A") == len(line):
        r += 999_999
    else:
        r += 1
    # keep track of c position
    c = 0
    for char in line:
        if char == "#":
            galaxies.append((r,c))

        if char == "A":
            c += 999_999
        else:
            c += 1

# create a distance matrix
diss_mat = {}

# until there's no galaxies left to check
while len(galaxies) > 1:
    # get the distance between the next galaxy and every other galaxy
    galaxy_of_interest = galaxies.pop(0)
    distances = []
    gi, gj = galaxy_of_interest
    for galaxy in galaxies:
        hi, hj = galaxy
        di = abs(hi - gi)
        dj = abs(hj - gj)
        distances.append(di + dj)
        
    diss_mat[galaxy_of_interest] = distances
        

total_distance = 0

# useful to keep g and d for debugging
for g, d in diss_mat.items():
    total_distance += sum(d)

print(total_distance)

