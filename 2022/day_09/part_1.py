file = 'input.txt'

# format = (x, y)

H = (0, 0)
T = (0, 0)

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

for line in open(file):
    dir, n = line.strip().split(' ')
    n = int(n)
    for i in range(n):
        # update Head
        H = (H[0] + h_shifts[dir][0], H[1] + h_shifts[dir][1])
        # print(H)
        T = move_tail(H, T)
        t_pos.add(T)


print(len(t_pos))
