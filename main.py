# two pointer solution (previously 10 second runtime)

# define function to read first line of text file
def read_dense_disk_map(file_path):
    with open(file_path, 'r') as file:
        content = file.readline()
    return content

# define function to convert dense disk map to verbose disk map
def convert_format(dense_disk_map):
    file = True
    id_num = 0
    verbose_disk_map = []
    for char in dense_disk_map:
        if file:
            for i in range(int(char)):
                verbose_disk_map.append(id_num)
            file = False
            id_num += 1
        else: # free space
            for i in range(int(char)):
                verbose_disk_map.append(".")
            file = True
    return verbose_disk_map

# define function to convert the verbose disk map to a compact disk map
def compact_format(verbose_disk_map):
    compact_disk_map = verbose_disk_map.copy()
    i = len(compact_disk_map) - 1

    while i > 0:
        if compact_disk_map[i] != '.':
            # Find the start of this block by going backwards
            block_start = i
            while block_start > 0 and compact_disk_map[block_start - 1] == compact_disk_map[i]:
                block_start -= 1

            block_size = i - block_start + 1

            # Find the leftmost sequence of free spaces that can fit this block
            best_space = -1
            for j in range(block_start):
                if compact_disk_map[j] == '.':
                    # Check if we have enough consecutive spaces
                    space_count = 0
                    for k in range(j, min(j + block_size, block_start)):
                        if compact_disk_map[k] == '.':
                            space_count += 1
                        else:
                            break
                    if space_count >= block_size:
                        best_space = j
                        break

            if best_space != -1:
                # Store the block to move
                block_to_move = compact_disk_map[block_start:i + 1]

                # Fill the destination with the block
                compact_disk_map[best_space:best_space + block_size] = block_to_move

                # Fill the original location with dots
                for j in range(block_start, i + 1):
                    compact_disk_map[j] = '.'

                # Move i to the end of the next potential block
                i = block_start - 1
            else:
                i -= 1
        else:
            i -= 1

    return compact_disk_map

# define function to calculate compact disk map checksum
def calculate_checksum(compact_disk_map):
    checksum = 0
    for index, file_id in enumerate(compact_disk_map):
        if file_id != ".":
            checksum += (index * file_id)
    return checksum

dense_disk_map = read_dense_disk_map('rob.txt')
print("dense_disk_map:", dense_disk_map)

verbose_map = convert_format(dense_disk_map)
print("verbose_disk_map:", ''.join(map(str, verbose_map)))

compact_map = compact_format(verbose_map)
print("compact_disk_map:", ''.join(map(str, compact_map)))

checksum = calculate_checksum(compact_map)
print("checksum:", checksum)