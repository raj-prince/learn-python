# Used when we need to store as a tree structure.
# Composite: for non-leaf node.
# Child: for leaf-node.

class Component(object):
    """ Abstract class."""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """ Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child item.
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here.
        print(f'{self.name}')


class Composite(Component):
    """ Concrete class and maintains the three recursive structure."""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # name of the child.
        self.name = args[0]

        # Keep child items.
        self.children = []


    def append_child(self, child):
        """ Method to add a new child."""
        self.children.append(child)

    def remove_child(self, child):
        """ Method to remove a child."""
        self.children.remove(child)

    def component_function(self):

        # Print the name of the composite object
        print(f'{self.name}')

        # Iterate over all the child.
        for i in self.children:
            i.component_function()


sub1 = Composite('submenu1')
sub11 = Child('sub_submenu11')
sub12 = Child('sub_submenu12')

sub1.append_child(sub11)
sub1.append_child(sub12)
top = Composite('top')
sub2 = Composite('submenu2')
top.append_child(sub1)
top.append_child(sub2)

# Iterate over the tree.
top.component_function()
