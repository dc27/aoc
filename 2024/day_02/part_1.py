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
    diffs = [n[i+1] - n[i] for i in range(len(n)-1)]
    
    if any([min(diffs) >= r[0] and max(diffs) <= r[1] for r in ranges]):
        SAFE += 1

print(SAFE)
