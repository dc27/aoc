file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

def transpose(grid:list[str]):
    flipped = list(map(list, zip(*grid)))
    unlist_lines = ["".join([x for x in line]) for line in flipped]
    return unlist_lines

def tilt(grid:list[str], direction:str="N"):
    if direction == "N":
        grid = transpose(grid)
        
        grid = [
            "#".join(
                ["".join(sorted(hsh.replace(".", "a"))).replace("a", ".") for hsh in line.split("#")]
            )
                for line in grid 
            ]
        
        grid = transpose(grid)

    return grid
    
grid = tilt(input_stream)


total_load = 0
for r, line in enumerate(grid):
    load = line.count("O") * (len(grid) - r)
    # print(line, load)
    total_load += load

print(total_load)