# For 75 blinks the time required to process the part 1 solution began approaching infinity.
# Two effcicienties have been added to the part 1 solution to acheive a runtime of 133ms:
# 1. The number of stones in a given snap is never counted, and instead added up as the last snap is processed
# 2. The order of the stones is disregarded allowing the state of the stones to be stored as a dictionary,
#    as a result each number in the state only needs to be processed once.

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
# How many stones will you have after blinking 75 times?

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
        map = {}
        content = file.readline()
        for item in content.split():
            if item in map:
                map[item] += 1
            else:
                map[item] = 1
        return map

# define function to process a given stone represented by a number, and return the new stone(s), and the number of stones
def process_stone(number):
  # cast the number to an integer as default
  number = int(number)
  # instantiate the number of stones
  stones_count = 1
  # check first rule, which applies when the number is 0
  if number == 0:
    return [1], stones_count # 1 stone
  # check second rule, which applies when the number has an even number of digits
  elif len(str(number)) % 2 == 0:
    left = int(str(number)[:len(str(number)) // 2])
    right = int(str(number)[len(str(number)) // 2:])
    return [left, right], stones_count + 1 # 2 stones
  # check third rule, which applies when none of the other rules apply
  else:
    return [number * 2024], stones_count # 1 stone

# define a function to process 1 blink for all stones, and return the processed list of all stones
def process_blink(stones_map):
  new_stones_map = {}
  blink_stones_count = 0
  # stones map is a dictionary, where the key is the number of the stone, and the value is the number of the stone
  for stone in stones_map:
    # value is the number of occurences of a given stone number in the stones map
    value = stones_map[stone]
    processed, stones_count = process_stone(stone)
    blink_stones_count += (stones_count * value)
    for new_stone in processed:
      new_stones_map[new_stone] = new_stones_map.get(new_stone, 0) + (1 * value)
  return new_stones_map, blink_stones_count

# define a function to process n blinks for all stones, and return a list representing the final state of stones
def process_n_blinks(stones_map, n):
  state_map = stones_map
  last_blink_stones_count = 0
  for i in range(n):
    # print(f"processesing blink number {i + 1}")
    state_map, blink_stones_count = process_blink(state_map)
    if i == (n - 1):
      last_blink_stones_count += blink_stones_count
    # print(f"state after blink {i + 1}: {state_map}")
  return state_map, last_blink_stones_count

def main():
  file_path = 'rob.txt'
  initial_state = read_input(file_path)
  print("initial_state", initial_state)
  final_state, last_blink_stones_count = process_n_blinks(initial_state, 75)
  print(f"Stones after 75 blinks: {last_blink_stones_count}")

main()