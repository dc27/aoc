from collections import Counter
import functools

def parse_input(file:str="test.txt")->list[int]:
  """
  Parses the input into a navigable data structure

  Returns stones list of integer engraving values
  """
  with open(file, "r") as f:
    stonestr = f.readline()
    stones = list(map(int, stonestr.split(" ")))

  return stones

@functools.cache
def multiply_by_2024(x:int)->int:
  return x * 2024

def blink(stones:Counter)->list[int]:
    
    stones_in = stones.copy()

    for engraving, count in stones_in.items():
    
      if count == 0: continue

      str_engraving = str(engraving)

      stones[engraving] -= count

      if engraving == 0:
        stones[1] += count

      elif len(str_engraving) % 2 == 0:
        stones[int(str_engraving[0:len(str_engraving) // 2])] += count
        stones[int(str_engraving[len(str_engraving) // 2 : ])] += count
        
      else:
        stones[multiply_by_2024(engraving)] += count


    return stones

# Solve the problem
def solve(file:str="test.txt", part_2:bool=False)->int:

  stones = parse_input(file)
  stones = Counter(stones)

  if part_2:
    n_iterations = 75 
  else:
    n_iterations = 25

  for _ in range(n_iterations):
    stones = blink(stones)

  return sum(stones.values())

print(solve("input.txt"))
print(solve("input.txt", part_2=True)) 