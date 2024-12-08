def file_to_matrix(file_path):
    """
    Reads a file and converts it into a matrix of integers.
    Each line in the file becomes a row in the matrix.
    """
    matrix = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue
                try:
                    # Convert line to list of integers
                    row = list(map(int, line.strip().split()))
                    matrix.append(row)
                except ValueError:
                    print(f"Invalid line in file: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()
    return matrix

def brute_force(matrix):
  count = 0
  for row in matrix:
    agood = False

    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]
        if modified_row != sorted(modified_row) and modified_row != sorted(modified_row, reverse=True):
            continue

        modified_row.sort()
        good = True

        for x, y in zip(modified_row, modified_row[1:]):
            if not(1 <= abs( x - y ) <= 3):
                good = False

        if good:
            agood = True

    if agood:
        count += 1

  return count





# Usage
file_path = 'rob.txt'
matrix = file_to_matrix(file_path)
counter = brute_force(matrix)
print(f"Number of Safe Rows: {counter}")