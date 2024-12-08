# Set input file path
file_path = 'rob.txt'

# Create matrix
matrix = []
try:
  with open(file_path, 'r') as file:
      for line in file:
          if not line.strip():  # Skip empty lines
              continue
          try:
              # Convert line to list of integers
              row = list(line.strip())
              matrix.append(row)
          except ValueError:
              print(f"Invalid line in file: {line.strip()}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Safe access function
def get_value(row, col):
    if row < 0 or col <0:
        return None
    try:
        return matrix[row][col]
    except IndexError:
        return None

# Initialize current sum and list of modifiers
curr = 0

modifiers = [
    [-1, 0], # check up
    [0, 1], # check right
    [1, 0], # check down
    [0, -1], # check left
    [1, -1], # check diagnonal up left
    [1, 1], # check diagonal up right
    [-1, 1], # check diagonal down right
    [-1, -1] # check diagonal down left
]


# Iterate through all items in matrix to find starting point "X"
for row_index, row in enumerate(matrix):
    for column_index, letter in enumerate(row):
        if letter == "X":
            # check all availible directions for the letter "M"
            for modifier in modifiers:
                if get_value(row_index + modifier[0], column_index + modifier[1]) == "M":
                    if get_value(row_index + modifier[0] * 2, column_index + modifier[1] * 2) == "A":
                        if get_value(row_index + modifier[0] * 3, column_index + modifier[1] * 3) == "S":
                            # print(f"Found XMAS starting at X({row_index},{column_index}) going in direction {modifier}")
                            curr += 1

print(curr)


