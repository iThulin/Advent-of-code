from aocd import submit

# Parameters
Year = 2023
Day = 2
path = str(Year) + '/Day_' + str(Day) + '/data.txt'
my_answer = ''

# Open & Manipulate Data
with open(path) as data_file:
    data = data_file.read()
    #print(data)
    input_a = data.splitlines()
    #print(lines)


# --- Part One ---

my_answer_a = sum
print(f"Answer_a: {my_answer_a}")

# Submit answers

#submit(my_answer_a, part="a", day=Day, year=Year)


# --- Part Two --- 

# Create Data
input_b = data.splitlines()

my_answer_b = ""
print(f"Answer_b: {my_answer_b}")

# Submit answers

#submit(my_answer_b, part="b", day=Day, year=Year)
