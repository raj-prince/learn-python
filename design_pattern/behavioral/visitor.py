# Used when we need to do two different things, on a object, with minimal change.
class House(object): # the class being visited.
    def accept(self, visitor):
        """ Interface to accept a visitor."""
        # Triggers the visiting operation.
        visitor.visit(self)

    def work_on_hvac(self, hvac_speciallist):
        # reference of hvac object in the house object.
        print(self, ' worked on by ', hvac_speciallist)

    def work_on_electricity(self, electrician):
        # reference of electrician object in the house object.
        print(self, ' worked on by ', electrician)

    def __str__(self):
        """ Simply return the class name when the House object is printed."""
        return self.__class__.__name__

class Visitor(object):
    """ Abstract Visitor."""
    def __str__(self):
        """ Simply return the class name when the Visitor object is printed."""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """ Concrete visitor: HVAC specialist"""

    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    """ Concrete visitor: electrician"""

    def visit(self, house):
        house.work_on_electricity(self)


# Create hvac specialist.
hv = HvacSpecialist()

# create electrician.
e = Electrician()

# Create house in which we need to visit.
house = House()

# Work on by one.
house.accept(hv)
house.accept(e)