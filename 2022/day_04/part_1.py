file = 'input.txt'

CUM_SUM = 0

for line in open(file):
    e1, e2 = line.strip().split(',')

    init_1, fin_1 = map(int, e1.split('-'))
    init_2, fin_2 = map(int, e2.split('-'))

    # first is entirely within second
    if (init_1 >= init_2) & (fin_1 <= fin_2):
        CUM_SUM += 1
    # second is entirely within first
    elif (init_2 >= init_1) & (fin_2 <= fin_1):
        CUM_SUM += 1

print(CUM_SUM)