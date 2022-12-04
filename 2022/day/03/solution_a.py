total_priority = 0

with open('2022/day/03/input.txt', 'r') as fh:
    for row in fh:
        rucksack = row.rstrip()
        compartment_size = len(rucksack) // 2
        compartments = rucksack[:compartment_size], rucksack[compartment_size:]
        contents = set()
        for item in compartments[0]:
            contents.add(item)
        for item in compartments[1]:
            if item in contents:
                if item.islower():
                    priority = ord(item) - ord('a') + 1
                else:
                    priority = ord(item) - ord('A') + 27

        total_priority += priority
        print(f'{item}: {priority}')

print(total_priority)