import random

from commons import timer
from data import Person
from databases import Database
from tests import Test


class DeleteTest(Test):
    """
    Abstract class that performs delete test scenario for all the given databases and adds them at the end of the
    given file.
    """

    @staticmethod
    @timer
    def perform_scenario(database: Database[Person]) -> None:
        """Class method that performs delete scenario"""
        for _ in range(1, Test.size):
            database.delete(random.randint(1, database.get_size() + Test.size - 1))

    def __str__(self):
        return "delete"
