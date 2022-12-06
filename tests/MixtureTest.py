import random

from commons import timer
from data import Person
from databases import Database
from tests import Test


def query_mix(database, searches, mods):
    for search_counter in range(1, searches):
        database.get(random.randint(1, Test.size - 1))
    for insert_counter in range(Test.size, Test.size + mods):
        database.add(insert_counter, Person.mock_person())
    for delete_counter in range(Test.size, Test.size + mods):
        database.delete(delete_counter)


class MixtureTest(Test):
    """
    Abstract class that performs mixture test scenario for all the given databases and adds them at the end of the
    given file.
    """

    @staticmethod
    @timer
    def perform_scenario(database: Database[Person]) -> None:
        """Class method that performs mixture scenario"""
        '''query_mix(database, 24000, 3000)
        query_mix(database, 18000, 6000)
        query_mix(database, 12000, 9000)'''
        query_mix(database, 24000, 300)
        query_mix(database, 18000, 600)
        query_mix(database, 12000, 900)

    def __str__(self):
        return "mixture"
