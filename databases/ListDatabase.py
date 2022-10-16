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
        pass

    def get(self, key: int) -> T:
        """Class method that returns value under the specific key."""
        pass

    def get_range(self, key_from: int, key_to: int) -> list[T]:
        """Class method that returns values under the keys in the defined range."""
        pass

    def update(self, key: int, new_value: T) -> bool:
        """Class method that updates (overwrites) entry in database. In case of non-existing key value it returns
        false."""
        pass

    def delete(self, key: int) -> bool:
        """Class method that deletes entry under the specific key. In case of non-existing key value, it returns
        false."""
        pass

    def __str__(self):
        return "ListDatabase"
