file = 'input.txt'
import re
from collections import defaultdict

A, B = ([], [])

for line in open(file, 'r'):
    line = line.strip()
    a, b = map(int, re.findall(pattern="\d+", string=line))
    A.append(a)
    B.append(b)

AF = defaultdict(int)
BF = defaultdict(int)

for a, b in zip(A, B):
    AF[a] += 1
    BF[b] += 1

TOTAL_SCORE = 0

for a in AF.keys():
    if a in BF.keys():
        TOTAL_SCORE += AF[a] * a * BF[a]




print(TOTAL_SCORE)



