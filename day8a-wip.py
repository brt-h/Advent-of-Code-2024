from collections import deque

def read_matrix(file_path):
  """
  Reads and parses the map file into a 2D list.
  Letters and digits represent antennas, '.' represents empty space.
  """
  try:
      with open(file_path, 'r') as file:
          return [list(line.strip()) for line in file if line.strip()]
  except FileNotFoundError:
      print(f"File not found: {file_path}")
      exit()

def print_matrix(matrix):
  for row in matrix:
      print(''.join(row))

def get_value(matrix, x, y):
  if x < 0 or y < 0:
      return None
  try:
      return matrix[y][x]
  except IndexError:
      return None

def get_column(x, matrix):
    return [row[x] for row in matrix]

def get_row(y, matrix):
    return matrix[y]

def get_rising_diagonal(x, y, matrix):
    rising_diagonal = deque()
    start_x, start_y = x, y

    def is_within_bounds(x, y):
        return 0 <= x < len(get_column(0, matrix)) and 0 <= y < len(matrix[0])

    # Traverse up and to the right
    while is_within_bounds(x, y):
        rising_diagonal.append(get_value(matrix, x, y))
        x += 1
        y += 1

    x, y = start_x, start_y

    # Traverse down and to the left
    while is_within_bounds(x, y):
        rising_diagonal.appendleft(get_value(matrix, x, y))
        x -= 1
        y -= 1

    return rising_diagonal

def get_falling_diagonal(x, y, matrix):
    falling_diagonal = deque()
    start_x, start_y = x, y

    def is_within_bounds(x, y):
        return 0 <= x < len(get_column(0, matrix)) and 0 <= y < len(matrix[0])

    # Traverse down and to the right
    while is_within_bounds(x, y):
        falling_diagonal.append(get_value(matrix, x, y))
        x += 1
        y -= 1

    x, y = start_x, start_y

    # Traverse up and to the left
    while is_within_bounds(x, y):
        falling_diagonal.appendleft(get_value(matrix, x, y))
        x -= 1
        y += 1

    return falling_diagonal

def find_antenna_types(matrix):
    antenna_types = set()
    for y_index, row in enumerate(matrix):
        for x_index, column in enumerate(row):
            if column != ".":
                antenna_types.add(column)
    return antenna_types

def check_vertical(x, y, matrix):
    column = get_column(x, matrix)
    print(column)
    pass

def find_antinodes(antenna_type, matrix):
    antinodes = []
    for y_index, row in enumerate(matrix):
        for x_index, column in enumerate(row):
            if 10 == 100:
                pass # check vertical, check horizontal, check diagonal 1, check diagonal 2
                antinodes.append([x_index, y_index])
    return antinodes





matrix = read_matrix('rob.txt')
print_matrix(matrix)
antenna_types = find_antenna_types(matrix)
print(antenna_types)

check_vertical(0,0,matrix)

# valid_locations = count_valid_obstacles(matrix)
# print(f"Number of valid obstacle locations: {valid_locations}")