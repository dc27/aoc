import re

def parse_input(file:str="test.txt")->list[list]:
  """
  Parses the input into a navigable data structure
  """
  lines = []

  for line in open(file, 'r'):
      line = line.strip()
      (r, *el) = map(int, re.findall(r"\d+", line))
      lines.append((r, el))

  return lines
    

def can_achieve(goal:int, nums:tuple[int], part:int=1):
    def evaluate_expr(index, current):
        """
        Recursve function to evaluate all possible operations applied to nums to achieve goal value

        params:
          index: index of nums tup
          current: cumulative result of operations
        """
        # early breakout: if current exceeds goal, goal will never be reached.
        if current > goal:
            return False

        # base case: if all numbers have been used
        if index == len(nums):
            return current == goal

        next_num = nums[index]

        # explore all operations recursively
        # (addition, subtraction and concatenation)

        if part == 1:
          return (
              evaluate_expr(index + 1, current + next_num) or
              evaluate_expr(index + 1, current * next_num)
          )
        else:
            return (
              evaluate_expr(index + 1, current + next_num) or
              evaluate_expr(index + 1, current * next_num) or
              evaluate_expr(index + 1, int(str(current) + str(next_num)))
          ) 
        

    return evaluate_expr(1, nums[0])  # start with the first number

# Solve the problem
def solve(file:str="test.txt", part:int=1)->int:

  lines =  parse_input(file)

  TOTAL = 0

  for goal, nums in lines:
      if can_achieve(goal, tuple(nums), part=part):
          TOTAL += goal

  return TOTAL

print(solve("input.txt", part=1))
print(solve("input.txt", part=2)) 