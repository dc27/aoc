file = 'input.txt'

lines = [line.strip() for line in open(file, 'r')]

bounds = [0, 0, len(lines[0]), len(lines)]

number_is_legal = False
current_number = ''
numbers = []
same_number = False

for line_no, line in enumerate(lines):
    
    for pos, char in enumerate(line):
        if char.isdigit():
            same_number = True
            current_number += char

            # lookaround
            for x_mod in [-1, 0, 1]:
                for y_mod in [-1, 0, 1]:
                    y_ = line_no + y_mod
                    x_ = pos + x_mod
                    
                    if (bounds[0] <= y_ < bounds[3]) & (bounds[1] <= (x_) < bounds[2]):
                        if (lines[y_][x_] != '.') and not (lines[y_][x_].isdigit()):
                            number_is_legal = True
                            break

        else:
            # add number if legal and reset
            if same_number & number_is_legal:
                numbers.append(int(current_number))
            same_number = False
            current_number = ''
            number_is_legal = False
            continue


print(sum(numbers))
        



# go through document.
# for each num string lookaround and see if it's legal. 