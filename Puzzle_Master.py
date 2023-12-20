from aocd import submit

# Parameters
Year = 2023
Day = 2
path = str(Year) + '/Day_' + str(Day) + '/data.txt'

# Open & Manipulate Data
with open(path) as data_file:
    data = data_file.read()
    input_a = data.splitlines()
    input_b = input_a

# --- Part One ---
def part_a(input_a):
 
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
