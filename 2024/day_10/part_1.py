from collections import defaultdict

file = "input.txt"

GRID = []

# 1. parse input
for line in open(file, "r"):
  GRID.append(list(map(int, line.strip())))
  
X = len(GRID[0]) # left-right
Y = len(GRID) # up-down

zeroes = []

for j, y in enumerate(GRID):
  for i, x in enumerate(y):
    if GRID[j][i] == 0:
      # (y, x)
      zeroes.append((j, i))


# [+1, 0] (below)
# [-1, 0] (above)
# [0, +1] (to the right)
# [0, -1] (to the left)

trails = defaultdict(set)

for zero_position in zeroes:

  end_reached = False
  queue = [zero_position]

  # I think this is an example of Lee's algorithm
  # until reaching the end, set next nodes to 1+ whatever the current pos is,
  # for each of the next noeds set the next next nodes to 1+ whatever the current pos is ...

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
                      trails[zero_position].add(d)

                    else:
                    # if unvisited
                      # add next nodes to queue for next time
                      new = d[0], d[1]
                      if new not in queue:
                        queue.insert(0, new)
                  

TOTAL_SCORE = 0

for start, ends in trails.items():
   print(start, len(ends))
   TOTAL_SCORE += len(ends)

print(TOTAL_SCORE)



