# C had switch statements in 1972
# Now 50 short years later, Python has it in 3.10
from typing import Optional, Any


def match_test(error_code: int, text: Optional[str]) -> Any:
    match error_code, text:
        case 200, "failed":
            return "dsfsdf"
        case 200, _:
            return text
        case 404, _:
            return "Not found"
        case _, _:
            return f"Code {error_code} with Data {text}"


def number_relationships(tuple_maybe) -> str:
    match tuple_maybe:
        case 0, item2 if item2 < 10:
            return "Num x = 0 and y less than 10, sounds important"
        case 77, _:
            return "X is 77, that's all that matters"
        case item1, item2 if item1 == item2:
            return "same"
        case _:
            return "Nothing special"


def match_list(values: list[int]):
    match values:
        case [item1]:
            print(f"One value {item1}")
        case [item1, item2]:
            print(f"Two values {item1}, {item2}")
        case [item1, item2, item3]:
            print(f"Three values {item1}, {item2}, {item3}")
        case [*four_or_more]:
            print(f"So many values {four_or_more}")


def match_dict(values: dict[Any, Any]):
    match values:
        case {"food": "pizza", "amount": amount} if amount > 2:
            print("Plenty of pizza for all")
        case {"food": "salad", "amount": 0}:
            print("I forgot the salad")


if __name__ == '__main__':
    match_test(200, "Everything's okay")
    x = number_relationships((0, 6))
    y = number_relationships((0, 66))
    z = number_relationships((77, 6))
    whoops = number_relationships(45)

    print("Done")
