# chain of Responsibility
# Used if we want to handle any thing with so many person in sequence.

class Handler:
    """ Abstract Handler."""

    def __init__(self, successor):
        # used to define who is next handler.
        self._successor = successor

    def handle(self, request):
        # if handled, stop here
        handled = self._handle(request)

        # other wise keep going.
        if not handled:
            self._successor._handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')


class ConcreteHandler1(Handler):
    """ Concrete Handler 1."""
    def _handle(self, request):
        if 0 < request <= 10:
            print(f'Request {request} handled in handler 1')
            return True # Indicates handled.


class DefaultHandler(Handler):
    """ Default Handler."""

    def _handle(self, request):
        """ If there is no handler available."""
        print(f'end of chain, no handler for {request}.')
        return True

class Client:
    """ Using Handlers"""

    def __init__(self):
        # Create change of handler, need to handle.
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


# Create client.
c = Client()

# Create list of requests.
requests = [2, 4, 56]

# Handle each of the request by delegating it to handler.
c.delegate(requests)
