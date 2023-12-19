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
#submit(my_answer_a, part="a", day=Day, year=Year)
# CORRECT

# --- Part Two --- 

# Find first and last digit for each line.
# Digits may be words, i.e. 8 could be 'eight'


# Digits may be used to create other digits, i.e. oneight -> 18
# to prevent this we must preserve the edges of our numbers when replacing the digits.
number_replace = {'zero': 'z0ro',
            'one': 'o1e',
            'two': 't2o',
            'three': 'th3ee',
            'four': 'f4ur',
            'five': 'f5ve',
            'six': 's6x',
            'seven': 'se7en',
            'eight': 'ei8ht',
            'nine': 'n9ne'}

def replace_words(text):
    for k, v in number_replace.items():
        text = text.replace(k,v)
    return text

# Replace all the spelled out numbers with our replacement numbers
replaced_data = replace_words(data)
replaced_input = replaced_data.splitlines()

# Run the code from part 1 to get the numbers
sum = 0
for line in replaced_input: # loop through all lines
    nums = []
    for letter in line: # loop through each character
        if letter.isnumeric():
            nums.append(letter)
    # Sum the digits and return the value
    sum += int(nums[0] + nums[-1])

    #print(f"Nums: {nums}")
    #print(f"Sum: {sum}")

my_answer_b = sum
print(f"Answer_b: {my_answer_b}")

# Submit answers

#submit(my_answer_b, part="b", day=Day, year=Year)
# CORRECT