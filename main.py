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
            current_id = compact_disk_map[i]
            
            # Find all blocks of this file ID
            blocks = []
            temp_i = i
            while temp_i >= 0:
                if compact_disk_map[temp_i] == current_id:
                    block_end = temp_i
                    block_start = temp_i
                    while block_start > 0 and compact_disk_map[block_start - 1] == current_id:
                        block_start -= 1
                    blocks.append((block_start, block_end))
                    temp_i = block_start - 1
                else:
                    temp_i -= 1
            
            total_size = sum(end - start + 1 for start, end in blocks)
            
            # Find leftmost space that can fit all blocks
            best_space = -1
            for j in range(blocks[-1][0]):
                space_count = 0
                consecutive = True
                for k in range(j, min(j + total_size, blocks[-1][0])):
                    if compact_disk_map[k] == '.':
                        space_count += 1
                    else:
                        consecutive = False
                        break
                if consecutive and space_count >= total_size:
                    best_space = j
                    break
            
            if best_space != -1:
                # Move all blocks
                new_pos = best_space
                for start, end in reversed(blocks):
                    size = end - start + 1
                    # Move block
                    for k in range(size):
                        compact_disk_map[new_pos + k] = current_id
                    # Clear original
                    for k in range(start, end + 1):
                        compact_disk_map[k] = '.'
                    new_pos += size
                
                i = blocks[-1][0] - 1
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