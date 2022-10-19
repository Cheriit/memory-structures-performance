from databases import Database
from typing import TypeVar, Generic
from classes import Node

T = TypeVar('T')


class TreeDatabase(Generic[T], Database[T]):
    """
     Class that handles memory operation on the T-Tree structured "database".
    """

    def __init__(self, values: list[tuple[int, T]]) -> None:
        self.items = None
        for value in values:
            if self.items is None:
                self.items = Node(value[0], value[1])
            else:
                self.items.insert(value[0], value[1])

    def add(self, key: int, value: T) -> bool:
        """Class method that adds value to the structure. In case of the already existing key, it returns false."""
        if len(self.items.search(key)) > 0:
            return False
        self.items.insert(key, value)

    def get(self, key: int) -> T:
        """Class method that returns value under the specific key."""
        return self.items.search(key)

    def get_range(self, key_from: int, key_to: int) -> list[T]:
        """Class method that returns values under the keys in the defined range."""
        result = []
        for key in range(key_from, key_to+1):
            result += self.items.search(key)
        return result

    def update(self, key: int, new_value: T) -> bool:
        """Class method that updates (overwrites) entry in database. In case of non-existing key value it returns
        false."""
        if len(self.items.search(key)) > 0:
            return False
        self.items.update(key, new_value)

    def delete(self, key: int) -> bool:
        """Class method that deletes entry under the specific key. In case of non-existing key value, it returns
        false."""
        pass

    def __str__(self):
        return "TreeDatabase"
