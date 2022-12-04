file = 'input.txt'

def get_common_character(x):
    return(list(set(x[0]) & set(x[1]) & set(x[2]))[0])

inp = [line.strip() for line in open(file)]

letters = 'abcdefghijklmnopqrstuvwxyz'
LETTERS = letters.upper()

values = letters + LETTERS

CUM_PROP_SUM = 0

elf_groups = {}
elf_group = 0

for i in range(len(inp)):
    if i % 3 == 0:
        elf_group += 1
        elf_groups[elf_group] = [inp[i]]
    else:
        elf_groups[elf_group].append(inp[i])

for eg in elf_groups:
    common_char = get_common_character(elf_groups[eg])
    value = values.index(common_char) + 1
    CUM_PROP_SUM += value

print(CUM_PROP_SUM)

