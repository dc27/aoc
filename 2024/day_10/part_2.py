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

trails = defaultdict(int)

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
                      trails[zero_position] += 1

                    else:
                      # add next nodes to queue for next time
                      new = d[0], d[1]
                      queue.insert(0, new)
                  

TOTAL_SCORE = 0

for start, score in trails.items():
   print(start, score)
   TOTAL_SCORE += score

print(TOTAL_SCORE)
