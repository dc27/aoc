import re
file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

def diff(a:int, b:int)->int:
    return b - a


def get_next(seq: list)->int:
    
    next_sequence = [diff(seq[i],seq[i+1]) for i in range(len(seq) - 1)]

    if all(v == 0 for v in next_sequence):
        return seq[-1]
    else: 
        return seq[-1] + get_next(next_sequence)


sum =  0

for line in input_stream:
    digits = list(map(int, re.findall(r'-*\d+', line)))
    sum += get_next(digits)

print(sum)