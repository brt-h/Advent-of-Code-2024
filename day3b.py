import re  

with open('rob.txt', 'r') as file:
    # Read the file and replace newlines with an empty string
    long_string = file.read().replace('\n', '')

# Define regex patterns for the specific operations
do_pattern = r"\bdo\(\)"
dont_pattern = r"\bdon't\(\)"
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Initialize current sum and index pointers
curr = 0
next_do_index = 0
next_dont_index = 0

def get_next_do(start_index, end_index):
    # Search for the 'do()' pattern within the substring
    match = re.search(do_pattern, long_string[start_index:end_index])
    if match != None:
        # Return the end index of the match adjusted by the starting index
        return start_index + match.end()
    return None

def get_next_dont(start_index, end_index):
    # Search for the 'don't()' pattern within the substring
    match = re.search(dont_pattern, long_string[start_index:end_index])
    if match != None:
        # Return the end index of the match adjusted by the starting index
        return start_index + match.end()
    return None

def get_muls(start_index, end_index):
    global curr
    # Find all occurrences of the 'mul()' pattern
    match = re.findall(mul_pattern, long_string[start_index:end_index])
    for num1, num2 in match:
        # Calculate the product and add to the current sum
        curr += int(num1) * int(num2)

# Iterate over the long string based on the defined 'do' and 'don't' patterns
while next_do_index < len(long_string):
    next_dont_index = get_next_dont(next_do_index, len(long_string))

    if next_dont_index is None:
        # Set to end of string if no 'don't()' is found
        next_dont_index = len(long_string)

    # Calculate the sum of products between 'do' and 'don't'
    get_muls(next_do_index, next_dont_index)

    # Move to the next 'do()' occurrence
    next_do_index = get_next_do(next_dont_index, len(long_string))
    if next_do_index is None:
        # Exit loop if no more 'do()' is found
        break

# Print the final calculated sum of products
print(f"Final sum: {curr}")