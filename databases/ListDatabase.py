from databases import Database
from typing import TypeVar, Generic

T = TypeVar('T')


class ListDatabase(Generic[T], Database[T]):
    """
     Class that handles memory operation on the list structured "database".
    """

    def __init__(self, values: list[tuple[int, T]]) -> None:
        self.items = values

    def add(self, key: int, value: T) -> bool:
        """Class method that adds value to the structure. In case of the already existing key, it returns false."""
        for item in self.items:
            if item[0] == key:
                return False
        self.items.append((key, value))

    def get(self, key: int) -> T:
        """Class method that returns value under the specific key."""
        for item in self.items:
            if item[0] == key:
                return item[1]
        return None

    def get_range(self, key_from: int, key_to: int) -> list[T]:
        """Class method that returns values under the keys in the defined range."""
        to_return = []
        for item in self.items:
            if key_from <= item[0] <= key_to:
                to_return.append(item[1])
        return to_return

    def update(self, key: int, new_value: T) -> bool:
        """Class method that updates (overwrites) entry in database. In case of non-existing key value it returns
        false."""
        for item in self.items:
            if item[0] == key:
                index_to_update = self.items.index(item)
                self.items[index_to_update] = (key, new_value)
                return True
        return False

    def delete(self, key: int) -> bool:
        """Class method that deletes entry under the specific key. In case of non-existing key value, it returns
        false."""
        for item in self.items:
            if item[0] == key:
                self.items.remove(item)
                return True
        return False

    def __str__(self):
        return '    '.join(['[' + str(x[0]) + ']: ' + str(x[1]) for x in self.items])
