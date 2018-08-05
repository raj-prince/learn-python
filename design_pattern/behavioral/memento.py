# Used to restore the previous state of object. (undo via rollback).

# It is used to serialize or deserialize the object.
import pickle

class Originator:
    """ Class need to save the previous state of object."""

    def __init__(self):
        self._state = None

    # Take the screenshot of the current state.
    def create_memento(self):
        return pickle.dumps(vars(self))

    # Apply the given screenshot
    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)


def main():
    originator = Originator()

    print(vars(originator))

    memento = originator.create_memento()

    originator._state = True

    print(vars(originator))

    originator.set_memento(memento)

    print(vars(originator))

if __name__ == '__main__':
    main()
