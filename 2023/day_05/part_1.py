import re
from collections import OrderedDict
file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

# 1. parse input into seeds and maps
# 1.1. seeds
# seeds are the first line
seedstring = input_stream[0].removeprefix('seeds: ')
seeds = re.findall(r'\d+', seedstring)

seedflows = []

for s in seeds:
    seedflow = OrderedDict(seed = int(s))
    seedflows.append(seedflow)

# init map blocks
block = {}
block['mappings'] = []
blocks = []

# 1.2. create map blocks from rest input stream 
# start at 2th row to skip the space
for i, line in enumerate(input_stream[2:]):
    # empty lines after each block (end point) (or end of file)
    if (line == '') or (i == len(input_stream[2:])-1):
        blocks.append(block)
        block = {}
        block['mappings'] = []
        continue

    if line.endswith('map:'):
        title = line.removesuffix(' map:')
        block["title"] = title
    else:
        dest, start, r = list(map(int, re.findall(r'\d+', line)))
        block["mappings"].append(dict(dest = dest, start = start, r = r))


def map_seeds(seed:int, mappings:dict):

    for mapping in mappings:

        lower = mapping["start"]
        higher = mapping["start"] + mapping["r"] - 1
        change = mapping["dest"] - mapping["start"]
    
        if lower <= seed <= higher:
            return(seed + change)
        
    return(seed)
    

# perform the mapping
for flow in seedflows:
    for block in blocks:
        # where was the seed last (value)?
        _, seed = next(reversed(flow.items()))

        # where is the next location (title)?
        new_location = block["title"].split("-to-")[-1]
        new_value = map_seeds(seed, block["mappings"])
        # update OD
        flow[new_location] = new_value


# get answer by looking at dict (last item added relates to final positions after all map steps)
last_locations = [next(reversed(flow.items()))[1] for flow in seedflows]

print(min(last_locations))



