file = 'input.txt'

import re

numchars = [str(x) for x in list(range(0, 10))]
spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# create dictionary lookup to convert text numbers into their digit character
spelled_lookup = dict(zip(spelled_numbers, numchars[1:]))
numchars.extend(spelled_numbers)

re_numchars = '|'.join(numchars)

# find overlapping matches (...oneight... should return [one, eight] not simply [one])
regexp = f'(?=({re_numchars}))'


def use_lookup(match: str) ->str:

    if match not in spelled_numbers:
        # no need to lookup
        return match
    
    return spelled_lookup[match]

# init total
sum_of_callibration_values = 0

for line in open(file, 'r'):
    line = line.strip()
    # find matches
    matches = re.findall(regexp, line)
    # use lookup
    digits = list(map(use_lookup, [matches[0], matches[-1]]))
    # concatenate digits to number and convert type
    number = int(digits[0] + digits[1])
    sum_of_callibration_values += number

print(sum_of_callibration_values)