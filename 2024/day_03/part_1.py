file = 'input.txt'
import re
import math


TOTAL = 0

for line in open(file, 'r'):
  line = line.strip()
  instructions = re.findall(r"mul\(\d+,\d+\)", line)
  X = [math.prod(list(map(int, re.findall("\d+", instr)))) for instr in instructions]
  TOTAL += sum(X)

print(TOTAL)
