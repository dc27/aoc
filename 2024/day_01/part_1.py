file = 'input.txt'
import re

A, B = ([], [])

for line in open(file, 'r'):
    line = line.strip()
    a, b = map(int, re.findall(pattern="\d+", string=line))
    A.append(a)
    B.append(b)

X = [abs(a - b) for a, b in zip(sorted(A), sorted(B))]
print(sum(X))


