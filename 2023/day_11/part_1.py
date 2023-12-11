file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

# ----- galaxy expansion ----- 
def transpose(grid:list[str]):
    return list(map(list, zip(*grid)))

def expand(grid:list[str]):

    expanded_rows = []
    for line in grid:

        if line.count(".") == len(line):
            expanded_rows.append(line)
        
        expanded_rows.append(line)

    input_stream_t = transpose(expanded_rows)

    expanded_input_t = []

    for line in input_stream_t:

        if line.count(".") == len(line):
            expanded_input_t.append(line)
        
        expanded_input_t.append(line)
    

    return transpose(expanded_input_t)

universe = expand(input_stream)

galaxies = []

for r, line in enumerate(universe):
    for c, char in enumerate(line):
        if char == "#":
            galaxies.append((r,c))

diss_mat = {}

while len(galaxies) > 1:
    galaxy_of_interest = galaxies.pop(0)
    distances = []
    gi, gj = galaxy_of_interest
    for galaxy in galaxies:
        hi, hj = galaxy
        di = abs(hi - gi)
        dj = abs(hj - gj)
        distances.append(di + dj)
        
    diss_mat[galaxy_of_interest] = distances
        

TOTAL_DISTANCE = 0
for g, d in diss_mat.items():
    TOTAL_DISTANCE += sum(d)

print(TOTAL_DISTANCE)

