file = 'input.txt'

def extract_first_num(line: str) ->str:
    """extracts the first number in a string. Returns a string"""

    numchars = [str(x) for x in list(range(0, 10))]
    numchars.extend()

    for char in line:
        if char in numchars:
            return char

def extract_last_num(line: str) ->str:
    line_rev = line[::-1]
    return extract_first_num(line_rev)

sum_of_callibration_values = 0

for line in open(file, 'r'):
    line = line.strip()
    first_digit = extract_first_num(line)
    last_digit = extract_last_num(line)
    sum_of_callibration_values += int(first_digit + last_digit)

print(sum_of_callibration_values)


