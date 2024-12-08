import re

with open('rob.txt', 'r') as file:
    # Read the entire file as a single string
    long_string = file.read().replace('\n', '')

# Define the regex
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches
matches = re.findall(pattern, long_string)

# Initialize the result
curr = 0

# Process all matches
for num1, num2 in matches:
    curr += int(num1) * int(num2)

print(curr)