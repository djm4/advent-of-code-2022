fully_overlapping_assignments = 0
partially_overlapping_assignments = 0

with open('2022/day/04/input.txt', 'r') as fh:
    for row in fh:
        assignments = [[int(y) for y in x.split('-')] for x in row.rstrip().split(',')]
        assignments.sort(key=lambda x: x[0])
        if assignments[0][0] == assignments[1][0] or assignments[0][1] >= assignments[1][1]:
            fully_overlapping_assignments += 1
        if not assignments[0][1] < assignments[1][0]:
            partially_overlapping_assignments += 1

print(f'{fully_overlapping_assignments} assignments overlap completely')
print(f'{partially_overlapping_assignments} assignments overlap in part')
