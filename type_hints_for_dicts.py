from typing import TypedDict, Optional, List


# Python 3.8


class GpsCoordinate(TypedDict):
    long: float
    lat: float


class Location(TypedDict, total=False):
    place: str
    coordinate: Optional[GpsCoordinate]


area34: Location = {"place": "classified"}
area33: Location = {"place": "Somewhere outside New Mexico", "coordinate": {"lat": 32.43, "long": 23.5333}}


def return_locations() -> List[Location]:
    return [area33, area34]


if __name__ == '__main__':
    print(return_locations())
