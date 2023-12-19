from aocd import submit

# Parameters
Year = 2023
Day = 1
path = str(Year) + '/Day_' + str(Day) + '/data.txt'
my_answer = ''

# Open & Manipulate Data
with open(path) as data_file:
    data = data_file.read()
    #print(data)
    input_list = data.splitlines()
    #print(lines)


# --- Part One ---

# Find first and last digit for each line.
sum = 0
for line in input_list: # loop through all lines
    nums = []
    for letter in line: # loop through each character
        if letter.isnumeric():
            nums.append(letter)
    # Sum the digits and return the value
    sum += int(nums[0] + nums[-1])

    #print(f"Nums: {nums}")
    #print(f"Sum: {sum}")

my_answer_a = sum
print(f"Answer_a: {my_answer_a}")

# Submit answers
submit(my_answer_a, part="a", day=Day, year=Year)
# CORRECT

# --- Part Two ---



#submit(my_answer_b, part="b", day=Day, year=Year)