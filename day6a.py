# The map indicates the current position of the guard with "^"
# (this indicates the guard is currently facing upwards on the map)
# Obstructions such as crates, desks, and alchemical reactors are shown as "#"
# Lab guards follow a procedure repeatedly:
# - If an obstruction is immediately in front, turn right 90 degrees.
# - Otherwise, move one step forward.
# Determine how many distinct positions the guard visits before leaving the area.

# Import the os and time modules to manage and animate the command-line output
import os
import time

# Define the input file path
file_path = 'rob.txt'

# Initialize the matrix with origin point at top left
matrix = []
try:
    # Open and read each line from the file
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():  # Skip over any empty lines
                continue
            try:
                # Convert the line into a list and append to the matrix
                row = list(line.strip())
                matrix.append(row)
            except ValueError:
                print(f"Invalid line in file: {line.strip()}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Clear and print the matrix to stdout nicely
# Animates the matrix display so it's visually clear
# how the guard moves inside the area


def print_matrix():
    global matrix
    time.sleep(0.2)
    os.system('clear')  # Use 'cls' for Windows
    for row in matrix:
        print(''.join(row))


# Safely access the matrix value at a given position
# Prevents out-of-bounds errors by returning None if attempted access
# to an out-of-bounds index occurs


def get_value(x, y):
    if x < 0 or y < 0:
        return None
    try:
        # Attempt to return the value from the matrix
        return matrix[y][x]
    except IndexError:
        print("Exited maze!")  # Notify when the guard exits the maze
        return None


# Locate the guard's (marked by "^") x, y position within the matrix


def find_guard():
    for y_index, row in enumerate(matrix):
        for x_index, column in enumerate(row):
            if column == "^":
                return [x_index, y_index]
    raise Exception(
        "No guard found")  # Error raised if guard is not found in matrix


# Define positional modifiers for directional guidance:

modifier = [
    [0, -1],  # Move up
    [1, 0],  # Move right
    [0, 1],  # Move down
    [-1, 0],  # Move left
]

# Start guard's location by capturing initial position from the matrix

initial_guard_position = find_guard()
guard_x_location, guard_y_location = initial_guard_position
# Initialize the initial direction the guard is facing (0 = up)
guard_facing = 0

# Function to adjust the guard's position
# Changes coordinates based on current facing direction and matrix content


def move_guard(guard_x, guard_y):
    global guard_facing, guard_x_location, guard_y_location
    proposed_x = guard_x + modifier[guard_facing][0]  # Proposed new x position
    proposed_y = guard_y + modifier[guard_facing][1]  # Proposed new y position
    proposed_tile_value = get_value(proposed_x,
                                    proposed_y)  # Check the matrix value
    match proposed_tile_value:
        case "#":
            # Turn 90 degrees right due to obstruction
            guard_facing = (guard_facing + 1) % 4
            # print_matrix() # Uncomment to see the guards movement
        case "^" | ".":
            # Mark moved positions with an 'X' and update guard position
            guard_x_location = proposed_x
            guard_y_location = proposed_y
            matrix[proposed_y][proposed_x] = "X"
        case "X":
            # Already visited positions don't require marking
            guard_x_location = proposed_x
            guard_y_location = proposed_y
        case None:
            # Exiting when moving to an area outside the matrix
            guard_x_location = None
            guard_y_location = None


# Coordinates the guard's turns, looping until he exits via an out-of-bounds space
# Uses the current global guard positions and direction to move or turn


def guard_turns():
    while guard_x_location is not None and guard_y_location is not None:
        move_guard(guard_x_location, guard_y_location)


guard_turns()

# Calculate and print total distinct positions visited by the guard
# Includes positions occupied by '^' and 'X'

sum = 0

# Define a function to count and return the number of visited positions


def get_sum():
    global sum
    for row in matrix:
        for column in row:
            if column in ["X", "^"]:
                sum += 1


get_sum()
print(f"sum is: {sum}")  # Output total count of visited positions
