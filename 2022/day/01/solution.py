
elf_calories = []
current_elf_calories = 0
maximum_elf_calories = 0

print('Elf calorie bar chart:')
with open('2022/day/01/input_a.txt', 'r') as fh:
    for row in fh:
        # Cheekily, this uses the fact that calling int() onm a blank line throws
        # an exception to find the gaps between elves. It's very Pythonic to
        # do this, I believe.
        try:
            current_elf_calories += int(row)
        except ValueError as e:
            print('*' * int(current_elf_calories/1000))
            maximum_elf_calories = max(current_elf_calories, maximum_elf_calories)
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0

print()

elf_calories.sort(reverse=True)

# How many calories does the most calorie-carrying else carry?
# This solution could use elf_calories[0] instead, but that list
# was only introduced for the second part of the challenge.
print(f'Most calories: {maximum_elf_calories}')

# How many calories do the top three calorie-carrying elves carry?
top_three = elf_calories[0:3]
print(f'Top three calories: {sum(top_three)} ( = {" + ".join([str(x) for x in top_three])})')
