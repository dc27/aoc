from copy import deepcopy

file = "input.txt"

GRID = []

for x, line in enumerate(open(file, 'r')):
  line = line.strip()
  if line.find("^") != -1:
    initial_guard_position = (x, line.find("^"))
    line = line.replace("^", "X")
  GRID.append(list(line))

# grid boundaries 
X = len(GRID[0])
Y = len(GRID)

new_direction = {
  "UP"    : "RIGHT",
  "RIGHT" : "DOWN",
  "DOWN"  : "LEFT",
  "LEFT"  : "UP" 
}

# 2. get guard path with no added obstacles
G = deepcopy(GRID)

guard_direction = "UP"
guard_position = initial_guard_position

guard_path = []

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

  nxt_step = G[potential_nxt[0]][potential_nxt[1]]

  if nxt_step == "#":
    guard_direction = new_direction[guard_direction]
  else:
    guard_position = potential_nxt
    G[guard_position[0]][guard_position[1]] = "X"
    if guard_position not in guard_path: 
      guard_path.append(guard_position)

loop_scenarios = 0

for x, y in guard_path:
  # initial settings
  # guard facing up, positioned at start
  # movelist is empty, if guard position and direction are ever the same
  # guard is in a loop
  guard_direction = "UP"
  guard_position = initial_guard_position
  movelist = set()
  movelist.add(str(guard_position) + guard_direction)

  # insert obstacle at X, Y
  G = deepcopy(GRID)
  G[x][y] = "#"

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

    nxt_step = G[potential_nxt[0]][potential_nxt[1]]

    if nxt_step == "#":
      guard_direction = new_direction[guard_direction]
    else:
      guard_position = potential_nxt
      G[guard_position[0]][guard_position[1]] = "X"

    guardmove = str(guard_position) + guard_direction
    if guardmove in movelist:
      # guard is repeating path (they are in a loop)
      loop_scenarios += 1
      break
    else:
      movelist.add(guardmove)


print(loop_scenarios)