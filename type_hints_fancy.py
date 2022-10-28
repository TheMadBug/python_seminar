from random import random
from typing import TypeVar, Sequence, Optional, Generic

from type_hints import DrinkOrder

# Generic Argument

T = TypeVar("T")


def first(seq: Sequence[T]) -> T:
    return seq[0]


# begin script
the_first = first((1, 2))
print(the_first)


def take_items(house: dict[str, int]) -> Optional[dict[str, list[int]]]:
    if random() > 0.5:
        return [house.get("kitchen"), house.get("study")]
    else:
        return None


# begin script
x = first(["cat", "dog"])
items = take_items({"kitchen": 3, "study": 11})
print(items)


X = TypeVar("X")


class PigeonHole(Generic[X]):

    def __init__(self, item: X):
        self.item = item


hole_up = PigeonHole(4)
hole_up.item


def is_sweet(value: DrinkOrder):
    pass