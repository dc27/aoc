from itertools import zip_longest

file = "input.txt"

# 1. parse input
for line in open(file, "r"):
  disk_dense = line.strip()
  disk = list(map(int, list(disk_dense)))


files = disk[::2]
spaces = disk[1::2]


files = [(i, f) for i, f in enumerate(files)]

# [(filenumber, filesize)]

# init copy to lookup original positions
files_og = files.copy()

# work backward through the list of files
for fi in range(len(files)-1, -1, -1):
  
  # get the up-to-date location of next file
  F = files_og[fi]
  floc = files.index(F)
  # popped file gets placed back in the list,
  # either in the place it came from or where there's a space
  files.pop(floc)

  # try each space in order to see if it fits
  for si in range(len(spaces)):

    # if we get to the file location, there's not a space
    if si == floc:
      files.insert(floc, F)
      break
  
    # if there's space:
    if F[1] <= spaces[si]:
      
      # fill space with filesize (reduce space)
      spaces[si] -= F[1]

      # collapse surrounding spaces
      if fi < len(spaces):
        spaces[floc-1] += F[1] + spaces.pop(floc)
      else:
        spaces[floc-1] += F[1]
      
      # actually move the file
      files.insert(si+1, F)
      spaces.insert(si, 0)
      break
      

# reconstruct the list with files and spaces
disk_efficient = []

for f, s in zip_longest(files, spaces):
  disk_efficient.append(f)
  disk_efficient.append((0, s))

disk_flat = []

for entity in disk_efficient:
  entity_expanded = [entity[0]] * entity[1]
  disk_flat.extend(entity_expanded)

checksum = sum([x * i for i, x in enumerate(disk_flat)])
print(checksum)
