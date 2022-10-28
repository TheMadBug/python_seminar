def the_basics():

    some_text = "hello"

    an_int = 3 + 1

    a_bool = True

    a_float = 3.141592653589793238462643383279

    print(f"pi is exactly {a_float:.0f}")

    an_empty_set = set()
    a_set_with_stuff_in_it = {"cat", "dog"}
    if "cat" in a_set_with_stuff_in_it:
        print("we have a cat")

    an_empty_dictionary = {}
    a_dictionary_with_stuff_in_it = {"oranges": 1, "apples": 2}

    an_empty_list = []
    a_list_with_stuff_in_it = [2, 3, 5, 7, 11]
    a_list_with_stuff_in_it += [13]

    a_tuple = 2, 3, 5, 7, 11
    # difference between tuple and a list?
    # tuples are immutable
    # by convention, more acceptable for tuples to have different data types and be of an expected length

    def methods_can_be_nested():
        # sometimes this is neater, sometimes it's messier
        nonlocal a_tuple
        return a_tuple[3]


def _this_method_should_only_be_called_in_this_file():
    print("I'm shy, see the underscore at the start")
