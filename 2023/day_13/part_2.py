file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

def parse_input(input_stream:list[str])->list[list[str]]:

    blocks = []
    block = []

    for line in input_stream:
        if line == "":
            blocks.append(block)
            block = []
            continue
        else:
            block.append(line)

    blocks.append(block)
    return blocks
    
blocks = parse_input(input_stream)

def transpose(grid:list[str]):
    return list(map(list, zip(*grid)))

def find_mirror(block:list[str])->int:

    for i, line in enumerate(block[1:]):
        if line == block[i]:
            # there might be a reflection ...
            # keep going forwards and backwards
            forward = i + 1
            backward = i
            while (backward >= 0 and forward <= (len(block)-1)):
                
                # check to see if they no longer reflect
                if block[backward] != block[forward]:
                    break
                backward -= 1
                forward += 1
            # they continued to reflect. it was a mirror!
            else: return i+1
    
    return None


def fix_smudge(block:list[str])->list[str]:
    
    return block



reflection_summary = 0

for block in blocks:

    # 2. find mirror
    is_vertical_mirror = False
    mirror_location = find_mirror(block)

    if mirror_location is None:
        mirror_location = find_mirror(transpose(block))
        is_vertical_mirror = True

    if not is_vertical_mirror:
        mirror_location *= 100

    reflection_summary += mirror_location

print(reflection_summary)








