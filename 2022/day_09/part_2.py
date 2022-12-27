file = 'input.txt'

# format = (x, y)

# ----- set up nodes -----
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


def follow_head(h, t):

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

def follow_tail(t1, t2):

    diff_x = t1[0] - t2[0]
    diff_y = t1[1] - t2[1]

    # if it's 0 or 1 away in both directions no need to move
    if abs(diff_x) < 2 & (abs(diff_y) < 2):
        return(t2)

    # squares
    if (diff_x >= 2) & (diff_y >= 2):
        t2 = (t1[0] - 1, t1[1] - 1)
    elif (diff_x <= -2) & (diff_y >= 2):
        t2 = (t1[0] + 1, t1[1] - 1)
    elif (diff_x >= 2) & (diff_y <= -2):
        t2 = (t1[0] - 1, t1[1] + 1)
    elif (diff_x <= -2) & (diff_y <= -2):
        t2 = (t1[0] + 1, t1[1] + 1)
    else:
        t2 = follow_head(t1, t2)
    
    return(t2)
    

t_pos = set()

nodes = list(node_pos.keys())

for line in open(file):
    dir, n = line.strip().split(' ')
    n = int(n)
    for i in range(n):
        # update Head
        # (list of lists would have been easier to index)
        node_pos['H'] = (node_pos['H'][0] + h_shifts[dir][0], node_pos['H'][1] + h_shifts[dir][1])
        # update first tail
        node_pos['1'] = follow_head(node_pos['H'], node_pos['1'])
        # update all other Tails, using previous as Head
        for j in range(2, 10):
            node_pos[nodes[j]] = follow_tail(node_pos[nodes[j-1]], node_pos[nodes[j]])
        
        t_pos.add(node_pos['T'])

    # print(dir, n)
    # for k, v in node_pos.items():
    #     print(f'{k}: {v}')

print(len(t_pos))
# print(sorted(t_pos))
