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
  print(goal, el)
  print("------------------------------")
  potential_operators = product("+*", repeat=len(el)-1)
  mstring = build_string(el, potential_operators)
  for ms in mstring:
    l, r = (["a"], ["b"])
    while r != []:
      # print(ms)
      (l, *r) = list(filter(None, re.split(r"(^\d+[*+]\d+)", ms, maxsplit=2)))
      # print(l, r)
      if "*" in l:
        result = prod(map(int, re.findall(r'\d+', l)))
      else:
        result = sum(map(int, re.findall(r'\d+', l)))

      if r == []:
        next
      else:
        ms = str(result) + r[0]

      if result > goal:
        break

    if result == goal:
      # goal was achievable
      TOTAL += goal
      break

print(TOTAL)
     
     
     



exit()    



# (190, [10, 19])
10 + 19
10 * 19

# (3267, [81, 40, 27])

81 + 40 + 27
81 + 40 * 27
81 * 40 + 27
81 * 40 * 27

# (83, [17, 5])


# (156, [15, 6])
# (7290, [6, 8, 6, 15])
# (161011, [16, 10, 13])
# (192, [17, 8, 14])
# (21037, [9, 7, 18, 13])

9 + 7 + 18 + 13
9 + 7 + 18 * 13
9 + 7 * 18 + 13
9 + 7 * 18 * 13
9 * 7 + 18 + 13
9 * 7 + 18 * 13
9 * 7 * 18 + 13
9 * 7 * 18 * 13



# (292, [11, 6, 16, 20])