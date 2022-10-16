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
    def perform_scenario(database: Database[Person]) -> None:
        """Class method that performs read scenario"""
        pass

    def __str__(self):
        return "read"
