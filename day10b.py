# A hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step.
# Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).
# A trailhead is any position that starts one or more hiking trails - here, these positions will always have height 0.
# A trailhead's rating is the number of distinct hiking trails which begin at that trailhead

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
# trailhead ratings 20, 24, 10, 4, 1, 4, 5, 8, 5
# sum of all ratings is 81

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

def find_distinct_paths_to_a_peak(map, trailhead_x, trailhead_y):
  # at elevation 0 number of distinct paths starts at 1, the trailhead
  paths = 1
  print("Starting at trailhead, paths: ", paths)

  # current elevation starts at 0'
  current_elevation = 0

  # current locations to evaluate starts with just the trailhead
  locations_to_evaluate = [[trailhead_x, trailhead_y]]

  while current_elevation < 9:

    # find all availible steps
    new_locations_to_evaluate = []

    # find all availible steps for current elevation
    for location in locations_to_evaluate:

      # find all availible steps for current location being evaluated
      availible_steps = get_availible_steps(map, location[0], location[1], current_elevation)

      # adjust number of paths based on number of availible steps
      num_availible_steps = len(availible_steps)
      if num_availible_steps == 0:
        # if current path is a dead end subtract one from paths
        paths -= 1
        print(f"----0 paths found for location: {location} number of paths reduced by 1 to {paths}")
      else:
        # if current path leads to more than 1 path, add the extras to paths
        paths += (num_availible_steps - 1)
        print(f"----{num_availible_steps} paths found for location: {location} number of paths increased by {num_availible_steps - 1} to {paths}")

      # add all availible steps to new locations to evaluate
      for step in availible_steps:
        new_locations_to_evaluate.append(step)

    # update locations to evaluate
    locations_to_evaluate = new_locations_to_evaluate

    # update current elevation
    current_elevation += 1
    print("--Updating current elevation to ", current_elevation)

  # once current_elevation = 9 return paths
  return paths

def find_accessible_peaks(map, trailhead_x, trailhead_y):
  peaks = []

  # current elevation starts at 0
  current_elevation = 0

  # current locations to evaluate starts with just the trailhead
  # TODO change this to a set for performance efficiency?
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
  paths = find_distinct_paths_to_a_peak(map, trailhead_x, trailhead_y)
  print(f"trailhead at {trailhead_x}, {trailhead_y} has {paths} paths")
  return paths

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