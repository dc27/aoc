file = 'input.txt'

clock:int = 1
X:int = 1 
cumsum = 0

interesting = list(range(20, 260, 40))

for line in open(file):
    l = line.strip()
    
    clock += 1

    if clock in interesting:
        print(X)
        cumsum += (X * clock)

    if l[0] != 'n': 
        _, n = l.split()
        X += int(n)
        clock += 1
        if clock in interesting:
            print(X)
            cumsum += (X * clock)



print(cumsum)
print(interesting)