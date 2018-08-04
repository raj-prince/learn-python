# Single Pattern is used when we need to make some information shared b/w objects.
# Like global variable.

class Borg:
    """ Borg class making class attributes global."""

    _shared_state = {}

    def ___init__(self):
        self.__dict__ = self._shared_state # Make it an attribute dictionary.


class Singleton(Borg): # Inherits from Borg class
    """ This class now shares all its attributes among its various instances."""

    # This essentially makes the singleton objects an object-oriented global variable.

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the attribute dictionary by inserting a new key-value pair.
        self._shared_state.update(kwargs)


    def __str__(self):
        # Returns the attribute dictionary for printing.
        return str(self._shared_state)

# Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

# Let's create another singleton object and test
y = Singleton(SMTP="Simple Network Management Protocol")
print(y)
