import re

def parse_input(file:str="input.txt")->tuple[list]:

  N = []

  for line in open(file, 'r'):
      line = line.strip()
      n = list(map(int, re.findall("\d+", line)))
      N.append(n)

  return N
  
def solve(file:str="input.txt", part=1)->int:
  """
  Day 2 Solution
  p1
  1. create list of diffs for each line in input
  2. check if list of diffs is within any valid range -> both ranges mean that 
     list is always increasing or decreasing so no need to test for that too

  p2
  1. create temp copy of input line
  2. try removing each number in input
  3. do the same check as p1 and break out of miniloop if a SAFE result is found 
  """
  
  N = parse_input(file=file)

  SAFE = 0

  ranges = [[1, 3], [-3, -1]]

  for n in N:
      if part == 1: 
        diffs = [n[i+1] - n[i] for i in range(len(n)-1)]
      
        if any([min(diffs) >= r[0] and max(diffs) <= r[1] for r in ranges]):
          SAFE += 1

      if part == 2:
        for i, _ in enumerate(n):
          c = n.copy()
          c.pop(i)
          diffs = [c[i+1] - c[i] for i in range(len(c)-1)]
          
          if any([min(diffs) >= r[0] and max(diffs) <= r[1] for r in ranges]):
              SAFE += 1
              break


  return SAFE
   
print(solve("input.txt", 1))
print(solve("input.txt", 2))
            



  