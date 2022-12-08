from math import prod

tree_grid = []
row_max_heights = []
col_max_heights = []


def scenic_score(tree_grid, row, col):
    score_parts = [0, 0, 0, 0]
    base_height = tree_grid[row][col]
    check_left = col - 1
    view_clear = True
    while check_left >= 0 and view_clear:
        score_parts[0] += 1
        if tree_grid[row][check_left] < base_height:
            check_left -= 1
        else:
            view_clear = False
    check_right = col + 1
    view_clear = True
    while check_right < len(col_max_heights) and view_clear:
        score_parts[1] += 1
        if tree_grid[row][check_right] < base_height:
            check_right += 1
        else:
            view_clear = False
    check_up = row - 1
    view_clear = True
    while check_up >= 0 and view_clear:
        score_parts[2] += 1
        if tree_grid[check_up][col] < base_height:
            check_up -= 1
        else:
            view_clear = False
    check_down = row + 1
    view_clear = True
    while check_down < len(row_max_heights) and view_clear:
        score_parts[3] += 1
        if tree_grid[check_down][col] < base_height:
            check_down += 1
        else:
            view_clear = False
    return prod(score_parts)


with open('2022/day/08/input.txt', 'r') as fh:
    row_index = 0
    for row in fh:
        row = row.rstrip()
        row_length = len(row)
        if row_length > len(col_max_heights):
            col_max_heights.extend([0] * (row_length - len(col_max_heights)))
        tree_grid.append([0] * row_length)
        row_max_heights.append(0)
        for col_index, tree in enumerate(row):
            tree_height = int(tree)
            tree_grid[row_index][col_index] = tree_height
            row_max_heights[row_index] = max(tree_height, row_max_heights[row_index])
            col_max_heights[col_index] = max(tree_height, col_max_heights[col_index])
        row_index += 1

visibility_grid = [[True] * len(col_max_heights)]
for i in range(len(row_max_heights) - 2):
    visibility_row = [True]
    visibility_row.extend([False] * (len(col_max_heights) - 2))
    visibility_row.append(True)
    visibility_grid.append(visibility_row)
visibility_grid.append([True] * len(col_max_heights))

for row_index, row in enumerate(tree_grid[1:-1], 1):
    leftmost_tree_height = 0
    rightmost_tree_height = 0
    for left_index, tree_height in enumerate(row):
        if tree_height > leftmost_tree_height:
            visibility_grid[row_index][left_index] = True
            leftmost_tree_height = tree_height
            if leftmost_tree_height == row_max_heights[row_index]:
                break
    for right_index, tree_height in enumerate(reversed(row)):
        if tree_height > rightmost_tree_height:
            visibility_grid[row_index][-(right_index + 1)] = True
            rightmost_tree_height = tree_height
            if rightmost_tree_height == row_max_heights[row_index]:
                break

for col_index in range(1, len(col_max_heights) - 1):
    uppermost_tree_height = 0
    lowermost_tree_height = 0
    for top_index in range(len(row_max_heights)):
        tree_height = tree_grid[top_index][col_index]
        if tree_height > uppermost_tree_height:
            visibility_grid[top_index][col_index] = True
            uppermost_tree_height = tree_height
            if uppermost_tree_height == col_max_heights[col_index]:
                break
    for bottom_index in range(len(col_max_heights) - 1, 1, -1):
        tree_height = tree_grid[bottom_index][col_index]
        if tree_height > lowermost_tree_height:
            visibility_grid[bottom_index][col_index] = True
            lowermost_tree_height = tree_height
            if lowermost_tree_height == col_max_heights[col_index]:
                break

print(sum(sum(1 if x else 0 for x in row) for row in visibility_grid))

top_score = 0
for row_index in range(len(row_max_heights)):
    for col_index in range(len(col_max_heights)):
        top_score = max(top_score, scenic_score(tree_grid, row_index, col_index))

print(top_score)
