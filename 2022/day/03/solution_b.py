total_priority = 0

with open('2022/day/03/input.txt', 'r') as fh:
    while fh:
        priority = 0
        try:
            group_rucksacks = [(next(fh)).rstrip() for x in range(3)]
        except StopIteration as e:
            break
        group_items = {}
        for rucksack in group_rucksacks:
            rucksack_items = set()
            for item in rucksack:
                if item not in rucksack_items:
                    rucksack_items.add(item)
                    if item in group_items:
                        if group_items[item] == 2:
                            if item.islower():
                                priority = ord(item) - ord('a') + 1
                            else:
                                priority = ord(item) - ord('A') + 27
                            break
                        else:
                            group_items[item] += 1
                    else:
                        group_items[item] = 1

        total_priority += priority
        print(group_rucksacks)
        print(group_items)
        print(f'{item}: {priority}')

print(total_priority)