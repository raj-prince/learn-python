# Used when there is no better interface.
# Like, Korean class has speak_korean() method and British class has speak_british()
# but client wants to call speak() method for each of them.

class Korean:
    """ Korean speaker."""
    def __init__(self):
        self.name = 'Korean'

    def speak_korean(self):
        return 'An-neyong!'

class British:
    """ English speaker."""

    def __init__(self):
        self.name = "British"

    # Note different method name here.
    def speak_english(self):
        return 'Hello!'

class A:
    def __init__(self):
        self.name = 'prince'

class Adapter(A):
    """ This changes the generic method name to individualized method names. """

    def __init__(self, obj, **adapted_method):
        self._object = obj
        # Add a new dictionary item that establishes the mapping between the generic
        # method name: speak() and the concrete method.
        self.__dict__.update(adapted_method)

    # First try to fetch the attribute using __getattribute__ method.
    # if not defined then call it.
    def __getattr__(self, attr):
        """ Simply returns the rest of attributes!"""
        return getattr(self._object, attr)

objects = []

# Create korean object.
korean = Korean()

# Create British object.
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f'{obj.name} says {obj.speak()}')
