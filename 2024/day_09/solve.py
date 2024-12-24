import re
from collections import defaultdict

def parse_input(file:str="test.txt")->list[list]:
  """
  Parses the input into a navigable data structure

  Returns (GRID (lists of lists), nodes (defaultdict of lists))
  """
  GRID = []
  nodes = defaultdict(list)

  for j, line in enumerate(open(file, 'r')):
      line = line.strip()
      GRID.append(list(line)) # list to be able to easily replace chars with # for debugging
      nodelocations = re.finditer(r"[^.]", line)
      for l in nodelocations:
         nodes[l.group()].append((l.start(), j))

  return (GRID, nodes)
    
# Solve the problem
def solve(file:str="test.txt", part:int=1)->int:

  GRID, nodes =  parse_input(file)

  X = len(GRID[0])
  Y = len(GRID)

  ANTINODES = set()

  for ntype, nlocs in nodes.items():
     for _ in range(len(nlocs)):
        current = nlocs.pop(0)

        for pair in nlocs:
          # in part 2 all nodes are ANTINODES
          if part == 2:
            ANTINODES.add(current)
            ANTINODES.add(pair)
          
          dx = pair[0] - current[0]
          dy = pair[1] - current[1]
        
          # 1. moving from current
          m = 1

          while True:
            anode = (current[0] - m * dx, current[1] - m * dy)
            if (0 <= anode[0] < X) and (0 <= anode[1] < Y):
              ANTINODES.add(anode)
              if part == 2:
                m+=1
              else:
                # part 1 only needs 'adjacent' antinodes (+/-) 1 * dx or dy
                break
            else:
              # not in grid, stop
              break
          
          # 2. moving from pair
          m = 1

          while True:
            anode = (pair[0] + m * dx, pair[1] + m * dy)
            if (0 <= anode[0] < X) and (0 <= anode[1] < Y):
              ANTINODES.add(anode)
              if part == 2:
                m+=1
              else:
                break
            else:
              # not in grid, stop
              break

          


  return len(list(ANTINODES))

print(solve("input.txt", part=1))
print(solve("input.txt", part=2)) 