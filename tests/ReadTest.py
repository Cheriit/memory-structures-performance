import random

from commons import timer
from data import Person
from databases import Database
from tests import Test


class ReadTest(Test):
    """
    Abstract class that performs read test scenario for all the given databases and adds them at the end of the
    given file.
    """

    @staticmethod
    @timer
    def perform_scenario(database: Database[Person], index_range=range(1, Test.size)) -> None:
        """Class method that performs read scenario"""
        for _ in index_range:
            database.get(random.randint(1, Test.size - 1))

    def __str__(self):
        return "read"
