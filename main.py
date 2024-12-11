# This script simulates a guard's movements in a maze.
# The guard's initial position is indicated by "^",
# meaning the guard faces upwards initially.
# Obstructions such as crates, desks, and alchemical reactors are represented as "#".
# The guard follows these rules in order:
# - If an obstruction is immediately ahead, it turns right by 90 degrees
# - Otherwise, it moves forward by one step
# We aim to calculate the number of distinct positions the guard visits before leaving
# the grid.

import os
import time

file_path = 'rob.txt'
matrix = []

def create_matrix():
    # Read matrix data from a file and prepare the matrix for further operations.
    global matrix
    matrix = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue
                row = list(line.strip())  # Create a list of characters for the row
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()  # Terminate the program if the file is not found

create_matrix()

def print_matrix():
    # Print matrix to the console (for debugging purposes)
    global matrix
    time.sleep(0.01)
    os.system('clear')  # Clears terminal, use 'cls' if on Windows
    for row in matrix:
        print(''.join(row))  # Join row list into string before printing

def get_value(x, y):
    # Safely get the value from matrix at (x, y)
    if x < 0 or y < 0:
        return None  # Return None if outside bounds
    try:
        return matrix[y][x]
    except IndexError:
        return None  # Return None if outside bounds

def find_guard():
    # Finds the current position of the guard denoted by "^"
    for y_index, row in enumerate(matrix):
        for x_index, column in enumerate(row):
            if column == "^":
                return [x_index, y_index]
    raise Exception("No guard found")  # Raise an error if no guard is present

modifier = [
    [0, -1],  # Move up
    [1, 0],  # Move right
    [0, 1],  # Move down
    [-1, 0],  # Move left
]

# Initialize guard position and direction
# Guard's facing direction is encoded as 0 (up), 1 (right), 2 (down), or 3 (left)
guard_x_location, guard_y_location = find_guard()
guard_facing = 0

visited_states = set()  # Maintain a set of visited states

def move_guard(guard_x, guard_y):
    # Manage guard movement based on current facing direction and surroundings.
    global guard_facing, guard_x_location, guard_y_location
    proposed_x = guard_x + modifier[guard_facing][0]
    proposed_y = guard_y + modifier[guard_facing][1]
    proposed_tile_value = get_value(proposed_x, proposed_y)
    # print_matrix()  # Uncomment this line to view each move step-by-step
    match proposed_tile_value:
        case "#":
            guard_facing = (guard_facing + 1) % 4  # Turn right
        case "^" | ".":
            guard_x_location = proposed_x
            guard_y_location = proposed_y
            matrix[proposed_y][proposed_x] = "X"  # Mark path taken on grid
        case "X":
            guard_x_location = proposed_x
            guard_y_location = proposed_y
        case None:
            guard_x_location = None
            guard_y_location = None
            # Exiting the map upon encountering None
            print(f"Obstacle location {obstacle_location}: guard exited maze")

def guard_in_loop():
    # Detect if the guard enters a cyclic path
    global visited_states, valid_obstacle_locations
    current_state = (guard_x_location, guard_y_location, guard_facing)
    if current_state in visited_states:
        print(f"Obstacle location {obstacle_location}: guard is in a loop!")
        valid_obstacle_locations += 1  # Increase count if loop found
        time.sleep(1)  # Pause for clarity in console output
        return True
    visited_states.add(current_state)  # Add new state to visited set
    return False

def guard_turns():
    # Manage guard's turns and movements until it exits the area or loops
    while (not guard_in_loop()) and (guard_x_location is not None) and (guard_y_location is not None):
        move_guard(guard_x_location, guard_y_location)

# Initialize counter of valid obstacle positions
valid_obstacle_locations = 0

# Iterate over the grid, attempting to place an obstacle at each point and test path
for obstacle_y in range(len(matrix)):
    for obstacle_x in range(len(matrix[0])):
        create_matrix()  # Reset the matrix for each test
        if matrix[obstacle_y][obstacle_x] != ".":
            print(f"Obstacle location {[obstacle_x, obstacle_y]}: already occupied")
        if matrix[obstacle_y][obstacle_x] == ".":
            guard_x_location, guard_y_location = find_guard()  # Re-get guard position
            visited_states = set()  # Reset visited states for new test
            guard_facing = 0  # Reset initial guard direction
            obstacle_location = [obstacle_x, obstacle_y]  # Track current obstacle location
            matrix[obstacle_y][obstacle_x] = "#"  # Place obstacle
            guard_turns()  # Simulate guard movements for this setup

# Final output of the number of obstacle locations that allow guard looping
print(f"number of valid obstacle locations: {valid_obstacle_locations}")