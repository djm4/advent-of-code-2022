x = 1
signal = []

with open('2022/day/10/input.txt', 'r') as fh:
    for line in fh:
        instruction, value = (line.rstrip().split(' ') + [''])[:2]
        if instruction == 'noop':
            signal.append(x)
        elif instruction == 'addx':
            signal.extend([x, x])
            x += int(value)

print(sum(cycle * signal[cycle - 1] for cycle in range(20, len(signal), 40)))

for y in range(6):
    raster_line = ''
    for x in range(40):
        cycle = x + (y * 40)
        raster_line += '##' if abs(x - signal[cycle]) <= 1 else '  '
    print(raster_line)
