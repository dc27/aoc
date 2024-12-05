import re
import math

file = "input.txt"

page_ordering_rules = []
update_instructions = []

for line in open(file, 'r'):
  line = line.strip()
  rule = list(map(int, re.findall(r"\d+", line)))
  if "|" in line:
    page_ordering_rules.append(rule)
  
  if "," in line:
    update_instructions.append(rule)
  
first_instruction = [42,54,21,36,22,33,13,29,35]

# is there a rule that says 54, 21, 36, 22, 33, 13, 19, or 35 must come before 42?
# is there a rule that says 21, 36, 22, 33, 13, 29, or 35 must come before 54?
# is there a rule that says 36, 22, 33, 13, 29, or 35 must come before 21 ?
# is there a rule ...
# is there a rule that says 35 must come before 29?

# reverse initially?

# does 35 have to come before any of [29, 13, 33, 22, 36, 21, 54, 42]? -> invalid if so
# does 29 have to come before any of

valid_rules = []

for x, I in enumerate(update_instructions):
  valid = True

  full = I.copy()
  I.reverse()
  
  print(x, I)

  relevant_rules = [[X, Y] for X, Y in page_ordering_rules if X in I and Y in I]
  for page_num in I:
    relevant_rules_update = []
    for X, Y in relevant_rules:
      if X == page_num:
        valid = False
      
      if Y != page_num:
        relevant_rules_update.append([X, Y])

    relevant_rules = relevant_rules_update
  
  if valid == True:
    valid_rules.append(full)

MIDDLES = 0

for r in valid_rules:
  middle_value = r[math.floor(len(r)/2)]
  MIDDLES += middle_value
  

print(MIDDLES)
  
