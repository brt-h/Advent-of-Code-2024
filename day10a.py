# A hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step.
# Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).
# A trailhead is any position that starts one or more hiking trails - here, these positions will always have height 0.
# A trailhead's score is the number of 9-height positions reachable from that trailhead via a hiking trail.

# test case:
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732

# test case information:
# 9 trailheads
# trailhead scores 5, 6, 5, 3, 1, 3, 5, 3, 5
# sum of all scores is 36

def read_matrix(file_path):
  """
  Reads and parses the topographic map into a 2D list.
  '0' represents trailheads, '9' represents peaks
  """
  try:
      with open(file_path, 'r') as file:
          return [list(line.strip()) for line in file if line.strip()]
  except FileNotFoundError:
      print(f"File not found: {file_path}")
      exit()

def print_map(map):
  for row in map:
      print(''.join(row))

def get_value(map, x, y):
  if x < 0 or y < 0:
      return None
  try:
      return map[y][x]
  except IndexError:
      return None

def find_trailheads(map):
  trailheads = []
  for y_index, row in enumerate(map):
      for x_index, column in enumerate(row):
          if column == "0":
            trailheads.append([x_index, y_index])
  if trailheads != []:
    return trailheads
  raise Exception("No trailheads found")

def get_availible_steps(map, current_x, current_y, current_elevation):
  availible_steps = []
  required_elevation = str(current_elevation + 1)
  for direction in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
    next_x = current_x + direction[0]
    next_y = current_y + direction[1]
    elevation = get_value(map, next_x, next_y)
    if elevation == required_elevation:
      availible_steps.append([next_x, next_y])
  return availible_steps

def find_accessible_peaks(map, trailhead_x, trailhead_y):
  peaks = []

  # current elevation starts at 0
  current_elevation = 0

  # current locations to evaluate starts with just the trailhead
  # TODO change this to a set for perfromance efficiency?
  locations_to_evaluate = [[trailhead_x, trailhead_y]]

  while current_elevation < 9:
    # find all availible steps
    new_locations_to_evaluate = []

    # find all availible steps for current elevation
    for location in locations_to_evaluate:

      # find all availible steps for current location being evaluated
      availible_steps = get_availible_steps(map, location[0], location[1], current_elevation)

      # add all availible steps to new locations to evaluate
      for step in availible_steps:
        # check if step is already in new locations to evaluate
        if step not in new_locations_to_evaluate:
          new_locations_to_evaluate.append(step)

    # update locations to evaluate
    locations_to_evaluate = new_locations_to_evaluate

    # update current elevation
    current_elevation += 1

  # once current_elevation = 9 return peaks
  peaks = locations_to_evaluate
  return peaks

def score_trailhead(map, trailhead_x, trailhead_y):
  peaks = find_accessible_peaks(map, trailhead_x, trailhead_y)
  return len(peaks)

def sum_trailhead_scores(map):
  trailheads = find_trailheads(map)
  trailhead_scores = []
  for trailhead in trailheads:
    trailhead_scores.append(score_trailhead(map, trailhead[0], trailhead[1]))
  return sum(trailhead_scores)

def main():
  file_path = 'rob.txt'
  map = read_matrix(file_path)
  sum = sum_trailhead_scores(map)
  print(f"Sum of trailhead scores: {sum}")

main()