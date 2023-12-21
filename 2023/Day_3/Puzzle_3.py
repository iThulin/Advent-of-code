from aocd import submit

# Parameters
Year = 2023
Day = 3
path = str(Year) + '/Day_' + str(Day) + '/data.txt'

# Open & Manipulate Data
with open(path) as data_file:
    data = data_file.read()
    input_a = data.splitlines()
    input_b = input_a

# --- Part One ---
def part_a(input_a):
 
    # Greedy nearest neighbors algorithm.
    # 1. Find a symbol
    # 2. look for a digit in surrounding directions
    # 3. If number is found, scan horizontally for full number
    # 4. Add number to the sum and continue search

    array = []

    for line in input_a:
        row = []
        for character in line:
            if character == '.':
                row.append('')
            else:
                row.append(character)
        array.append(row)

    for i in range(len(array)):
        print(array[i])


    return answer_a

# --- Part Two --- 

def part_b(input_b):

    return answer_b

# --- SUBMIT ANSWERS ---

answer_a = part_a(input_a)
print(f"Answer_a: {answer_a}")
#submit(my_answer_a, part="a", day=Day, year=Year)

answer_b = part_b(input_b)
print(f"Answer_b: {answer_b}")
#submit(my_answer_b, part="b", day=Day, year=Year)
