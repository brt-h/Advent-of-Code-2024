# two pointer solution (10 second runtime)

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
    file_size = 1
    for i in range(len(compact_disk_map) - 1, -1, -1):  # loop backwards through string
        if compact_disk_map[i] != '.':
            if compact_disk_map[i] == compact_disk_map[i - 1]:
                file_size += 1
            else:
                swap = compact_disk_map[i-file_size:i]
                swap_location = -1
                opening_size = 1
                for j in range(i):
                    if compact_disk_map[j] == '.':
                        if compact_disk_map[j] == compact_disk_map[j + 1]:
                            opening_size += 1
                        else:
                            swap_location = j
                            break
                if swap_location != -1:
                    compact_disk_map[swap_location:swap_location+opening_size] = swap
                    compact_disk_map[i-file_size:i] = '.'
                    file_size = 1
                    opening_size = 1
    return compact_disk_map

# define function to calculate compact disk map checksum
def calculate_checksum(compact_disk_map):
    checksum = 0
    for index, file_id in enumerate(compact_disk_map):
        if file_id != ".":
            checksum += (index * file_id)
    return checksum

dense_disk_map = read_dense_disk_map('rob.txt')

print("dense_disk_map: ", dense_disk_map)

verbose_disk_map = convert_format(dense_disk_map)

print("verbose_disk_map: ", verbose_disk_map)

compact_disk_map = compact_format(verbose_disk_map)

print("compact_disk_map: ", compact_disk_map)

checksum = calculate_checksum(compact_disk_map)

print("checksum: ", checksum)