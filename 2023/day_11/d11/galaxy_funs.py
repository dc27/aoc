
def transpose(grid:list[str]):
    return list(map(list, zip(*grid)))

def expand(grid:list[str]):

    expanded_rows = []
    for line in grid:

        if line.count(".") == len(line):
            expanded_rows.append("A"*len(line))
        else:
            expanded_rows.append(line)

    input_stream_t = transpose(expanded_rows)

    expanded_input_t = []

    for line in input_stream_t:

        if line.count(".") + line.count("A") == len(line):
            expanded_input_t.append(list("A" * len(line)))
        else:
            expanded_input_t.append(line)
    

    return transpose(expanded_input_t)

def search_for_galaxies(eu:list[str], x_size:int)->list[tuple]:

    galaxies = []

    r = 0
    for line in eu:
        if line.count("A") == len(line):
            r += (x_size - 1)
        
        r += 1
        c = 0
        for char in line:
            if char == "#":
                galaxies.append((r,c))
            
            if char == "A":
                c += (x_size - 1)
            
            c += 1

    return galaxies

# create a distance matrix
def determine_distances(galaxies:list[tuple])->dict:

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
    
    return diss_mat


def sum_distances(dissmat: dict)->int:

    res = 0

    for d in dissmat.values():
        res += sum(d)

    return res