import re


class CargoDeck:
    def __init__(self):
        self.stacks = []
        self.deck_size = 0
        self.spaces = re.compile(r'\s+')
        self.letters = re.compile(r'[A-Z]')
        self.crane_type = 9000

    def build_stack(self, header):
        stack_labels = [int(x) - 1 for x in self.spaces.split(header.pop().strip())]
        self.deck_size = len(stack_labels)
        for x in range(self.deck_size):
            self.stacks.append([])
        header.reverse()
        for crate_row in header:
            for deck_slot in range(self.deck_size):
                crate_index = (deck_slot * 4) + 1
                crate_id = crate_row[crate_index:crate_index+1]
                if self.letters.match(crate_id):
                    self.stacks[stack_labels[deck_slot]].append(crate_id)

    def crane_lift(self, from_slot, to_slot, count=1, crane_model=9000):
        if crane_model == 9000:
            self.crane_lift_9000(from_slot, to_slot, count)
        elif crane_model == 9001:
            self.crane_lift_9001(from_slot, to_slot, count)

    def crane_lift_9000(self, from_slot, to_slot, count=1):
        for x in range(count):
            self.stacks[to_slot - 1].append(self.stacks[from_slot - 1].pop())

    def crane_lift_9001(self, from_slot, to_slot, count=1):
        payload = self.stacks[from_slot - 1][-count:]
        self.stacks[from_slot - 1] = self.stacks[from_slot - 1][:-count]
        self.stacks[to_slot - 1].extend(payload)


instruction_parser = re.compile(r'move (\d+) from (\d+) to (\d+)')

# Using the CrateMover 9000 (original problem)
cargo_deck = CargoDeck()
with open('2022/day/05/input.txt', 'r') as fh:
    header = []
    for header_line in fh:
        if header_line.rstrip() == '':
            break
        header.append(header_line.rstrip())
    cargo_deck.build_stack(header)

    for instructions in fh:
        matches = instruction_parser.search(instructions)
        if matches is not None:
            count, from_slot, to_slot = [int(x) for x in matches.groups()]
            cargo_deck.crane_lift(from_slot, to_slot, count)

print(f"Using the CargoMover 9000, the top crates are: {''.join(x[-1] for x in cargo_deck.stacks)}")

# Using the CrateMover 9001 (supplementary problem)
cargo_deck = CargoDeck()
with open('2022/day/05/input.txt', 'r') as fh:
    header = []
    for header_line in fh:
        if header_line.rstrip() == '':
            break
        header.append(header_line.rstrip())
    cargo_deck.build_stack(header)

    for instructions in fh:
        matches = instruction_parser.search(instructions)
        if matches is not None:
            count, from_slot, to_slot = [int(x) for x in matches.groups()]
            cargo_deck.crane_lift(from_slot, to_slot, count, crane_model=9001)

print(f"Using the CargoMover 9001, the top crates are: {''.join(x[-1] for x in cargo_deck.stacks)}")
