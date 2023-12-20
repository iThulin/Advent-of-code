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

# Separate each game into a list containing tuples of each result
master_list = []
false_list = []
for line in input_a:
    game_list = []

    # Split Game ID
    game_id = line.split(":")[0].split(" ")[1]

    # Split results into separate indices in list
    game_result = line.split(":")[1].split(";")
    #print(game_id)
 
# Split results into Red, Blue, and Green results
    for game in game_result:
        record = []

        grab = [x.strip() for x in game.split(",")]
        #print(grab)

        for pull in grab:
            split_text = pull.split(' ', 1)
            num = int(split_text[0])
            color = split_text[1]
            #num, color = [y.strip() for y in pull.split(" ")[0]], [z.strip() for z in pull.split(" ")[1]]

            record.append((num, color))
            #print(f"Num: {num}, color: {color}")

    # Rebuild the list in the proper arrangment
    game_list.append((game_id, record))
    print(game_list)

    print(f"Test: {game_list[0][1]}")
    for i in range(0, len(game_list[0][1])):
        print(f"2nd Test: {game_list[0][1][i][0]}")

        # game_list[0][1][i][1] = the color of rocks pulled in each game
        # game_list[0][1][i][0] = number of rocks pulled
        match game_list[0][1][i][1]:
            case 'red':
                if game_list[0][1][i][0] > 12:
                    false_list.append(game_list[0][0])
            case 'blue':
                if game_list[0][1][i][0] > 14:
                    false_list.append(game_list[0][0])
            case 'green':
                if game_list[0][1][i][0] > 13:
                    false_list.append(game_list[0][0])

print(f"Master_list: {master_list}")
print(f"False_list: {false_list}")

# Remove any numbers on the false list from the master list.

my_answer_a = ""
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
