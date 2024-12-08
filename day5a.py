# new pages for the safety manuals must be printed in a very specific order

# The notation X|Y means that if both page number X and page number Y are to be produced as part of an update
# page number X must be printed at some point before page number Y.

# start by identifying which updates are already in the right order.

# add up the middle page number from those correctly-ordered updates

file_path = 'rob.txt'

rules = []
updates = []
x_before_y = {}
x_after_y = {}
correct_updates = []
correct_updates_middle_numbers_sum = 0

def convert_rule(s):
    numbers = s.split('|')
    return [int(numbers[0]), int(numbers[1])]

def convert_update(s):
    return [int(x) for x in s.split(',')]

def parse_input():
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
      print(f"File not found: {file_path}")
      exit()

def print_parsed_input():
  print(f"{len(rules)} rules:")
  for rule in rules:
    print(rule)

  print(f"{len(updates)} updates:")
  for update in updates:
    print(update)

parse_input()

# print_parsed_input()

# create dictionary of all rules that apply to each page

def create_maps():
    # Dictionary: each key is a page number, value is list of pages that must come BEFORE it
    global x_before_y
    for rule in rules:
        before_page = rule[0]  # page that must come before
        after_page = rule[1]   # page that must come after

        if before_page not in x_before_y:
            x_before_y[before_page] = [after_page]
        else:
            x_before_y[before_page].append(after_page)
            x_before_y[before_page].sort()
    x_before_y = dict(sorted(x_before_y.items()))

    # Dictionary: each key is a page number, value is list of pages that must come AFTER it
    global x_after_y
    for rule in rules:
        before_page = rule[0]  # page that must come before
        after_page = rule[1]   # page that must come after

        if after_page not in x_after_y:
            x_after_y[after_page] = [before_page]
        else:
            x_after_y[after_page].append(before_page)
            x_after_y[after_page].sort()
    x_after_y = dict(sorted(x_after_y.items()))

def print_maps():
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

# print_maps()

# check which updates are already in the right order
def check_updates():
    for update in updates:
        # print(f"Checking update: {update}")
        correct = True
        for i, page in enumerate(update):
            # print(f"Checking page {page}")
            page_rules = x_after_y.get(page, [])
            for page in update[i+1:]:
                if page in page_rules:
                    correct = False
                    # print(f"rule broken, status updated to: {correct}")
        if correct:
            # print(f"Update: {update} is correct")
            correct_updates.append(update)

check_updates()

def sum_middle_numbers():
    global correct_updates_middle_numbers_sum
    for update in correct_updates:
        middle_num_index = ((len(update)) - 1) // 2
        middle_num = update[middle_num_index]
        correct_updates_middle_numbers_sum += middle_num
    print(f" sum of correct updates middle number is:{correct_updates_middle_numbers_sum}")

sum_middle_numbers()