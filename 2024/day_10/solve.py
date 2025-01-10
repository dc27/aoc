from collections import defaultdict

def parse_input(file:str="test.txt")->list[list]:
  """
  Parses the input into a navigable data structure

  Returns GRID (lists of lists of ints)
  """
  GRID = []

  # 1. parse input
  for line in open(file, "r"):
    GRID.append(list(map(int, line.strip())))

  return GRID
    
# Solve the problem
def solve(file:str="test.txt", part:int=1)->int:

  GRID =  parse_input(file)


  X = len(GRID[0]) # left-right
  Y = len(GRID) # up-down

  zeroes = []

  for j, y in enumerate(GRID):
    for i, x in enumerate(y):
      if GRID[j][i] == 0:
        # (y, x)
        zeroes.append((j, i))

  if part == 1:
     trails = defaultdict(set)
  elif part == 2:
    trails = defaultdict(int)
  else:
     raise ValueError("part must be 1 or 2")

  for zero_position in zeroes:

    end_reached = False
    queue = [zero_position]

    while end_reached == False:

        if len(queue) == 0:
          end_reached = True
          break

        for _ in range(len(queue)):
            
            # each direction
            position = queue.pop()
            a = position[0] -1, position[1]
            l = position[0], position[1] - 1
            b = position[0] + 1, position[1]
            r = position[0], position[1] + 1
            
            
            for d in [a, l, b, r]:
                # make sure we can actually go there (within bounds of 2darray)
                if (0 <= d[0] < (Y)) & (0 <= d[1] < (X)):
                    if GRID[d[0]][d[1]] == GRID[position[0]][position[1]] + 1:
                      # end condition
                      if (GRID[d[0]][d[1]] == 9):
                        if part == 1:
                          trails[zero_position].add(d)
                        else:
                          trails[zero_position] += 1

                      else:
                        # add next nodes to queue for next time
                        queue.insert(0, d)
                    

  if part == 1:
     return sum([len(ends) for ends in trails.values()])
  else:
     return  sum(trails.values())

print(solve("input.txt", part=1))
print(solve("input.txt", part=2)) 