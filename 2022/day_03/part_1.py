file = 'input.txt'

def bisect_string(x):
    midpoint = int(len(x)/2)
    return([x[0:midpoint], x[midpoint:]])

def get_repeated_characters(x):
    return(list(set(x[0]) & set(x[1]))[0])

letters = 'abcdefghijklmnopqrstuvwxyz'
LETTERS = letters.upper()

values = letters + LETTERS

CUM_PROP_SUM = 0

for line in open(file):
    x = line.strip()
    comp_conts = bisect_string(x)
    repeated_character = get_repeated_characters(comp_conts)
    value = values.index(repeated_character) + 1
    CUM_PROP_SUM += value

print(CUM_PROP_SUM)

