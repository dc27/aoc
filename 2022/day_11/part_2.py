file = 'input.txt'

from math import floor

class Monke:

    '''
    Each monkey has several attributes:

    Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
    Operation shows how your worry level changes as that monkey inspects an item.
    (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
    Test shows how the monkey uses your worry level to decide where to throw an item next.
    If true shows what happens with an item if the Test was true.
    If false shows what happens with an item if the Test was false.
    '''

    def __init__(self, name, items, op, test, t, f):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.t = t
        self.f = f

    def info(self):
        print(
            f'''
name:{self.name},
items:{self.items},
operation:{self.op},
test: {self.test},
if_t:{self.t},
if_f:{self.f}
            '''
            )

    def inspect(self, old):
        new = 0
        _locals = locals()
        exec(self.op, globals(), _locals)
        return(_locals['new'])

    def inspect_items(self):
        self.items = tuple(self.inspect(item) for item in self.items)
        pass


    def do_test(self, monkeys, product):
        for item in self.items:
            item = item % product # keep worry level (item) from getting too large
            if item % self.test == 0:
                monkeys[self.t].items += (item,)
            else:
                monkeys[self.f].items += (item,)

        self.items = ()
        

# get monkey info from file
lines = [line.strip('\n') for line in open(file)]

monkes = []
monke = []

for line in lines:
    if line == '':
        monkes.append(monke)
        monke = []
    else:
        monke.append(line)
else:
    monkes.append(monke)

# assign monkey info to Monke objects
Monkeys = []

for i in range(len(monkes)):
    starting_items = tuple(map(int, monkes[i][1].split(': ')[-1].split(',')))
    operation = monkes[i][2].split(': ')[-1]
    test = int(monkes[i][3].split(' ')[-1])
    testTrue = int(monkes[i][4].split(' ')[-1])
    testFalse = int(monkes[i][5].split(' ')[-1])
    monkey = Monke(i, starting_items, operation, test, testTrue, testFalse)
    Monkeys.append(monkey)

inspected_items = [0] * len(Monkeys)

test_product = 1

# numbers get too big when unchecked.
# get product of all monkey test divisors and
# replace items with remainder after dividing by product
for monkey in Monkeys:
    test_product *= monkey.test

for cycle in range(1, 10001):
    for i in range(len(Monkeys)):
        Monkeys[i].inspect_items()
        inspected_items[i] += len(Monkeys[i].items)
        # pass product in (calc it only once)
        Monkeys[i].do_test(Monkeys, test_product)

inspected_items.sort()

monkey_business = inspected_items[-1] * inspected_items[-2]

print(monkey_business)


