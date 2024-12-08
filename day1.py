def read_numbers(file_path):
  list1 = []
  list2 = []

  with open(file_path, 'r') as file:
      for line in file:
          # Split the line into numbers based on whitespace
          numbers = line.strip().split()
          if len(numbers) == 2:  # Ensure the line has exactly two numbers
              list1.append(int(numbers[0]))  # Add the first number to list1
              list2.append(int(numbers[1]))  # Add the second number to list2

  return list1, list2

# Usage
file_path = 'tk.txt'
list1, list2 = read_numbers(file_path)

def create_frequency_map(arr):
  freq_map = {}
  for element in arr:
      if element in freq_map:
          freq_map[element] += 1  # Increment count if element exists
      else:
          freq_map[element] = 1  # Initialize count if element is new
  return freq_map
  
freq = create_frequency_map(list2)

counter = 0
for element in list1:
  if element in freq:
    counter += element * freq[element]

print(counter)
#list1.sort()
#list2.sort()
#counter = 0
#for i in range(len(list1)):
# counter += abs(list1[i] - list2[i])

#print(counter)
