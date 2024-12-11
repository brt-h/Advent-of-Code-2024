def read_matrix(file_path):
  """
  Reads and parses the maze file into a 2D list.
  '^' represents guard, '#' represents obstacles, '.' represents empty space
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

def find_guard(matrix):
  for y_index, row in enumerate(matrix):
      for x_index, column in enumerate(row):
          if column == "^":
              return [x_index, y_index]
  raise Exception("No guard found")

def get_next_position(position, facing):
  modifiers = [
      [0, -1],  # Move up
      [1, 0],   # Move right
      [0, 1],   # Move down
      [-1, 0],  # Move left
  ]
  return [
      position[0] + modifiers[facing][0],
      position[1] + modifiers[facing][1]
  ]

def move_guard(matrix, position, facing):
  """
  Moves the guard based on current position and facing direction.
  Returns new matrix state, new position, and new facing direction.
  """
  proposed_pos = get_next_position(position, facing)
  proposed_tile = get_value(matrix, proposed_pos[0], proposed_pos[1])

  new_matrix = [row[:] for row in matrix]
  new_position = position
  new_facing = facing

  if proposed_tile == "#":
      new_facing = (facing + 1) % 4  # Turn right when hitting obstacle
  elif proposed_tile in ["^", "."]:
      new_position = proposed_pos
      new_matrix[proposed_pos[1]][proposed_pos[0]] = "X"  # Mark visited position
  elif proposed_tile == "X":
      new_position = proposed_pos  # Move to already visited position
  elif proposed_tile is None:
      return new_matrix, None, new_facing  # Guard exits the maze

  return new_matrix, new_position, new_facing

def simulate_guard_path(matrix, start_position, obstacle_pos):
  # Use a more efficient matrix representation - only track visited positions
  visited = set()
  position = start_position
  facing = 0
  state_history = {}  # Maps (x,y,facing) to step number
  step = 0

  # Create efficient bounds checking
  height, width = len(matrix), len(matrix[0])

  def is_valid_pos(x, y):
      return 0 <= x < width and 0 <= y < height

  def get_cell(x, y):
      return '#' if (x == obstacle_pos[0] and y == obstacle_pos[1]) else matrix[y][x]

  while position is not None:
      x, y = position
      if not is_valid_pos(x, y):
          return False

      state = (x, y, facing)
      if state in state_history:
          return True

      state_history[state] = step
      visited.add((x, y))

      # Calculate next position
      next_x = x + [0, 1, 0, -1][facing]
      next_y = y + [-1, 0, 1, 0][facing]

      if not is_valid_pos(next_x, next_y):
          position = None
      else:
          cell = get_cell(next_x, next_y)
          if cell == '#':
              facing = (facing + 1) % 4
          else:
              position = [next_x, next_y]

      step += 1
  return False

def count_valid_obstacles(matrix):
  valid_count = 0
  start_position = find_guard(matrix)

  for y in range(len(matrix)):
      for x in range(len(matrix[0])):
          if matrix[y][x] == ".":
              if simulate_guard_path(matrix, start_position, [x, y]):
                  valid_count += 1

  return valid_count


matrix = read_matrix('rob.txt')
valid_locations = count_valid_obstacles(matrix)
print(f"Number of valid obstacle locations: {valid_locations}")