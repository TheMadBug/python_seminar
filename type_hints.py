from dataclasses import dataclass
from enum import Enum
from typing import Tuple, TypeAlias


def get_drink_order():
    return "sweet", 3.5


def get_drink_order_typed() -> Tuple[str, float]:
    pass


class Flavor(str, Enum):
    sweet = "sweet"
    bitter = "bitter"


Litres: TypeAlias = float


@dataclass(frozen=True)
class DrinkOrder:
    flavor: Flavor
    size: Litres


def get_drink_order_dataclass() -> DrinkOrder:
    return "sweet", 3


no_idea = get_drink_order()

string_and_float_tuple = get_drink_order_typed()

drink_order = get_drink_order_dataclass()