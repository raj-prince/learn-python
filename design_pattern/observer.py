# Used if there is a subject, which has so muny subscriber and if there is
# some change occurs in subject then all view gets notification.

class Subject(object):
    """ Represents: what is being observed."""

    def __init__(self):
        # list of observers to a given subject.
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # Notify all the observers except the modifier
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    # Getter that gets the core temperature.
    @property
    def temp(self):
        return self._temp

    # Setter that sets the core temperature.
    @temp.setter
    def temp(self, temp):
        if self._temp != temp:
            self._temp = temp
            self.notify()


class TempViewer:
    def update(self, subject):
        print(f'Temperature viewer: {subject._name} has temperature {subject._temp}')

c1 = Core("Core 1")

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90
