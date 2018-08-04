# Used to set different behaviour on same method.
# for example, here execute method can be used to execute different method.
import types # Import the types module

class Strategy:
    """ The Strategy Pattern class."""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # if a reference to a function is provided, replace the execute()
        # method with the given function.
        if function:
            self.execute = types.MethodType(function, self)

    # It is replaced by other method, if provided.
    def execute(self):
        """ The default method that prints the name of the strategy being used."""
        print(f'{self.name} is used!')


# Replacement method 1.
def strategy_one(self):
    print(f'{self.name} is used to execute method 1.')

# Replacement method 2.
def strategy_two(self):
    print(f'{self.name} is used to execute method 2.')

# Default strategy
s0 = Strategy()

# First strategy
s1 = Strategy(strategy_one)

# Second strategy
s2 = Strategy(strategy_two)

s1.name = 'Strategy one'
s2.name = 'Strategy two'

s0.execute()
s1.execute()
s2.execute()
