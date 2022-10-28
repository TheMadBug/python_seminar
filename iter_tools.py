import itertools
from dataclasses import dataclass

@dataclass
class Animal:
    species: str
    name: str


all_animals = [
    Animal("cat", "Sargent Bobkins"),
    Animal("dog", "Major Woofles"),
    Animal("cat", "Master Meow"),
    Animal("dog", "Barky"),
    Animal("mouse", "Sherry")
]

sorted_by_species = sorted(all_animals, key=lambda a: a.species)

for species_name, animals_by_species in itertools.groupby(sorted_by_species, lambda a: a.species):
    print(f"We have {len(list(animals_by_species))} {species_name}s")

#
#
# cycling_alphabet = []
# for letter in itertools.takewhile(lambda _: len(cycling_alphabet) < 10, itertools.cycle(["A", "B", "C"])):
#     cycling_alphabet.append(letter)
# print(cycling_alphabet)

children = ["Jane", "Joe", "Jork", "Jaggard"]
toys = ["ball", "puzzle"]

# for child, toy in zip(children, toys):
#     print(f"{child} gets to play with {toy}")
#     # wont even mention Jork or Jaggard

for child, toy in itertools.zip_longest(children, toys, fillvalue="No toy sorry"):
    print(f"{child} gets to play with {toy}")