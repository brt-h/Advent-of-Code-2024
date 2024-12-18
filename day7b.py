from typing import List

def read_equations(file_path):
  """
  Reads and parses the equations file into a list of equations.
  The first number serves as the target value, while the remaining numbers can
  be combined using the "+" and "*" operators to potentially achieve a true equation.
  Equations are evaluated left to right, ignoring the standard precedence rules.
  The order of numbers remains fixed; only the operators can change.
  """
  try:
      with open(file_path, 'r') as file:
          equations = []
          for line in file:
              parts = line.strip().replace(':', ' ').split()
              equation = list(map(int, parts))
              equations.append(equation)
          return equations
  except FileNotFoundError:
      print(f"File not found: {file_path}")
      exit()

def print_equations(equations):
    for line in equations:
        print(line)

# Applies the given operator to the current result and the next number
# in the equation.
def apply_operator(current_result, next_number, operator):
    if operator == '+':
        return current_result + next_number
    elif operator == '*':
        return current_result * next_number
    elif operator == '||':
        # concatenate two integers into a single integer
        return int(str(current_result) + str(next_number))

# Depth-first search function to evaluate if the equation can sum 
# up to the expected result using any combination of operators.
def dfs(start_index, current_result, equation):
    if start_index == len(equation):
        return current_result == equation[0]
    for operator in ['+', '*', '||']:
        next_result = apply_operator(current_result, equation[start_index], operator)
        if dfs(start_index + 1, next_result, equation):
            return True
    return False

# Evaluates an equation by initializing the depth-first search.
def evaluate_equation(equation):
    if len(equation) < 2:  # At least one number and target are needed
        return False
    return dfs(start_index=2, current_result=equation[1], equation=equation)

# Sums the results of equations that can be evaluated as true.
def sum_valid_equations(equations):
    sum = 0
    for equation in equations:
        if evaluate_equation(equation):
            sum += int(equation[0])  # Adding the target value of valid equations
    return sum

equations = read_equations('rob.txt')
print_equations(equations)
valid_equations = sum_valid_equations(equations)
print(f"Sum of valid equations: {valid_equations}")