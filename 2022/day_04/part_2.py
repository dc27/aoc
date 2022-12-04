file = 'input.txt'

CUM_SUM = 0

for line in open(file):
    e1, e2 = line.strip().split(',')

    init_1, fin_1 = map(int, e1.split('-'))
    init_2, fin_2 = map(int, e2.split('-'))

    # overlap when any 1 == 2
    if len(set([init_1, fin_1]) & set([init_2, fin_2])) > 0:
        CUM_SUM += 1
    # when any 1 is between 2
    elif ((init_1 > init_2) & (init_1 < fin_2)) | ((fin_1 > init_2) & (fin_1 < fin_2)):
        CUM_SUM +=1
    # when any 2 is between 1
    elif ((init_2 > init_1) & (init_2 < fin_1)) | ((fin_2 > init_1) & (fin_2 < fin_1)):
        CUM_SUM +=1 

print(CUM_SUM)

