import re
from collections import OrderedDict
file = 'test.txt'

input_stream = [line.strip() for line in open(file, 'r')]

# 1. parse input into seeds and maps
# 1.1. seeds
# seeds are the first line
seedstring = input_stream[0].removeprefix('seeds: ')
seedrangestrings = re.findall(r'\d+ \d+', seedstring)

def parse_srs(seedrangestr: str)->list:
    return tuple(map(int, seedrangestr.split()))

seedranges = [tuple(map(int, srs.split())) for srs in seedrangestrings]

seedflows = []

# keep track of the seedranges at each level
for s in seedranges:    
    seedflow = OrderedDict(seed = s)
    seedflows.append(seedflow)

print(seedflows)

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


def map_seeds(seed:tuple, mapping:dict)->int:

    m_lower = mapping["start"]
    m_higher = mapping["start"] + mapping["r"] - 1
    m_change = mapping["dest"] - mapping["start"]

    s_lower = seed[0]
    s_higher = seed[0] + seed[1] - 1

    # 1. they're both within the interval (complete overlap):
    if m_lower <= s_lower <= m_higher & m_lower <= s_higher <= m_higher:
        return(1)
    
    # 2. they're

        
        

for block in blocks:
    print(block["title"])
    print(block["mappings"])

quit()

# perform the mapping
for flow in seedflows:
    print("fff")
    for block in blocks:
        print("bbb")
        # where was the seed last (value)?
        _, seed = next(reversed(flow.items()))

        # where is the next location (title)?
        new_location = block["title"].split("-to-")[-1]
        new_value = map_seeds(seed, block["mappings"])
        # update OD
        flow[new_location] = new_value


last_locations = [next(reversed(flow.items()))[1] for flow in seedflows]

print(min(last_locations))

# get answer by looking at dict


