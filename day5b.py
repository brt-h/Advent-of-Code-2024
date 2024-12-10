# New pages for the safety manuals must be printed in a very specific order

# The notation X|Y means that if both page number X and page number Y are to be produced as part of an update,
# page number X must be printed at some point before page number Y.

# Now identify which updates are in the wrong order.
# Then, fix those updates and sum up the middle page number from the previously incorrectly-ordered updates.

file_path = 'rob.txt'

rules = []  # List to store the rules
updates = []  # List to store the updates
x_before_y = {}  # Dictionary to store pages that must precede other pages
x_after_y = {}  # Dictionary to store pages that must come after other pages
incorrect_updates = []  # List of updates that are in the incorrect order
corrected_updates = [] # Corrected list of updates that were in the incorrect order
incorrect_updates_middle_numbers_sum = 0  # Variable to store the sum of middle numbers in incorrect updates

def convert_rule(s):
    """Convert a rule string 'X|Y' into a list of two integers [X, Y]."""
    numbers = s.split('|')
    return [int(numbers[0]), int(numbers[1])]

def convert_update(s):
    """Convert an update string 'X,Y,Z,...' into a list of integers."""
    return [int(x) for x in s.split(',')]

def parse_input():
  """Parse the input file to populate rules and updates lists."""
  reading_rules = True
  try:
      with open(file_path, 'r') as file:
          for line in file:
              line = line.strip()
              if not line:  # Empty line marks transition from rules to updates
                  reading_rules = False
                  continue

              if reading_rules:
                  rules.append(convert_rule(line))
              else:
                  updates.append(convert_update(line))

  except FileNotFoundError:
      print(f"File not found: {file_path}")  # Error message for missing file
      exit()

def print_parsed_input():
  """Print the parsed rules and updates for verification."""
  print(f"{len(rules)} rules:")
  for rule in rules:
    print(rule)

  print(f"{len(updates)} updates:")
  for update in updates:
    print(update)

parse_input()

# print_parsed_input()  # Uncomment to debug parsed input

# Create dictionary of all rules that apply to each page

def create_maps():
    """Create the mappings of page dependencies with two dictionaries: before and after."""
    # Dictionary: each key is a page number, value is list of pages that must come BEFORE it
    global x_before_y
    for rule in rules:
        before_page = rule[0]  # page that must come before
        after_page = rule[1]   # page that must come after

        if before_page not in x_before_y:
            x_before_y[before_page] = [after_page]
        else:
            x_before_y[before_page].append(after_page)
            x_before_y[before_page].sort()  # Keep the list sorted
    x_before_y = dict(sorted(x_before_y.items()))  # Sort dictionary by key

    # Dictionary: each key is a page number, value is list of pages that must come AFTER it
    global x_after_y
    for rule in rules:
        before_page = rule[0]  # page that must come before
        after_page = rule[1]   # page that must come after

        if after_page not in x_after_y:
            x_after_y[after_page] = [before_page]
        else:
            x_after_y[after_page].append(before_page)
            x_after_y[after_page].sort()  # Keep the list sorted
    x_after_y = dict(sorted(x_after_y.items()))  # Sort dictionary by key

def print_maps():
    """Print the x_before_y and x_after_y maps for verification."""
    # Ensure the maps are created before printing
    if not x_before_y or not x_after_y:
        create_maps()

    print("x_before_y:")
    for key in x_before_y:
        print(f"{key}: {x_before_y[key]}")

    print("x_after_y:")
    for key in x_after_y:
        print(f"{key}: {x_after_y[key]}")

create_maps()

# print_maps()  # Uncomment to debug the maps

# Check which updates are already in the right order
def check_updates():
    """Identify updates that are in the incorrect order based on defined page rules."""
    for update in updates:
        correct = True
        for i, page in enumerate(update):
            page_rules = x_after_y.get(page, [])
            for page in update[i+1:]:
                if page in page_rules:
                    correct = False
        if not correct:
            incorrect_updates.append(update)

check_updates()

def find_first_number(update):
    # [75, 97, 47, 61, 53]
    for i, page in enumerate(update):
        # 0, 97
        page_rules = x_after_y.get(page, [])
        # []
        first_page = True
        for rule in page_rules:
            if rule in update:
                first_page = False
        if first_page:
            return page

def fix_incorrect_updates():
    for update in incorrect_updates:
        remaining_pages = update.copy()
        corrected_update = []
        while len(remaining_pages) > 0:
            first_number = find_first_number(remaining_pages)
            remaining_pages.remove(first_number)
            corrected_update.append(first_number)
        corrected_updates.append(corrected_update)

fix_incorrect_updates()

def sum_middle_numbers():
    """Sum the middle numbers from updates that are in the correct order."""
    global incorrect_updates_middle_numbers_sum
    for update in corrected_updates:
        middle_num_index = ((len(update)) - 1) // 2
        middle_num = update[middle_num_index]
        incorrect_updates_middle_numbers_sum += middle_num
    print(f" sum of incorrect updates middle number is: {incorrect_updates_middle_numbers_sum}")

sum_middle_numbers()