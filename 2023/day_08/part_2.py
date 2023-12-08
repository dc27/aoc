import math

file = 'input.txt'

input_stream = [line.strip() for line in open(file, 'r')]

directions = input_stream[0]
node_lines = input_stream[2:]

nodes = dict()

for line in node_lines:
    label, arms = line.split(' = (')
    l, r = arms.removesuffix(')').split(', ')
    nodes[label] = (l, r)

d_lookup = {'L': 0, 'R': 1}

# multiple start points this time
start_nodes = [node for node in nodes.keys() if node.endswith('A')]
steps = dict()

# iterate over each start point
for node in start_nodes:
    current_node = node
    step = 0

    # get number of steps it takes to reach end point
    while not current_node.endswith('Z'):
        direction = directions[step % len(directions)]
        # go to next node
        current_node = nodes[current_node][d_lookup[direction]]
        # take the next step
        step += 1
    
    steps[current_node] = step

# answer is lowest common multiple of all the steps in each cycle.
print(math.lcm(*sorted(steps.values())))

