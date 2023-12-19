from aocd import submit

# Parameters
Year = 2023
Day = 1
path = str(Year) + '/Day_' + str(Day) + '/data.txt'
my_answer = ''

# Open & Manipulate Data
with open(path) as data_file:
    data = data_file.read()
    print(data)
    lines = data.splitlines()
    #print(lines)

# Submit answer
#submit(my_answer, part="a", day=Day, year=Year)2023\Day_1\data.txt