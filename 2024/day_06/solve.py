import re
import math
  
def parse_input(file:str="input.txt")->list[list]:

  GRID = []

  for x, line in enumerate(open(file, 'r')):
    line = line.strip()
    if line.find("^") != -1:
      initial_guard_position = (x, line.find("^"))
      line = line.replace("^", "X")
    GRID.append(list(line))

  return (initial_guard_position, GRID)


def solve(file:str="input.txt", part:int=1)->int:

    initial_guard_position, GRID = parse_input(file=file)
  
    # grid boundaries 
    X = len(GRID)
    Y = len(GRID[0])

    new_direction = {
      "UP"    : "RIGHT",
      "RIGHT" : "DOWN",
      "DOWN"  : "LEFT",
      "LEFT"  : "UP" 
    }

    guard_direction = "UP"
    guard_position = initial_guard_position

    while True:
      if guard_direction == "UP":
        potential_nxt = (guard_position[0]-1, guard_position[1])
      if guard_direction == "DOWN":
        potential_nxt = (guard_position[0]+1, guard_position[1])
      if guard_direction == "LEFT":
        potential_nxt = (guard_position[0], guard_position[1]-1)
      if guard_direction == "RIGHT":
        potential_nxt = (guard_position[0], guard_position[1]+1)


      if max(potential_nxt) in (X, Y) or min(potential_nxt) == -1:
        break

      nxt_step = GRID[potential_nxt[0]][potential_nxt[1]]

      if nxt_step == "#":
        guard_direction = new_direction[guard_direction]
      else:
        guard_position = potential_nxt
        GRID[guard_position[0]][guard_position[1]] = "X"

    # guard_sees 
    # look forward and see what the obstacle is
    # go to obstacle
    # update guard direction
      
    # else
    #   change direction and step forward

    nxchars = 0
      
    for i in range(X):
      nxchars += GRID[i].count("X")

    return nxchars


print(solve("input.txt", part=1))
print(solve("input.txt", part=2)) #TODO (optimise)
