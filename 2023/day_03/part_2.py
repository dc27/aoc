import math

# 0. setup
file = 'input.txt'

lines = [line.strip() for line in open(file, 'r')]

# it's good to have boundaries
bounds = [0, 0, len(lines[0]), len(lines)]

# initial settings 
number_is_starry = False
current_number = ''
same_number = False
starry_numbers = dict()

# get loopy, key track of position in doc (line_no) and line (pos)
for line_no, line in enumerate(lines):
    
    for pos, char in enumerate(line):
        if char.isdigit():
            same_number = True
            current_number += char

            # lookaround (for stars)
            for x_mod in [-1, 0, 1]:
                for y_mod in [-1, 0, 1]:
                    y_ = line_no + y_mod
                    x_ = pos + x_mod
                    
                    # boundaries prevent key errors
                    if (bounds[0] <= y_ < bounds[3]) & (bounds[1] <= (x_) < bounds[2]):
                        if (lines[y_][x_] == '*'):
                            # grab the star's position
                            star_pos = (y_, x_)
                            number_is_starry = True
                            break

        else:
            # add number if legal and reset
            if same_number & number_is_starry:
                if star_pos in starry_numbers.keys():
                    starry_numbers[star_pos].append(int(current_number))
                else: 
                    starry_numbers[star_pos] = [int(current_number)]
            same_number = False
            current_number = ''
            number_is_starry = False
            continue


# 2. calculate gear ratios
# start cumsum
sum_of_gear_ratios = 0

for v in starry_numbers.values():
    if len(v) > 1:
        gear_ratio = math.prod(v)
        sum_of_gear_ratios += gear_ratio

print(sum_of_gear_ratios)