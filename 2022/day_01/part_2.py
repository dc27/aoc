file = 'input.txt'

elf = 0
elf_cals = []
new_elf = []

for line in open(file, 'r'):
	if line.strip() == '':
		elf += 1
		elf_cals.append(new_elf)
		new_elf = []
	else:
		new_elf.append(int(line.strip()))

elf_cals.append(new_elf)

elf_sums = list(map(sum, elf_cals))

print(sum(sorted(elf_sums)[-3:]))
