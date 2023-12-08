file = 'test.txt'

input_stream = [line.strip() for line in open(file, 'r')]

directions = input_stream[0]
node_lines = input_stream[2:]

nodes = dict()

for line in node_lines:
    label, arms = line.split(' = (')
    l, r = arms.removesuffix(')').split(', ')
    nodes[label] = (l, r)

d_lookup = {'L': 0, 'R': 1}

current_node = 'AAA'
end = 'ZZZ'
step = 0

while current_node != end:
    direction = directions[step % len(directions)]
    # go to next node
    current_node = nodes[current_node][d_lookup[direction]]
    # take the next step
    step += 1

print(step)



    

