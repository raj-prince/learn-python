# We can make this pattern in creating some domain-specific language.
# Here, Basic method of parsing, using Non-terminal and Terminal Expression.

from abc import abstractmethod

class AbstractionExpression():

    # It forces the define in the subclass.
    @abstractmethod
    def interpret(self):
        pass

class NonterminalExpression(AbstractionExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print('Non-terminal expression being interpreted...')
        self._expression.interpret()

class TerminalExpression(AbstractionExpression):

    def interpret(self):
        print('Terminal expression being interpreted...')


def main():
    ast = NonterminalExpression(NonterminalExpression(TerminalExpression()))
    ast.interpret()

if __name__ == '__main__':
    main()
