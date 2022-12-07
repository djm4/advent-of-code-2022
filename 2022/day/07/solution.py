import re


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent

    def add_dir(self, directory_name):
        if directory_name not in [x.get_name() for x in self.directories]:
            directory = Directory(directory_name, self)
            self.directories.append(directory)

    def add_file(self, file_name, file_size):
        if file_name not in [x.get_name() for x in self.files]:
            file = File(file_name, int(file_size))
            self.files.append(file)

    def get_directory(self, directory_name):
        return next(filter(lambda x: x.get_name() == directory_name, self.directories), None)

    def get_size(self):
        size = 0
        size += sum([x.get_size() for x in self.files])
        size += sum([x.get_size() for x in self.directories])
        return size

    def get_name(self):
        return self.name

    def go_up(self):
        return self.parent

    def ls(self, recursive=False, with_size=False, prefix='- '):
        for directory in self.directories:
            if with_size:
                print(f'{prefix}{directory.name} (dir size={directory.get_size()})')
            else:
                print(f'{prefix}{directory.name} (dir)')
            if recursive:
                directory.ls(recursive, with_size, prefix=f'  {prefix}')
        for file in self.files:
            if with_size:
                print(f'{prefix}{file.name} (file, size={file.size})')
            else:
                print(f'{prefix}{file.name} (file)')

    def get_directories(self, recursive=False):
        if len(self.directories) > 0:
            for directory in self.directories:
                yield directory
                if recursive:
                    for sub_directory in directory.get_directories(True):
                        yield sub_directory


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name


instruction_parser = re.compile(r'^\$ (ls|cd) ?(.*)$')
ls_file_parser = re.compile(r'^(\d+) (.+)$')
ls_directory_parser = re.compile(r'^dir (.+)$')

root_directory = Directory('/')
current_directory = root_directory
ls_mode = False
with open('2022/day/07/input.txt', 'r') as fh:
    for line in fh:
        match = instruction_parser.match(line)
        if match:
            ls_mode = False
            instruction = match.group(1)
            if instruction == 'cd':
                directory = match.group(2)
                if directory == '..':
                    current_directory = current_directory.go_up()
                elif directory == '/':
                    current_directory = root_directory
                else:
                    current_directory.add_dir(directory)
                    current_directory = current_directory.get_directory(directory)
            elif instruction == 'ls':
                ls_mode = True
        elif ls_mode:
            file_match = ls_file_parser.match(line)
            dir_match = ls_directory_parser.match(line)
            if file_match:
                size, name = file_match.groups()
                current_directory.add_file(name, size)
            elif dir_match:
                name = dir_match.group(1)
                current_directory.add_dir(name)

total_size_sub_100000 = 0
for directory in root_directory.get_directories(recursive=True):
    directory_size = directory.get_size()
    if directory_size <= 100000:
        total_size_sub_100000 += directory_size

print(f'Total size of sub-100000 directories: {total_size_sub_100000}')

target_free_space = 70000000 - 30000000
current_used = root_directory.get_size()
space_needed = current_used - target_free_space

smallest_directory_size = current_used
for directory in root_directory.get_directories(recursive=True):
    directory_size = directory.get_size()
    if directory_size >= space_needed:
        smallest_directory_size = min(smallest_directory_size, directory_size)

print(f'Smallest candidate directory has a size of {smallest_directory_size}')
