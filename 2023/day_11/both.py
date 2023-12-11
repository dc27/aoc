from d11.galaxy_funs import expand, search_for_galaxies, determine_distances, sum_distances

file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

universe = expand(input_stream)

p1_galaxies = search_for_galaxies(universe, 2)
p2_galaxies = search_for_galaxies(universe, 1_000_000)

parts = {
    "1" : p1_galaxies,
    "2" : p2_galaxies
}

for p, g in parts.items():
    diss_mat = determine_distances(g)
    total_distance = sum_distances(diss_mat)
    print(f"Part {p}: {total_distance}")
