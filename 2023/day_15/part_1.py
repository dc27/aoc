file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

steps = []
for line in input_stream:
    new_steps = line.split(",")
    steps.extend(new_steps)

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

result = 0
for step in steps:
    result += HASH(step)

print(result)

