# Used when we need to de-couple the cohesive object.
# for example, we can add a mediator object in/bw the Colleague.

import sys

class Colleague(object):

    def __init__(self, mediator, id):
        self._mediator = mediator
        self._id = id

    def get_id(self):
        return self._id

    def send(self, msg):
        pass

    def receive(self, msg):
        pass


class ConcreteColleague(Colleague):

    def __init__(self, mediator, id):
        super().__init__(mediator, id)

    def send(self, msg):
        print(f'Message {msg} sent by Colleague {self._id}')
        self._mediator.distribute(self, msg)

    def receive(self, msg):
        print(f'Message {msg} received by Colleague {self._id}')

class Mediator:

    def add(self, colleague):
        pass

    def distribute(self, sender, msg):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        self._colleague = []

    def add(self, colleague):
        self._colleague.append(colleague)

    def distribute(self, sender, msg):
        for colleague in self._colleague:
            if colleague.get_id() != sender.get_id():
                colleague.receive(msg)

def main():
    mediator = ConcreteMediator()

    c1 = ConcreteColleague(mediator, 1)
    c2 = ConcreteColleague(mediator, 2)
    c3 = ConcreteColleague(mediator, 3)

    mediator.add(c1)
    mediator.add(c2)
    mediator.add(c3)

    c1.send('Good Morning!')


if __name__ == '__main__':
    main()

