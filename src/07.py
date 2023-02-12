input = list(open('../input/07.txt', 'r'))

class Folder:
    part1 = 0
    to_delete = 3598596
    part2 = 10000000000000000000
    def __init__(self, name: str, parent):
        #print(f'Creating folder {name}')
        self.name = name
        self.parent = parent
        self.content = []
        self.size = 0

    def get_folder(self, name):
        '''Return folder if found, else return None'''
        for element in self.content:
            if element.name == name and isinstance(element, Folder):
                return element
        return None

    def content_exists(self, name, type):
        '''Return True if item of name and type in folder, else return False'''
        for element in self.content:
            if element.name == name and isinstance(element, type):
                return True
        return False

    def add_content(self, name, opt):
        '''Add folder with given name and current folder as parent.
        Add file if not dir '''
        if opt == 'dir':
            self.content.append(Folder(name, self))
        else:
            self.content.append(File(name, opt))


    def get_size(self):
        folders = [folder for folder in self.content if isinstance(folder, Folder)]

        for folder in folders:
            self.size += folder.get_size()

        for file in self.content:
            if isinstance(file, File):
                #print('Adding file', file.name, 'Size:', file.size)
                self.size += file.size
        
        return self.size

    def print_sizes(self):
        folders = [folder for folder in self.content if isinstance(folder, Folder)]
        for folder in folders:
            folder.print_sizes()
        
        if self.size <= 100000:
            Folder.part1 += self.size

        if self.size > Folder.to_delete:
            if self.size < Folder.part2:
                Folder.part2 = self.size
        
class File:
    def __init__(self, name, size):
        #print(f'Creating file {name}')
        self.name = name
        self.size = int(size)

class Action:
    def __init__(self, command, opt=None):
        self.command = command
        self.opt = opt
        self.output = list() 

class Filesystem:
    def __init__(self, actions):
        self.root = Folder('/', None)
        self.current_dir = self.root
        self.actions = actions 

    def perform_action(self):
        action = self.actions.pop(0)
        operations = {'cd': self.handle_cd, 'ls': self.handle_ls}
        operations[action.command](action)
        
    def handle_cd(self, action):
        if action.opt == '..':
            self.current_dir = self.current_dir.parent
        elif action.opt == '/':
            self.current_dir = self.root
        else:
            self.current_dir = self.current_dir.get_folder(action.opt)
        #print(f'$ cd {action.opt}')
        #print(f'Moved to folder {self.current_dir.name}')

    def handle_ls(self, action):
        # check if contents listed is already in Folder.content, else add them
        #print([element.name for element in self.current_dir.content])
        for line in action.output:
            [opt, name]  = line
            type = Folder if opt == 'dir' else File
            if self.current_dir.content_exists(name, type):
                continue
            else:
                self.current_dir.add_content(name, opt)


commands = list()
for line in input[1:]:
    if line.startswith('$'):
        [_, command, *opt] = line.split()
        commands.append(Action(command, *opt))
    else:
        [info, name] = line.split()
        commands[-1].output.append([info, name])


filesystem = Filesystem(commands)
while filesystem.actions:
    filesystem.perform_action()

filesystem.handle_cd(Action('cd', '/'))
filesystem.current_dir.get_size()
filesystem.current_dir.print_sizes()

to_delete = -(70000000 - 30000000 - filesystem.root.size)

print(to_delete)
print(Folder.part2)

