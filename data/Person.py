from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Person:
    """Class for keeping people data."""
    first_name: str
    last_name: str
    pesel: str
    email: str
    phone_number: str
    age: int
    street: str
    city: str
    country: str

    @staticmethod
    def mock_person() -> Person:
        pass

    @staticmethod
    def mock_people(count: int) -> list[Person]:
        return [Person.mock_person() for _ in range(count)]
