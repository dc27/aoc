import re
from collections import defaultdict
file = "input.txt"

# 1. parse input

GRID = []
nodes = defaultdict(list)

for j, line in enumerate(open(file, "r")):
  line = line.strip()
  GRID.append(list(line))
  nodelocations = re.finditer(r"[^.]", line)
  for l in nodelocations:
    nodes[l.group()].append((l.start(), j))


X = len(GRID[0])
Y = len(GRID)

# count the nodetypes, only types with at least 2 nodes matter

anodes = set()

for k, v in nodes.items():
  
  for _ in range(len(v)):
    current = v.pop(0)
  
    for opp_node in v:
      
      dx = opp_node[0] - current[0]
      dy = opp_node[1] - current[1]
      anode_1 = (current[0] - dx, current[1] - dy)
      anode_2 = (opp_node[0] + dx, opp_node[1] + dy)
      if (0 <= anode_1[0] < X) and (0 <= anode_1[1] < Y):
        anodes.add(anode_1)
      if (0 <= anode_2[0]  < X) and (0 <= anode_2[1] < Y):
        anodes.add(anode_2)


# 2. 

print(len(list(anodes)))

for a in anodes:
  GRID[a[1]][a[0]] = "#"


# for j in range(Y):
#   print("".join(GRID[j]))


# (4, 3) | (5, 5)

# dx = 5 - 4 = 1
# dy = 5 - 3 = 2

# (3, 1), (6, 7)
