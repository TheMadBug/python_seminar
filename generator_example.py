import itertools


# Generators use yield to make a sequence
# been in Python3 forever

def fib_sequence():
    """
    Infinite sequence
    :return: A sequence of ints in the Fibonacci sequence, where the number is the sum of the two prior
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def print_fib_sequence() -> None:
    for item in fib_sequence():
        if item <= 50:
            print(item)
        else:
            break


def print_fib_concise() -> None:
    for item in itertools.takewhile(lambda x: x <= 50, fib_sequence()):
        print(item)


def print_fib_squared() -> None:
    fib_squared_sequence = (x * x for x in fib_sequence())
    for item in itertools.takewhile(lambda x: x <= 100, fib_squared_sequence):
        print(item)


def factors(number):
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            yield i


def print_finite_sequence():
    sequence_of_factors_of_100 = factors(100)
    sequence_of_factors_of_1000 = factors(1000)

    factors_16 = list(factors(16))
    print(factors_16)


if __name__ == '__main__':
    print("** Fib Sequence")
    print_fib_concise()

    print("** Factors 16")
    print_finite_sequence()
