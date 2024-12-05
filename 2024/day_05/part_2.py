import re
import math

file = "input.txt"

page_ordering_rules = []
update_instructions = []


#>>> parsing input
for line in open(file, 'r'):
  line = line.strip()
  rule = list(map(int, re.findall(r"\d+", line)))
  if "|" in line:
    page_ordering_rules.append(rule)
  
  if "," in line:
    update_instructions.append(rule)
  

#>>> finding invalid rules
invalid_instructions = []

for x, I in enumerate(update_instructions):
  valid = True

  full = I.copy()
  I.reverse()

  relevant_rules = [[X, Y] for X, Y in page_ordering_rules if X in I and Y in I]
  for page_num in I:
    relevant_rules_update = []
    for X, Y in relevant_rules:
      if X == page_num:
        valid = False
      
      if Y != page_num:
        relevant_rules_update.append([X, Y])

    relevant_rules = relevant_rules_update
  
  if valid == False:
    invalid_instructions.append(full)

valid_instructions = []

#>>> sorting invalid rules
for I in invalid_instructions:
  relevant_rules = [[X, Y] for X, Y in page_ordering_rules if X in I and Y in I]

  correct_order = []
  for i in range(len(I)):
    Xs = [rule[0] for rule in relevant_rules]
    last_number = [x for x in I if x not in correct_order and x not in Xs][0]
    
    relevant_rules = [[X, Y] for X, Y in relevant_rules if Y != last_number]

    correct_order.insert(0, last_number)

  valid_instructions.append(correct_order)



def get_middles(instructions:list[int])->int:
  MIDDLES = 0

  for r in instructions:

    middle_value = r[math.floor(len(r)/2)]
    MIDDLES += middle_value
  
  return MIDDLES

print(get_middles(valid_instructions))
  
