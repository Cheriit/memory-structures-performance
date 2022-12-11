import random
from typing import Type

from tests import Test, CreateTest, ReadTest, ReadRangeTest, UpdateTest, MixtureTest, DeleteTest
from databases import Database, ListDatabase, DictionaryDatabase, TreeDatabase
from data import Person

params_list: list[int] = [
    101,
    201,
    301,
    401,
    501,
    601,
    701,
    801,
    901,
    1001,
    1101,
    1201,
    1301,
    1401,
    1601,
    1701,
    1801,
    1901,
    2001,
    2101,
    2201,
    2301,
    2401,
    2501,
    2601
]
databases: list[Type[Database]] = [
    TreeDatabase,
    ListDatabase,
    DictionaryDatabase
]


def run_test(test: Test, test_database, param: int) -> None:
    print(f'Running {str(test)} test.')
    duration = test.run(f'out/{str(test)}.csv', test_database, param)
    print(f'Test took: {str(duration)} seconds')


def init_run(init_database, size=None) -> None:
    for counter in range(1, size):
        init_database.add(counter, Person.mock_person())


def run_tests(run_database: Database, param: int):
    init_run(run_database, param)
    run_test(CreateTest(), run_database, param)
    run_test(ReadTest(), run_database, param)
    run_test(ReadRangeTest(), run_database, param)
    run_test(UpdateTest(), run_database, param)
    run_test(MixtureTest(), run_database, param)
    run_test(DeleteTest(), run_database, param)


if __name__ == '__main__':
    random.seed(1918)
    for _ in range(5):
        for database in databases:
            for param in params_list:
                run_tests(database([x for x in enumerate(Person.mock_people(param))]), param)
