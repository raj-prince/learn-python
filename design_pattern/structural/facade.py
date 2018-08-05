# Used when we need hide the internal working.
# Like, when we start a car, just we need to click start button.
# Not, do individual operation like, starting engine, connect to tyre etc.

class SubsystemA:
    """ First component of task."""

    def method1(self):
        print('SubsystemA method1...')

    def method2(self):
        print('SubsystemA method2...')

class SubsystemB:
    """ Second component of a task."""

    def method1(self):
        print('SubsystemB method1...')

    def method2(self):
        print('SubsystemB method2...')

class Facade:

    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def method(self):
        self._subsystem_a.method1()
        self._subsystem_a.method2()
        self._subsystem_b.method1()
        self._subsystem_b.method2()


def main():
    f = Facade()
    f.method()

if __name__ == "__main__":
    main()
