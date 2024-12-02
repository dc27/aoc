file = 'input.txt'
import re

N = []

for line in open(file, 'r'):
    line = line.strip()
    n = list(map(int, re.findall("\d+", line)))
    N.append(n)

# 2 checks: 
# all diffsigns are the same:
# all diffs are within a range [1, 3]

SAFE = 0

ranges = [[1, 3], [-3, -1]]

for n in N:
    for i, _ in enumerate(n):
      c = n.copy()
      c.pop(i)
      diffs = [c[i+1] - c[i] for i in range(len(c)-1)]
      
      if any([min(diffs) >= r[0] and max(diffs) <= r[1] for r in ranges]):
          SAFE += 1
          break

print(SAFE)
