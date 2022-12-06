from abc import ABC, abstractmethod

from commons import timer
from databases import Database


class Test(ABC):
    """
    Abstract class that performs given test scenario for all the given databases and adds them at the end of the
    given file.
    """
    size: int = 3000

    @staticmethod
    @abstractmethod
    @timer
    def perform_scenario(database: Database, param: int) -> None:
        """Class method that performs given scenario"""
        pass

    @timer
    def run(self, result_file_name: str, database: Database, param: int):
        """Test runner that adds content to the file in the CSV format."""
        result = f'{str(database)},{str(self.perform_scenario(database))},{param}\n'
        with open(result_file_name, 'a+') as file:
            file.write(result)

    @abstractmethod
    def __str__(self):
        """Name of the test."""
        pass
