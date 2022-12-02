
score = 0
# Solution for where the second column indicates the outcome
with open('2022/day/02/input.txt', 'r') as fh:
    for row in fh:
        opponent_choice = ord(row[0]) - ord('A')
        result = ord(row[2]) - ord('X')
        your_choice = ((opponent_choice + result) - 1) % 3
        score += (your_choice + 1) + (result * 3)

print (f'Final score: {score}')