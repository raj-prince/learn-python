# When we need to wrap or package a set of methods into object.
# Like, we get request in terms of methods.
# So we can execute the method one by one easily.

class Command:
    """ Abstract Command class."""
    def execute(self):
        pass


class Copy(Command):
    """ Concreate class 1."""
    def execute(self):
        print('Pasting...')

class Paste(Command):
    """ Concrete class 2."""
    def execute(self):
        print('Pasting...')

class Save(Command):
    """ concrete class 3."""
    def execute(self):
        print('Saving...')

class Macro:
    """ Wrapper object of all the command method, need to execute."""
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute(self):
        for command in self._commands:
            command.execute(command)

def main():
    macro = Macro()
    macro.add_command(Copy)
    macro.add_command(Paste)
    macro.add_command(Save)

    macro.execute()

if __name__ == '__main__':
    main()
