# The stones are in a perfectly straight line.
# Each stone has a number engraved on it.
# Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:
# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
#   The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
#   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# - If none of the other rules apply, the stone is replaced by a new stone;
#   the old stone's number multiplied by 2024 is engraved on the new stone.
# No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.
# How many stones will you have after blinking 25 times?

# test case:
# Initial arrangement:
# 125 17
# After 1 blink:
# 253000 1 7
# After 2 blinks:
# 253 0 2024 14168
# After 3 blinks:
# 512072 1 20 24 28676032
# After 4 blinks:
# 512 72 2024 2 0 2 4 2867 6032
# After 5 blinks:
# 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
# After 6 blinks:
# 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
# (22 total stones)
# after 25 blinks:
# (55312)

# define function to read first line of text file, and return space separated list of numbers
def read_input(file_path):
    with open(file_path, 'r') as file:
      content = file.readline()
      return content.split()

# define function to process a given stone represented by a number, and return the new stone(s)
def process_stone(number):
  # cast the number to an integer as default
  number = int(number)
  # check first rule, which applies when the number is 0
  if number == 0:
    return 1
  # check second rule, which applies when the number has an even number of digits
  elif len(str(number)) % 2 == 0:
    left = int(str(number)[:len(str(number)) // 2])
    right = int(str(number)[len(str(number)) // 2:])
    return [left, right]
  # check third rule, which applies when none of the other rules apply
  else:
    return number * 2024

# define a function to process 1 blink for all stones, and return the processed list of all stones
def process_blink(stones):
  new_stones = []
  for stone in stones:
    processed = process_stone(stone)
    if isinstance(processed, list):
      new_stones.extend(processed)
    else:
      new_stones.append(processed)
  return new_stones

# define a function to process n blinks for all stones, and return a list representing the final state of stones
def process_n_blinks(stones, n):
  state = stones
  for i in range(n):
    print(f"processesing blink number {i + 1}")
    state = process_blink(state)
    # print(f"state after blink {i + 1}: {state}")
  return state

def main():
  file_path = 'rob.txt'
  initial_state = read_input(file_path)
  print("initial_state", initial_state)
  final_state = process_n_blinks(initial_state, 25)
  stones_after_25_blinks = len(final_state)
  print(f"Stones after 25 blinks: {stones_after_25_blinks}")

main()