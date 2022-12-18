# Day 1
elves = []
calories = []

with open('day1.txt', 'r') as data:
    sub_list = []
    for line in data:
        #print(line)
        if line.strip():
            #elves[elf_number].append(list)
            sub_list.append(int(line.strip()))
        else: 
            # If line is empty push the sublist and reset it
            elves.append(sub_list)
            sub_list = []
            continue

for i in range(len(elves)):
    sum = 0
    for item in elves[i]:
        sum += item
    calories.append(sum)

print(calories)