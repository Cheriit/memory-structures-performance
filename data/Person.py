from __future__ import annotations

from faker import Faker

from dataclasses import dataclass

fake: Faker = Faker()
Faker.seed(0)


@dataclass
class Person:
    """Class for keeping people data."""
    first_name: str
    last_name: str
    ssn: str
    email: str
    phone_number: str
    age: int
    address: str

    @staticmethod
    def mock_person() -> Person:
        return Person (
            fake.first_name(),
            fake.last_name(),
            fake.ssn(),
            fake.bothify(text="??????????@??.com"),
            fake.bothify(text="+###########"),
            int(fake.bothify(text="##")),
            fake.address()
        )

    @staticmethod
    def mock_people(count: int) -> list[Person]:
        return [Person.mock_person() for _ in range(count)]
