import re
import math
  
def parse_input(file:str="input.txt")->list[list]:

  page_ordering_rules = []
  page_orders = []

  #>>> parsing input
  for line in open(file, 'r'):
    line = line.strip()
    rule = list(map(int, re.findall(r"\d+", line)))
    if "|" in line:
      page_ordering_rules.append(rule)
    
    if "," in line:
      page_orders.append(rule)

  return [page_ordering_rules, page_orders]

def check_valid(page_order_rules:list[list], page_orders:list[list])->dict[list]:

  #>>> finding invalid rules
  valid_instructions = []
  invalid_instructions = []

  for I in page_orders:
    valid = True

    full = I.copy()
    I.reverse()

    relevant_rules = [[X, Y] for X, Y in page_order_rules if X in I and Y in I]
    for page_num in I:
      relevant_rules_update = []
      for X, Y in relevant_rules:
        # TODO: explain logic
        if X == page_num:
          valid = False
        
        if Y != page_num:
          relevant_rules_update.append([X, Y])

      relevant_rules = relevant_rules_update
    
    if valid == True:
      valid_instructions.append(full)
    else:
      invalid_instructions.append(full)

  return {"valid": valid_instructions, "invalid": invalid_instructions}


def make_valid(page_order_rules:list[list], invalid_page_orders:list[list])->list[list]:

    #>>> sorting invalid rules
  valid_page_orders = []

  for I in invalid_page_orders:
    relevant_rules = [[X, Y] for X, Y in page_order_rules if X in I and Y in I]

    correct_order = []
    for _ in range(len(I)):
      # TODO: explain logic more better
      # pretty much: go through the first numbers (the X value) in the page
      # order rules relevant to the pages in the print instruction
      # the only possible last/next number is the number in the print instruction that is not in X
      # the relevant rules need to be dwindled down to not include the number added
      Xs = [rule[0] for rule in relevant_rules]
      last_number = [x for x in I if x not in correct_order and x not in Xs][0]
      
      relevant_rules = [[X, Y] for X, Y in relevant_rules if Y != last_number]

      correct_order.insert(0, last_number)

    valid_page_orders.append(correct_order)

  return valid_page_orders

def get_middles(instructions:list[list])->int:
  MIDDLES = 0

  for r in instructions:

    middle_value = r[math.floor(len(r)/2)]
    MIDDLES += middle_value
  
  return MIDDLES


def solve(file:str="input.txt", part=1)->int:
  """
  Day 5 Solution
  1. parse input into two lists [order rules, print orders]
  2. organise print orders into two categories, valid / invalid
     to check if the print order is valid:
        start with last number in order
        if any order rules have the last number before any other number still to be checked then it is invalid
  3. depending on which part either
     (part 1) add up the middle-index value in each valid print order
     (part 2) add up the middle-index value of each invalid print order after the print order has been made valid
  """

  page_order_rules, page_orders = parse_input(file=file)
  
  categorised_page_orders = check_valid(page_order_rules, page_orders)

  
  if part == 1:
    MIDDLES = get_middles(categorised_page_orders["valid"])
  if part == 2:
    newly_validated_page_orders = make_valid(page_order_rules, categorised_page_orders["invalid"])
    MIDDLES = get_middles(newly_validated_page_orders)

  return MIDDLES


print(solve("input.txt", part=1))
print(solve("input.txt", part=2))
