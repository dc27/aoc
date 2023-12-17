from collections import defaultdict

def HASH(string:str)->int:
    
    current_value = 0

    for char in string:
        
        # 1. determine the ascii code for the current string
        # 2. increase the current value by the ASCII code you just determined
        current_value += ord(char)
        # 3. set the current value to itself multiplied by 17
        current_value *= 17
        # 4. set the current value to the remainder of dividing itself by 255
        current_value %= 256

    return current_value

# 1. parse input into list of steps
file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

steps = []

for line in input_stream:
    new_steps = line.split(",")
    steps.extend(new_steps)

# 2. carry out steps
boxes = defaultdict(dict)

for step in steps:
    # case 1 (=) add or replace lens in box
    if "=" in step:
        label, focal_length = step.split("=")
        box = str(HASH(label))
        # python dicts remember order of insertion
        boxes[box][label] = int(focal_length)
   # case 2 (-) remove lens from box 
    else:
        label, _ = step.split("-")
        box = str(HASH(label))
        # None in case that lens wasn't actually in that box (avoid KeyError)
        boxes[box].pop(label, None)

# 3. calculate total focussing power
# fp = box_number + 1 * slot_number * value

total_focussing_power = 0
for box, lenses in boxes.items():
    # empty (all the lenses got removed after being put in)
    if lenses == {}:
        continue

    slot_number = 1
    for _, value in lenses.items():
        focussing_power = (int(box) + 1) * slot_number * value
        total_focussing_power += focussing_power
        # next slot is 1 more further
        slot_number += 1

print(total_focussing_power)

    

