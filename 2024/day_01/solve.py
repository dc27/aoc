import re
from collections import defaultdict

def parse_input(file:str="input.txt")->tuple[list]:
  A = []
  B = []

  for line in open(file, 'r'):
    line = line.strip()
    a, b = map(int, re.findall(pattern="\d+", string=line))
    A.append(a)
    B.append(b)

  return (A, B)
  
def solve(file:str="input.txt", part=1)->int:
  
   A, B = parse_input(file)

   if part == 1:
      AB_DIFFS = [abs(a - b) for a, b in zip(sorted(A), sorted(B))]
      X = sum(AB_DIFFS)
      return X
   
   if part == 2:
      A_FQ = defaultdict(int)
      B_FQ = defaultdict(int)

      for a, b in zip(A, B):
          A_FQ[a] += 1
          B_FQ[b] += 1

      TOTAL_SCORE = 0

      for a in A_FQ.keys():
          # only need to consider values in both lists
          if a in B_FQ.keys():
              TOTAL_SCORE += A_FQ[a] * a * B_FQ[a]

      return TOTAL_SCORE
   
print(solve("input.txt", 1))
print(solve("input.txt", 2))
            



  