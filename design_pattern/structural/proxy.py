# Used when we have some resource instensive object. like Producer, Director.

import time

class Producer:
    """ Define the resource intensive object."""

    def produce(self):
        print('Producer is hard-working.')

    def meet(self):
        print('Producer has time to meet you now.')

class Proxy:
    """ Define the relatively less resource intensive object as a middle man."""
    def __init__(self):
        self.occupied = 'NO'
        self.producer = None

    def produce(self):
        """ Check if producer is available or not. """
        print('Artist is checking producer is available or not...')

        if self.occupied == 'NO':
            # create one if not already have.
            if self.producer == None:
                self.producer = Producer()

            time.sleep(2)
            # make the producer to meet the guest.
            self.producer.meet()
        else:
            # Otherwise, busy
            time.sleep(2)
            print('Producer is busy')




p = Proxy()

p.produce()

p.occupied = 'YES'

p.produce()
