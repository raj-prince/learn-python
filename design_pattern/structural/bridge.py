# Used when some methods are implementation dependent and some are independent.

class DrawingAPIOne(object):
    """ Implementation specific abstraction."""

    def draw_circle(self, x, y, radius):
        print(f'Drawing circle with method 1 at {x}, {y} with radius: {radius}')


class DrawingAPITwo(object):
    """ Implementation specific abstraction. """

    def draw_circle(self, x, y, radius):
        print(f'Drawing circle with method 2 at {x}, {y} with radius: {radius}')

class Circle(object):
    """ Implementation-independent abstraction."""

    def __init__(self, x, y, radius, drawing_api):
        """ Initialize the necessary attributes."""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """ Implementation-specific abstraction taker of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._drawing_api, self._x, self._y, self._radius)

    def scale(self, percent):
        """ Implementation-independent."""
        self._radius *= percent

# Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne)

# Build the second Circle object using API Two
circle2 = Circle(1, 2, 3, DrawingAPITwo)

circle1.draw()
circle2.draw()
