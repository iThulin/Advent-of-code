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
    # Separate each game into a list containing tuples of each result
    master_list = []
    false_list = []
    for line in input_a:

        # Split game_id and game_results list
        game_id = int(line.split(":")[0].split(" ")[1])
        game_result = line.split(":")[1].split(";")

        print(f"Game_id: {game_id} {game_result}\n")
    
        # Split results into Red, Blue, and Green results
        for game in game_result:
            grab = [x.strip() for x in game.split(",")]

            for pull in grab:
                split_text = pull.split(' ', 1)
                num = int(split_text[0])
                color = split_text[1]

                match color:
                    case 'red':
                        if num > 12:
                            if game_id not in false_list:
                                false_list.append(game_id)
                    case 'green':
                        if num > 13:
                            if game_id not in false_list:
                                false_list.append(game_id)
                    case 'blue':
                        if num > 14:
                            if game_id not in false_list:
                                false_list.append(game_id)
        master_list.append(int(game_id))
                
    print(f"Master sum: {sum(master_list)} {master_list}\n")
    print(f"False sum: {sum(false_list)} {false_list}")

    answer_a = sum(master_list) - sum(false_list)
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
#submit(my_answer_b, part="a", day=Day, year=Year)
