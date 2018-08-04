class Dog:
    """ One of the objects to be returned."""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """ Concrete Factory."""

    def get_pet(self):
        """ Returns a Dog Object."""
        return Dog()

    def get_food(self):
        """ Returns a Dog food Object."""
        return "Dog Food!"


class PetStore:
    """ Petstore houses our abstract factory."""

    def __init__(self, pet_factory=None):
        """ pet_factory is our abstract factory."""

        self.pet_factory = pet_factory


    def show_pet(self):
        """ Utility method to display the details of the objects returned by the Dog Factory."""

        pet = self.pet_factory.get_pet()
        pet_food = self.pet_factory.get_food()

        print(f'Our pet is {pet}')
        print(f'Our pet says hello by {pet.speak()}')
        print(f'Its food is {pet_food}')


# Create a concrete factory.
factory = DogFactory()

# Create a petstore housing our abstract factory.
shop = PetStore(factory)

# Invoke the utility methods
shop.show_pet()
""" Here we will not modify our PetStore. It will work for all Concrete factory.
So, we can add the CatFactory to work on this to also."""
