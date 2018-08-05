# Used in case, when object has so many states.

class AtmState():
    """ State of Object having so many states."""
    name = 'state'
    allowed = []

    # go to next allowed state.
    def go_next(self, state):
        if state.name in self.allowed:
            print(f'Current state: {self} switched to {state.name}')
            self.__class__ = state
        else:
            print(f'Current state: {self} switched to {state.name} not possible!')

    def __str__(self):
        return self.name

class Off(AtmState):
    """ State off."""
    name = 'off'
    allowed = ['on']

class On(AtmState):
    """ State on."""
    name = 'on'
    allowed = ['off']

class ATM():
    """ Testing on the Object containing different state."""
    def __init__(self):
        self.current = Off()

    def set_state(self, state):
        self.current.go_next(state)

def main():
    atm = ATM()

    atm.set_state(On)
    atm.set_state(Off)
    atm.set_state(On)


if __name__ == '__main__':
    main()
