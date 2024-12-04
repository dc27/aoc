file = "input.txt"
import re
import math


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
for i in range(X):
  for j in range(Y):
    # →
    if i+3 < X and "".join([GRID[i][j], GRID[i+1][j], GRID[i+2][j], GRID[i+3][j]]) == "XMAS":
      TOTAL += 1
    # ←
    if i-3 >= 0 and "".join([GRID[i][j], GRID[i-1][j], GRID[i-2][j], GRID[i-3][j]]) == "XMAS":
      TOTAL += 1
    # ↓
    if GRID[i][j:j+4] == "XMAS":
      TOTAL += 1
    # ↑
    if j-3 >= 0 and GRID[i][j-3:j+1][::-1] == "XMAS":
      TOTAL += 1
    # ↘
    if i+3 < X and j+3 < Y and "".join([GRID[i][j], GRID[i+1][j+1], GRID[i+2][j+2], GRID[i+3][j+3]]) == "XMAS":
      TOTAL += 1
    # ↖
    if i-3 >= 0 and j-3 >= 0 and "".join([GRID[i][j], GRID[i-1][j-1], GRID[i-2][j-2], GRID[i-3][j-3]]) == "XMAS":
      TOTAL += 1
    # ↗
    if i-3 >= 0  and j+3 < Y and "".join([GRID[i][j], GRID[i-1][j+1], GRID[i-2][j+2], GRID[i-3][j+3]]) == "XMAS":
      TOTAL += 1
    # ↙
    if i+3 < X  and j-3 >= 0 and "".join([GRID[i][j], GRID[i+1][j-1], GRID[i+2][j-2], GRID[i+3][j-3]]) == "XMAS":
      TOTAL += 1


print(TOTAL)
