file = "input.txt"

with open(file, "r") as f:
  stonestr = f.readline()
  stones = list(map(int, stonestr.split(" ")))


# stones = [125, 17]

def blink(stones:list[int])->list[int]:

  after_blink = []

  for s in stones:
    
    str_s = str(s)

    if s == 0:
      after_blink.append(s+1)

    elif len(str_s) % 2 == 0:
      l = int(str_s[0:len(str_s) // 2])
      r = int(str_s[len(str_s) // 2 : ])
      after_blink.append(l)
      after_blink.append(r)

    else:
      after_blink.append(s * 2024)

  return after_blink

for i in range(25):
  stones = blink(stones)

print(len(stones))


 
# 1. If the stone is engraved with the number 0, it is replaced by a stone
# engraved with the number 1.
# 2. If the stone is engraved with a number that has an even number of digits,
# it is replaced by two stones. The left half of the digits are engraved on the
# new left stone, and the right half of the digits are engraved on the new right
# stone. (The new numbers don't keep extra leading zeroes: 1000 would become
# stones 10 and 0.)
# 3. If none of the other rules apply, the stone is replaced by a new stone;
# the old stone's number multiplied by 2024 is engraved on the new stone.

