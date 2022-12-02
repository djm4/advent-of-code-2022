
score = 0

with open('2022/day/02/input.txt', 'r') as fh:
    for row in fh:
        opponent_choice = ord(row[0]) - ord('A')
        your_choice = ord(row[2]) - ord('X')
        result = ((your_choice - opponent_choice) + 1) % 3
        score += (your_choice + 1) + (result * 3)

print(f'Final score: {score}')
