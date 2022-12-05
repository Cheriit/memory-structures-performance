from abc import ABC, abstractmethod

from commons import timer
from databases import Database


class Test(ABC):
    """
    Abstract class that performs given test scenario for all the given databases and adds them at the end of the
    given file.
    """
    # size: int = 30001
    size: int = 3001

    @staticmethod
    @abstractmethod
    @timer
    def perform_scenario(database: Database) -> None:
        """Class method that performs given scenario"""
        pass

    @timer
    def run(self, result_file_name: str, databases: list[Database]):
        """Test runner that adds content to the file in the CSV format."""
        results = []
        for database in databases:
            results.append(f'{str(database)},{str(self.perform_scenario(database))}')
        with open(result_file_name, 'a+') as file:
            file.writelines(['\n'.join(results)])

    @abstractmethod
    def __str__(self):
        """Name of the test."""
        pass
