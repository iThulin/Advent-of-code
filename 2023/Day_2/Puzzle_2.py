from aocd import submit
from math import prod

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
        # Separate each game into a list containing tuples of each result
    games = []
    games_prod = []
    for line in input_a:
        min_list = [0, 0, 0]

        # Split game_id and game_results list
        game_id = int(line.split(":")[0].split(" ")[1])
        game_result = line.split(":")[1].split(";")

        print(f"\nGame_id: {game_id} {game_result}")
    
        # Split results into Red, Blue, and Green results
        for game in game_result:
            grab = [x.strip() for x in game.split(",")]
            print(f"\nGrab: {grab}")

            for pull in grab:
                split_text = pull.split(' ', 1)
                num = int(split_text[0])
                color = split_text[1]

                match color:
                    case 'red':
                        print(f"red, col: {color, num}, min: {min_list[0]}")
                        if num > min_list[0]:
                            min_list[0] = num
                            print(f"    Updated Red to {min_list[0]}")
                    case 'green':
                        print(f"green, col: {color, num}, min: {min_list[1]}")
                        if num > min_list[1]:
                            min_list[1] = num
                            print(f"    Updated Green to {min_list[1]}")
                    case 'blue':
                        print(f"blue, col: {color, num}, min: {min_list[2]}")
                        if num > min_list[2]:
                            min_list[2] = num
                            print(f"    Updated Blue to {min_list[2]}")
        games.append(min_list)
        games_prod.append(prod(min_list))
                
    print(f"\nPowers: {games}\n")
    print(f"Prods: {games_prod}\n")
    answer_b = sum(games_prod)

    return answer_b

# --- SUBMIT ANSWERS ---
'''
answer_a = part_a(input_a)
print(f"Answer_a: {answer_a}")
submit(my_answer_a, part="a", day=Day, year=Year)
'''
answer_b = part_b(input_b)
print(f"Answer_b: {answer_b}")
submit(answer_b, part="b", day=Day, year=Year)
