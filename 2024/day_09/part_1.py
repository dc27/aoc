file = "input.txt"

# 1. parse input
for line in open(file, "r"):
  disk_dense = line.strip()
  disk = list(map(int, list(disk_dense)))

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

