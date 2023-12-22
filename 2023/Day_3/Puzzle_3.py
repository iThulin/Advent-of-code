from aocd import submit
import re

# Parameters
Year = 2023
Day = 3
path = str(Year) + '/Day_' + str(Day) + '/data.txt'

# Open & Manipulate Data
with open(path) as data_file:
    data = data_file.read()
    input_a = data.splitlines()
    input_b = input_a

# Helper Functions
def is_symbol(text):
    return bool(re.match(r'^[\W_]+$', text))

def search_neighbors(array, row, col):
    neighbors = []
    domain_x = len(array)
    domain_y = len(array[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),(0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dir_r, dir_c in directions:
        new_row, new_col = row + dir_r, col + dir_c

        # Check if the new address is in the domain
        if 0 <= new_row < domain_x and 0 <= new_col < domain_y:
            neighbors.append((array[new_row][new_col], new_row, new_col))

    print(f"neighbors: {neighbors}")
    return neighbors

def trim_neighbors(neighbors):
    trim_neighbors = []
    upper, middle, lower = neighbors[:3], neighbors[3:5], neighbors[5:]
    print(f" upper: {upper}\n middle: {middle}\n lower: {lower}")

    #I will brute force this interaction
    if upper[0][0].isnumeric():
        trim_neighbors.append(upper[0])
    if upper[1][0].isnumeric() and upper[0] not in trim_neighbors:
        trim_neighbors.append(upper[1])
    if upper[2][0].isnumeric() and upper[1] not in trim_neighbors:
        if upper[1][0].isnumeric() == False:
            trim_neighbors.append(upper[2])

    if middle[0][0].isnumeric():
        trim_neighbors.append(middle[0])
    if middle[1][0].isnumeric():
        trim_neighbors.append(middle[1])

    if lower[0][0].isnumeric():
        trim_neighbors.append(lower[0])
    if lower[1][0].isnumeric() and lower[0] not in trim_neighbors:
        trim_neighbors.append(lower[1])
    if lower[2][0].isnumeric() and lower[1] not in trim_neighbors:
        if lower[1][0].isnumeric() == False:
            trim_neighbors.append(lower[2])

    print(f"Trimmed: {trim_neighbors}")
    return trim_neighbors


def scan_neighbors(array, row, col):
    num_list = []
    domain_x = len(array[0])
    pointer = col

    print(f"row: {row}, col: {col}")
    # Scan to the start of a number
    print(f"Start scan at: {array[row][pointer]}")
    while array[row][pointer - 1].isnumeric() and 0 <= pointer - 1:
        pointer -= 1

    while array[row][pointer].isnumeric():
        num_list.append(array[row][pointer])
        print(f" Appending: {array[row][pointer]}")
        if pointer + 1 < domain_x:
            pointer += 1
        else:
            break

    print(f"num_list: {num_list}")
    result = int("".join(num_list))
    print(result)
    return result
'''   

# --- Part One ---
def part_a(input_a):
 
    # Greedy nearest neighbors algorithm.
    # 1. Find a symbol
    # 2. look for a digit in surrounding directions
    # 3. If number is found, scan horizontally for full number
    # 4. Add number to the sum and continue search

    array = []
    part_sum = 0

    for line in input_b:
        row = []
        for character in line:
            if character == '.':
                row.append('')
            else:
                row.append(character)
        array.append(row)

    for row_num, row in enumerate(array):
        #print(row)
        for index, string_val in enumerate(array[row_num]):
            # 1. Find a symbol
            if is_symbol(string_val):
                print(f"{string_val} at Row, index {row_num},{index}")
                # 2. Look for a digit in surrounding directions.
                neighbors = search_neighbors(array, row=row_num, col=index)
                trimmed_neighbors = trim_neighbors(neighbors)
                # 3. If number is found, scan horizontally for full number
                for j, item in enumerate(trimmed_neighbors):
                    print(f'found a number: {item}')
                    part_num = scan_neighbors(array, row=trimmed_neighbors[j][1] , col=trimmed_neighbors[j][2] )
                    part_sum += part_num
                    print(f"Adding {part_num} to make sum= {part_sum}\n")
            else:
                #print(f"Row, Index, String: {row_num}, {index}, {string_val}")
                pass


    answer_a = part_sum

    return answer_a
'''
# --- Part Two --- 

def part_b(input_b):

    array = []
    part_sum = 0

    for line in input_b:
        row = []
        for character in line:
            if character == '.':
                row.append('')
            else:
                row.append(character)
        array.append(row)

    for row_num, row in enumerate(array):
        #print(row)
        for index, string_val in enumerate(array[row_num]):
            # 1. Find a symbol
            if string_val == '*':
                print(f"{string_val} at Row, index {row_num},{index}")
                # 2. Look for a digit in surrounding directions.
                neighbors = search_neighbors(array, row=row_num, col=index)
                trimmed_neighbors = trim_neighbors(neighbors)
                # 3. If number is found, scan horizontally for full number
                for j, item in enumerate(trimmed_neighbors):
                    print(f'found a number: {item}')
                    part_num = scan_neighbors(array, row=trimmed_neighbors[j][1] , col=trimmed_neighbors[j][2] )
                    part_sum += part_num
                    print(f"Adding {part_num} to make sum= {part_sum}\n")
            else:
                #print(f"Row, Index, String: {row_num}, {index}, {string_val}")
                pass

# ----------- TO DO -------------
    # adjust  scan_neighbors and trim neighbors to search for "GEARS"
            # Find * surrounded by 2 part numbers
            # Multiply part numbers ("gear_ratio") then sum each gear ration 
            # return gear ratio

    answer_b = part_sum


    answer_b = 'Still learning'
    return answer_b

# --- SUBMIT ANSWERS ---
'''
answer_a = part_a(input_a)
print(f"Answer_a: {answer_a}")
#submit(answer_a, part="a", day=Day, year=Year)

# --- COMPLETE ---
'''
answer_b = part_b(input_b)
print(f"Answer_b: {answer_b}")
#submit(my_answer_b, part="b", day=Day, year=Year)
