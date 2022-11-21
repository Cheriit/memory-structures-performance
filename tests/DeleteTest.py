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
        for counter in range(1, 15001):
            database.delete(counter)

    def __str__(self):
        return "delete"
