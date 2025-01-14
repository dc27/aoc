import functools
from collections import Counter


file = "input.txt"


with open(file, "r") as f:
  stonestr = f.readline()
  stones = list(map(int, stonestr.split(" ")))


# stones = [125, 17]

@functools.cache
def times2024(x:int)->int:
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
        stones[times2024(engraving)] += count


    return stones



 
# 1. If the stone is engraved with the number 0, it is replaced by a stone
# engraved with the number 1.
# 2. If the stone is engraved with a number that has an even number of digits,
# it is replaced by two stones. The left half of the digits are engraved on the
# new left stone, and the right half of the digits are engraved on the new right
# stone. (The new numbers don't keep extra leading zeroes: 1000 would become
# stones 10 and 0.)
# 3. If none of the other rules apply, the stone is replaced by a new stone;
# the old stone's number multiplied by 2024 is engraved on the new stone.



# 0 -> 1

# >= 1 

# n_digits = even: split
# n_didgits = odd: multiply by 2024


# 0 --> 1
# 1 --> 2024
# 2024 --> 20, 24
# 20 --> 2, 0
# 24 --> 2, 4

# 2 --> 4048
# 4 --> 8096
# 4048 --> 40, 48
# 8096 --> 80, 96

# 40 --> 4, 0
# 48 --> 4, 8
# 8 --> 16192

# 80 --> 8, 0
# 96 --> 9, 6
# 9 --> 18216
# 6 --> 12144


stones = Counter(stones)

for i in range(75):
  stones = blink(stones)

print(sum(stones.values()))
    


