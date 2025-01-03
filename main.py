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
    
    # Process each file ID from highest to lowest
    for id_num in range(8, -1, -1):
        # Find all blocks for this ID
        blocks = []
        i = len(compact_disk_map) - 1
        while i >= 0:
            if isinstance(compact_disk_map[i], (int, float)) and int(compact_disk_map[i]) == id_num:
                end = i
                start = i
                while i > 0 and isinstance(compact_disk_map[i-1], (int, float)) and int(compact_disk_map[i-1]) == id_num:
                    i -= 1
                    start = i
                blocks.append((start, end))
                i -= 1
            else:
                i -= 1
                
        if not blocks:
            continue
            
        # Calculate total size needed
        total_size = sum(end - start + 1 for start, end in blocks)
        
        # Find leftmost position with enough consecutive spaces
        best_pos = -1
        for pos in range(len(compact_disk_map)):    
            if pos > blocks[0][0]:  # Don't look beyond current position
                break
            count = 0
            valid = True
            for j in range(pos, min(pos + total_size, len(compact_disk_map))):
                if compact_disk_map[j] == '.':
                    count += 1
                else:
                    valid = False
                    break
            if valid and count >= total_size:
                best_pos = pos
                break
                
        # If we found a valid position, move all blocks
        if best_pos != -1:
            # Clear original positions first
            for start, end in blocks:
                for i in range(start, end + 1):
                    compact_disk_map[i] = '.'
            
            # Place blocks in new position
            curr_pos = best_pos
            for start, end in blocks:
                block_size = end - start + 1
                for i in range(block_size):
                    compact_disk_map[curr_pos + i] = id_num
                curr_pos += block_size
            # TODO delete this print
            print("compact_disk_map:", ''.join(map(str, compact_disk_map)))
    
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
print("verbose_disk_map:", verbose_map)

compact_map = compact_format(verbose_map)
print("compact_disk_map:", ''.join(map(str, compact_map)))

checksum = calculate_checksum(compact_map)
print("checksum:", checksum)