import string

file = 'input.txt'

lines = [list(line.strip()) for line in open(file)]

# helpers
def search_maze(array, term):
    for r in range(len(array)):
        for c in range(len(array[r])):
            if array[r][c] == term:
                return(r,c)

    else:
        return('Not in array')

def letter_lookup(letters, letter):
    return(letters.index(letter))

# probably not necessary
letters = string.ascii_lowercase[:]

# grab start and end positions
start = search_maze(lines, 'E')

# pre pathfinding setup
end_reached = False
position = start
lines[start[0]][start[1]] = 'z'
# so letters can be compared after they've been reassigned in the traversing mat
# kinda like a mirror matrix
original_mat = list(map(list, lines))
lines[start[0]][start[1]] = '0'
count = 0

queue = [position]

# I think this is an example of Lee's algorithm
# until reaching the end, set next nodes to 1+ whatever the current pos is,
# for each of the next noeds set the next next nodes to 1+ whatever the current pos is ...

# for p2 this is essential a reverse from p1 since this time we're looking for new start
# positions. So start at the end and work backword. Some rules need changed...
while end_reached == False:

    for _ in range(len(queue)):
        
        # each direction
        position = queue.pop()
        a = position[0] -1, position[1]
        l = position[0], position[1] - 1
        b = position[0] + 1, position[1]
        r = position[0], position[1] + 1

        for d in [a, l, b, r]:
            # make sure we can actually go there (within bounds of 2darray)
            if (0 <= d[0] < (len(lines))) & (0 <= d[1] < (len(lines[0]))):
                # end condition (reverse of part 1 - end at first a reached legally)
                if (lines[d[0]][d[1]] == 'a') & (letter_lookup(letters, original_mat[position[0]][position[1]]) <= 1):
                    print(f'steps: {count + 1}')
                    end_reached = True
                    break
                
                # if unvisited
                elif lines[d[0]][d[1]] in letters:
                    # moving condition thing from q. (reverse of part 1, can go to any letter above current letter or one below current letter)
                    if (letter_lookup(letters, original_mat[d[0]][d[1]])) >= (letter_lookup(letters, original_mat[position[0]][position[1]]) -1):
                        lines[d[0]][d[1]] = str(count + 1)
                        # add next nodes to queue for next time
                        new = d[0], d[1]
                        queue.insert(0, new) 
    
    count += 1
    