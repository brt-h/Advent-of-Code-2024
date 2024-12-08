# Set input file path
file_path = 'rob.txt'

# Create matrix
matrix = []
try:
  # Try to open the file and read each line
  with open(file_path, 'r') as file:
      for line in file:
          if not line.strip():  # Skip empty lines
              continue
          try:
              # Convert line to list of integers, skipping ValueError
              row = list(line.strip())
              matrix.append(row)
          except ValueError:
              print(f"Invalid line in file: {line.strip()}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Safe access function to get matrix values, safely handles out-of-bounds access
# Returns None if indices are out of bounds

def get_value(row, col):
    if row < 0 or col <0:
        return None
    try:
        return matrix[row][col]
    except IndexError:
        return None

# Initialize current sum and list of potential movement directions
curr = 0

# List of directional modifiers used to locate adjacent "M" and "S"
modifiers = [
    # [modifier_row, modifier_col] format
    [1, -1], # check diagonal up left
    [1, 1], # check diagonal up right
    [-1, 1], # check diagonal down right
    [-1, -1] # check diagonal down left
]


# Iterate through all items in matrix to find center point "A"
for row_index, row in enumerate(matrix):
    for column_index, letter in enumerate(row):
        if letter == "A":
            # Found center point "A", now checking diagonals for "M"
            for mod_index, modifier1 in enumerate(modifiers):
                # Checking first modifier direction for "M"
                if get_value(row_index + modifier1[0], column_index + modifier1[1]) == "M":
                    for modifier2 in (modifiers[:mod_index] + modifiers[mod_index + 1:]):
                        # Checking second modifier direction for another "M"
                        if get_value(row_index + modifier2[0], column_index + modifier2[1]) == "M":
                            # Check the opposite sides for two "S"
                            if get_value(row_index + (modifier1[0] * -1), column_index + (modifier1[1] * -1)) == "S":
                                if get_value(row_index + (modifier2[0] * -1), column_index + (modifier2[1] * -1)) == "S":
                                    # Found pattern X-MAS centered on "A", increment current count
                                    curr += 1

# Each "X-MAS" is double counted due to checking both diagonals, so divide by 2
curr = int(curr / 2)

print(curr)