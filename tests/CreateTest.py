from commons import timer
from data import Person
from databases import Database
from tests import Test


class CreateTest(Test):
    """
    Abstract class that performs create test scenario for all the given databases and adds them at the end of the
    given file.
    """

    @staticmethod
    @timer
    def perform_scenario(database: Database[Person]) -> None:
        """Class method that performs create scenario"""
        pass

    def __str__(self):
        return "create"
