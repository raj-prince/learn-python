class Dog:
    """ A Simple Dog Class."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Woof!")

class Cat:
    """ A Simple Cat Class. """

    def __init__(self, name):
        self.name = name


    def speak(self):
        print("Meow!")


def get_pet(pet="Dog"):
    """ The Factory Method"""

    pets = dict(dog=Dog("Ramu"), cat=Cat("Peace"))

    return pets[pet]

d = get_pet("dog")
d.speak() # Print Woof!

c = get_pet("cat")
c.speak() # Print Meow!

""" So in this factory method, we need to modify our method, when a new class we
need to instantiate, ie. We need previous information to work it. So we use abstract_factory
implementation to remove this drawback."""
