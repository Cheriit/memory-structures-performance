from databases import Database
from typing import TypeVar, Generic

T = TypeVar('T')


class DictionaryDatabase(Generic[T], Database[T]):
    """
     Class that handles memory operation on the dictionary structured "database".
    """

    def __init__(self, values: list[tuple[int, T]]) -> None:
        self.items = {}
        for value in values:
            self.items[value[0]] = value[1]

    def add(self, key: int, value: T) -> bool:
        """Class method that adds value to the structure. In case of the already existing key, it returns false."""
        if key in self.items.keys():
            return False
        self.items[key] = value

    def get(self, key: int) -> T:
        """Class method that returns value under the specific key."""
        return self.items[key]

    def get_range(self, key_from: int, key_to: int) -> list[T]:
        """Class method that returns values under the keys in the defined range."""
        to_return = []
        for key in self.items.keys():
            if key_from <= key <= key_to:
                to_return.append(self.items[key])
        return to_return

    def update(self, key: int, new_value: T) -> bool:
        """Class method that updates (overwrites) entry in database. In case of non-existing key value it returns
        false."""
        if key not in self.items.keys():
            return False
        self.items[key] = new_value

    def delete(self, key: int) -> bool:
        """Class method that deletes entry under the specific key. In case of non-existing key value, it returns
        false."""
        if key not in self.items.keys():
            return False
        self.items.pop(key)

    def __str__(self):
        return "DictionaryDatabase"
