import re
import math

def parse_input(file:str="input.txt")->list[list]:

  GRID = []

  for line in open(file, 'r'):
    line = line.strip()
    GRID.append(line)

  return GRID

def solve(file:str="input.txt", part=1)->int:
  """
  Day 4 Solution
  1. parse input into navigable grid
  2. depending on part check each direction axis (horizontal, vertical, negative diagonal, positive diagonal)
     for XMAS
  """

  GRID = parse_input(file=file)
  TOTAL = 0

  # grid boundaries 
  X = len(GRID[0])
  Y = len(GRID)

  # scan through every GRID[x][y]
  # check each direction for XMAS or SAMX
  for i in range(0, X):
    for j in range(0, Y):
      # P1
      if part == 1:
        if i+3 < X \
          and "".join([GRID[i][j], GRID[i+1][j], GRID[i+2][j], GRID[i+3][j]]) in ["XMAS", "SAMX"]:
          TOTAL += 1
        if GRID[i][j:j+4] in ["XMAS", "SAMX"]:
          TOTAL += 1
        if i+3 < X and j+3 < Y \
          and "".join([GRID[i][j], GRID[i+1][j+1], GRID[i+2][j+2], GRID[i+3][j+3]]) in ["XMAS", "SAMX"]:
          TOTAL += 1
        if i-3 >= 0 and j+3 < Y \
          and "".join([GRID[i][j], GRID[i-1][j+1], GRID[i-2][j+2], GRID[i-3][j+3]]) in ["XMAS", "SAMX"]:
          TOTAL += 1
      # P2
      if part == 2:
        # hunt for A then check diagonals. A on a zero row wouldn't have 4 diagonals
        if i == 0 or j == 0:
          continue
        if GRID[i][j] == "A":
          # loops started at 1 so only need to check XY edge
          if i+1 < X and j+1 < Y \
            and "".join([GRID[i-1][j-1], "A", GRID[i+1][j+1]]) in ["SAM", "MAS"] \
            and "".join([GRID[i+1][j-1], "A", GRID[i-1][j+1]]) in ["SAM", "MAS"]:
            TOTAL += 1


  return TOTAL


print(solve("input.txt", part=1))
print(solve("input.txt", part=2))
