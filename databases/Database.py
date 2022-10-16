from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Database(ABC, Generic[T]):
    """
    Abstract class that handles memory operation on the chosen memory structure.
    """

    @abstractmethod
    def __init__(self, values: list[tuple[int, T]]) -> None:
        """Class method that accepts starting state of the database."""
        pass

    @abstractmethod
    def add(self, key: int, value: T) -> bool:
        """Class method that adds value to the structure. In case of the already existing key, it returns false."""
        pass

    @abstractmethod
    def get(self, key: int) -> T:
        """Class method that returns value under the specific key."""
        pass

    @abstractmethod
    def get_range(self, key_from: int, key_to: int) -> list[T]:
        """Class method that returns values under the keys in the defined range."""
        pass

    @abstractmethod
    def update(self, key: int, new_value: T) -> bool:
        """Class method that updates (overwrites) entry in database. In case of non-existing key value it returns
        false."""
        pass

    @abstractmethod
    def delete(self, key: int) -> bool:
        """Class method that deletes entry under the specific key. In case of non-existing key value, it returns
        false."""
        pass

    @abstractmethod
    def __str__(self):
        """Name of the database."""
        pass
