import re
from collections import OrderedDict
file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

# 1. parse input into seeds and maps
# 1.1. seeds
# seeds are the first line
seedstring = input_stream[0].removeprefix('seeds: ')
seedrangestrings = re.findall(r'\d+ \d+', seedstring)

seedranges = [tuple(map(int, srs.split())) for srs in seedrangestrings]

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


def map_seeds(seedrange:tuple, mapping:dict)->list:
    """
    Mapping function. Takes in two ranges (one of seeds, one of mappings), determines the nature of overlap.

    For a part of the seed range overlaps with the mapping range then the new mapping is applied.
    For any part of the seed range which falls outside the mapping range then the seedrange is returned.
    The function returns a two-item list where the first item is mapped overlapping seed range.
    The second item is the any unmapped seed range.
    """

    # 0. parse into top and bottom of each range
    # 0.1 mappings
    m_lower = mapping["start"]
    m_higher = mapping["start"] + mapping["r"] - 1
    m_change = mapping["dest"] - mapping["start"]

    # 0.2 seed ranges
    s_lower = seedrange[0]
    s_higher = seedrange[0] + seedrange[1] - 1

    # 1. no overlap
    if s_higher < m_lower or s_lower > m_higher:
        return [None, seedrange]

    # 2. they're both within the interval (complete overlap):
    if s_lower >= m_lower and s_higher <= m_higher:
        new_lower = s_lower + m_change
        mapped = (new_lower, seedrange[1])
        return [mapped,  None]
    
    # 3. overlap with two hangovers
    # lowest < lowest and highest > highest
    if s_lower < m_lower and s_higher > m_higher:
        # split seeds into three
        below = (s_lower, m_lower - 1 - s_lower + 1)
        above = (m_higher + 1, s_higher - m_higher + 1)
        within = (m_lower + m_change, mapping["r"])
        return [within, [below, above]]

    # 4. single overlap (by process of elimination)
    # 4.1 exceeds below map range
    if s_lower < m_lower:
        below = (s_lower, m_lower - 1 - s_lower + 1)
        within = (m_lower + m_change, s_higher - m_lower + 1)
        return [within, below]
    # 4.2 exceeds above map range
    elif s_higher > m_higher:
        above = (m_higher + 1, s_higher - m_higher + 1)
        within = (s_lower + m_change, m_higher - s_lower + 1)
        return [within, above]

# keep mapping until all seeds have been mapped OR all seeds have been found mapless
# all seeds start off unmapped
# for each map, put each collection of unmapped seeds through
# keep hold of the 'unmapped' seeds


for block in blocks:

    n_maps = len(block["mappings"])
    still_to_map = seedranges
    maps_exhausted = False
    mapped = []
    counter = 0
    print(f"Attempting block:{block['title']}")
    print("-"*80)

    while still_to_map != [] and not maps_exhausted:
        
        mapping = block["mappings"][counter]
        # try to map remaining seedranges
        map_attempts = [map_seeds(sr, mapping) for sr in still_to_map]
        unmapped = [a[1] for a in map_attempts if a[1] is not None]
        # disgusting ... one of the ways the ranges can overlap results in a list of lists output.
        # needs to be unnested (if it's a list, NOT if it's a tuple)
        nested = [sr for sublist in unmapped if isinstance(sublist, list) for sr in sublist]
        flat_part = [sr for sr in unmapped if not isinstance(sr, list)]
        unmapped_flattened = nested + flat_part
        mappedt = [a[0] for a in map_attempts if a[0] is not None]

        still_to_map = unmapped_flattened
        mapped.extend(mappedt)

        counter +=1
        maps_exhausted = counter >= n_maps
    
    mapped.extend(still_to_map)
    seedranges = mapped[:]

start_points = [r[0] for r in seedranges]
print(min(start_points))


