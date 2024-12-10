# The map shows the current position of the guard with ^ 
# (to indicate the guard is currently facing up from the perspective of the map)
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #
# Lab guards repeatedly follow these steps:
# - If there is something directly in front of you, turn right 90 degrees.
# - Otherwise, take a step forward.
# How many distinct positions will the guard visit before leaving the mapped area?

# Import os and time module to animate stdout
import os
import time

# Set input file path
file_path = 'rob.txt'

# Create matrix with x, y origin at top left
matrix = []
try:
  # Try to open the file and read each line
  with open(file_path, 'r') as file:
      for line in file:
          if not line.strip():  # Skip empty lines
              continue
          try:
              row = list(line.strip())
              matrix.append(row)
          except ValueError:
              print(f"Invalid line in file: {line.strip()}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Clear stdout and print the matrix nicely
def print_matrix():
    global matrix
    time.sleep(0.2)
    os.system('clear')
    for row in matrix:
        print(''.join(row))

# Safe access function to get matrix values, safely handles out-of-bounds access
# Returns None if indices are out of bounds

def get_value(x, y):
    if x < 0 or y <0:
        return None
    try:
        return matrix[y][x]
    except IndexError:
        print("Exited maze!")
        return None

# Find the x, y position of the security guard "^" in the matrix
# todo fix naming in this function

def find_guard():
    for y_index, row in enumerate(matrix):
        for x_index, column in enumerate(row):
            if column == "^":
                return [x_index, y_index]
    raise Exception("No guard found")

# List of directional modifiers
modifier = [
    [0, -1], # up
    [1, 0], # right
    [0, 1], # down
    [-1, 0], # left
]

guard_x_location = find_guard()[0]
guard_y_location = find_guard()[1]
guard_facing = 0

def move_guard(guard_x, guard_y):
    global guard_facing
    global guard_x_location
    global guard_y_location
    proposed_x = guard_x + modifier[guard_facing][0]
    proposed_y = guard_y + modifier[guard_facing][1]
    proposed_tile_value = get_value(proposed_x, proposed_y)
    match proposed_tile_value:
        case "#":
            # print_matrix() # Uncomment to see the guards movement
            guard_facing = (guard_facing + 1) % 4
        case "^" | ".":
            guard_x_location = proposed_x
            guard_y_location = proposed_y
            matrix[proposed_y][proposed_x] = "X"
        case "X":
            guard_x_location = proposed_x
            guard_y_location = proposed_y
        case None:
            guard_x_location = None
            guard_y_location = None

def guard_turns():
    while guard_x_location or guard_y_location is not None:
        move_guard(guard_x_location, guard_y_location)

guard_turns()

# Initialize current sum
sum = 0
def get_sum():
    global sum
    for row in matrix:
        for column in row:
            if column in ["X", "^"]:
                sum += 1
get_sum()
print(f"sum is: {sum}")

# Loop through each turn the guard takes
# - if the tile he is moving to is open aka not "#", update it to an "X" and move forward
# - if the tile he is moving to is a "#", turn right 90 degrees aka update the direction modifier
# - if the time he is moving to is out of bounds end the loop
# then count all the "X"s in the matrix