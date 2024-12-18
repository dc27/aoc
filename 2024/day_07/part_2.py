import re
from itertools import product
from math import prod
file = "input.txt"

# 1. parse input

lines = list()

for x, line in enumerate(open(file, 'r')):
  line = line.strip()
  (r, *el) = map(int, re.findall(r"\d+", line))
  lines.append((r, el))

def build_string(a:list, b:product)->list[str]:
    return [
        "".join(str(a[i]) + op for i, op in enumerate(ops)) + str(a[-1])
        for ops in b
    ]

# 2. solve

TOTAL = 0

for goal, el in lines:
  # print(goal, el)
  
  potential_operators = product("+*±", repeat=len(el)-1)
  mstring = build_string(el, potential_operators)
  for ms in mstring:
    l, r = (["a"], ["b"])
    # evaluate expression 
    while r != []:      
      # split into left and right (49+65+99+100) -> '49+65' ['+99+100']
      
      (l, *r) = list(filter(None, re.split(r"(^\d+[*+±]\d+)", ms, maxsplit=2)))
      # then do whatever's on the left
      
      if "*" in l:
        result = prod(map(int, re.findall(r"\d+", l)))
      elif "+" in l:
        result = sum(map(int, re.findall(r"\d+", l)))
      else:
        result = int("".join(re.findall(r"\d+", l)))

      # recombine with whatever's on the right if there's anything there
      if r == []:
        next
      else:
        ms = str(result) + r[0]

      # early breakout if goal unreachable
      if result > goal:
        break

    if result == goal:
      # goal was achievable
      TOTAL += goal
      # no need to check the other possibilities
      break

print(TOTAL)
# notes: very slow
# TODO:: rewrite with recursion?