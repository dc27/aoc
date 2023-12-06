import re
import math

file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

# parse input into list of tuples of ints

for line in input_stream:
    if line.startswith("Time"):
        line = line.removeprefix("Time:")
        line = line.replace(' ', '')
        time = int(line)
    if line.startswith("Distance"):
        line = line.removeprefix("Distance:")
        line = line.replace(' ', '')
        distance = int(line)

# previous solution was made to work with a list of tuples ...
race_stats = [(time, distance)]

# brute force. for every time work out if you will win the race

# not so brute force. work out the first point where you win the race.
# work out the last point you win the race.

def get_dist(hold_time:int, race_time:int)->int:

    speed = hold_time
    time = race_time - hold_time

    return speed * time

hold_time_ranges = []

# run simulations
for rs in race_stats:
    max_t = rs[0]
    distance_to_beat = rs[1]

    min_hold_time = max_hold_time = None

    # bottom up
    for hold_time in range(1, max_t):
        distance_travelled = get_dist(hold_time, max_t)
        if distance_travelled > distance_to_beat:
            min_hold_time = hold_time
            break

    # top down
    for hold_time in range(max_t-1, 1, -1):
        distance_travelled = get_dist(hold_time, max_t)
        if distance_travelled > distance_to_beat:
            max_hold_time = hold_time
            break

    hold_time_ranges.append(max_hold_time - min_hold_time + 1)

print(math.prod(hold_time_ranges))
    


    


        

