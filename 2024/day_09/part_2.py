file = "test.txt"

# 1. parse input
for line in open(file, "r"):
  disk_dense = line.strip()
  disk = list(map(int, list(disk_dense)))



files = disk[::2]
spaces = disk[1::2]

print(files)
print(spaces)


# starting at the end: 
# for each file in the string:
# .... try to put it in an earlier slot
# .... if you can't
# ........ leave it forever
# .... move it, remove the empty space of that size, the moved file creates empty space


disk_flat = [
    i // 2 if i % 2 == 0 else "."
    for i, entity in enumerate(disk)
    for _ in range(entity)
]

print(disk_flat)


exit()







def defrag_disk(disk):




  files = disk[::2]
  end_point = sum(files)
  files_indices = [i for i in range(len(files))]

  disk_efficient = []
  files_to_add = []

  for i, entity in enumerate(disk):
    
    if i % 2 == 0:
      for _ in range(entity):
        disk_efficient.append(i // 2)
        

        if len(disk_efficient) == end_point:
          return disk_efficient


    else:
      while len(files_to_add) < entity:
        to_add = files.pop()
        file_size_to_add = files_indices.pop()
      
        for n in range(to_add):
          files_to_add.append(file_size_to_add)
        
      for _ in range(entity):
        disk_efficient.append(files_to_add.pop(0))
        

        if len(disk_efficient) == end_point:
          return disk_efficient

          
disk_efficient = defrag_disk(disk)

checksum = sum([x * i for i, x in enumerate(disk_efficient)])

print(checksum)





########    
# earliest spot 99 fits?
# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..

# earliest spot 8888 fits?
# 0099.111...2...333.44.5555.6666.777.8888..
# nowhere...
# 8888 is to be left alone

# earliest spot 777 fits?
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..

# ...earliest spot 6666 fits?
# nowhere
# 6666 is to be left alone
# earliest spot 555 fits?
# nowhere
# 555 is to be left alone

# earliest spot 44 fits?
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..

# earliest spot 333 fits?
# 00992111777.44.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..