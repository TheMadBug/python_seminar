# probably been in Python forever

def list_comprehension():
    numbers = [1, 2, 3, 4]

    squared_numbers = [x*x for x in numbers]

    even_numbers = [x for x in numbers if x % 2 == 0]

    even_numbers_squared = [x*x for x in numbers if x % 2 == 0]

    number_to_square_dict = {x: x*x for x in numbers}

    print("Done")


if __name__ == '__main__':
    list_comprehension()
