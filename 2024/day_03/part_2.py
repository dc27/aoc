file = 'input.txt'
import re
import math


TOTAL = 0
DO = True
INSTRUCTION_STREAM = []

for line in open(file, 'r'):
  line = line.strip()
  instructions = re.findall(r"(mul\(\d+,\d+\)|(?:do(?:n't)*))", line)
  INSTRUCTION_STREAM.extend(instructions)


for instruction in INSTRUCTION_STREAM:
  if instruction == "do":
    DO = True
  if instruction == "don't":
    DO = False
  if instruction.startswith("mul") and DO == True:
      X = math.prod(map(int, re.findall("\d+", instruction)))
      TOTAL += X

print(TOTAL)
