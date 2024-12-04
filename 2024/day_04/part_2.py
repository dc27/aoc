file = "input.txt"

TOTAL = 0
GRID = []

for line in open(file, 'r'):
  line = line.strip()
  GRID.append(line)

# grid boundaries 
X = len(GRID[0])
Y = len(GRID)

# scan through every GRID[x][y]
# check each direction for XMAS
for i in range(1, X):
  for j in range(1, Y):
    if GRID[i][j] == "A":
      # loops started at 1 so only need to check XY edge
      if i+1 < X and j+1 < Y \
        and "".join([GRID[i-1][j-1], "A", GRID[i+1][j+1]]) in ["SAM", "MAS"] \
        and "".join([GRID[i+1][j-1], "A", GRID[i-1][j+1]]) in ["SAM", "MAS"]:
        TOTAL += 1


print(TOTAL)
