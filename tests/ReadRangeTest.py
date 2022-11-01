import random

from commons import timer
from data import Person
from databases import Database
from tests import Test


def query_range(database, searches, elements_per_query):
    for _ in range(searches+1):
        random_key = random.randint(1, 29091)
        database.get_range(random_key, random_key + elements_per_query)


class ReadRangeTest(Test):
    """
    Abstract class that performs read range test scenario for all the given databases and adds them at the end of the
    given file.
    """

    @staticmethod
    @timer
    def perform_scenario(database: Database[Person]) -> None:
        """Class method that performs read range scenario"""
        query_range(database, 30000, 10)
        query_range(database, 3000, 100)
        query_range(database, 300, 1000)

    def __str__(self):
        return "read_range"
