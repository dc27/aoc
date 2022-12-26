file = 'input.txt'

# format = (x, y)

H = (0, 0)
T = (0, 0)

in_between_nodes = list(map(str, range(1, 9)))

node_pos = {
    'H' : H
}

for node in in_between_nodes:
    node_pos[node] = (0, 0)

node_pos['T'] = T

h_shifts = {
    'U' : (0, 1),
    'R' : (1, 0),
    'D' : (0, -1),
    'L' : (-1, 0)
}

def move_tail(h, t):

    diff_x = h[0] - t[0]
    diff_y = h[1] - t[1]

    # up
    if diff_y >= 2:
        t = (h[0], h[1] -1)
    # down
    elif diff_y <= -2:
        t = (h[0], h[1] + 1)
    # right    
    elif diff_x >= 2:
        t = (h[0] -1, h[1])
    # left    
    elif diff_x <= -2:
        t = (h[0] + 1, h[1])
    
    return(t)


t_pos = set()

nodes = list(node_pos.keys())

for line in open(file):
    dir, n = line.strip().split(' ')
    n = int(n)
    for i in range(n):
        # update Head
        node_pos['H'] = (node_pos['H'][0] + h_shifts[dir][0], node_pos['H'][1] + h_shifts[dir][1])
        for j in range(1, 10):
        # print(H)
            T = move_tail(node_pos[nodes[j-1]], node_pos[nodes[j]])
            t_pos.add(T)


print(len(t_pos))
