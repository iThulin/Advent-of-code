file = open('day1.txt', 'r')
#print(data.read())

#elves = []
elf_number = 0

data = file.read()
elves = data.split()

file.close()
"""
with open('day1.txt', 'r') as data:
    for line in data:
        #print(line)
        if line.strip():
            #elves[elf_number].append(list)
            print(line)
        else: 
            print("Line break")
            #elf_number += 1
            continue
"""
print(elves)