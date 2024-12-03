import re
import math

def parse_input(file:str="input.txt")->list[int]:

  INSTRUCTION_STREAM = []

  for line in open(file, 'r'):
    line = line.strip()
    instructions = re.findall(r"(mul\(\d+,\d+\)|(?:do(?:n't)*))", line)
    INSTRUCTION_STREAM.extend(instructions)

  return INSTRUCTION_STREAM

def solve(file:str="input.txt", part=1)->int:
  """
  Day 3 Solution
  1. parse input into long list of individual instructions (e.g. mul(111, 222))
  2. carry out each instruction and ignore do(n't) instructions if only part 1
  """

  INSTRUCTION_STREAM = parse_input(file=file)

  TOTAL = 0
  DO = True

  for instruction in INSTRUCTION_STREAM:
    if part == 2:
      if instruction == "do":
        DO = True
      if instruction == "don't":
        DO = False
    if instruction.startswith("mul") and DO == True:
        X = math.prod(map(int, re.findall("\d+", instruction)))
        TOTAL += X

  return TOTAL

print(solve("input.txt", part=1))
print(solve("input.txt", part=2))
