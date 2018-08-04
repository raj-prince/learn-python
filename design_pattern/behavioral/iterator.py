# Iterator is used to traversed the data-structure separately.
def count_to(count):
    """ Our iterator implementation."""

    numbers_in_words = ['one', 'two', 'three', 'four']

    # built in iterator.
    # returns a iterator of tuple with (position, number_in_word).
    iterator = zip(range(count), numbers_in_words)

    for position, number in iterator:

        # returns a generator containing number in words
        yield number

# Test
for num in count_to(4):
    print(f'{num}')
