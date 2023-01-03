import random
from typing import Type

from tests import Test, CreateTest, ReadTest, ReadRangeTest, UpdateTest, MixtureTest, DeleteTest
from databases import Database, ListDatabase, DictionaryDatabase, TreeDatabase100, TreeDatabase500, TreeDatabase1000
from data import Person

import sys
import threading

iteration_count = 5

params_list: list[int] = list(range(20001, 100001, 10000))
# params_list: list[int] = list(range(20001, 30001, 1000))

databases: list[Type[Database]] = [
    TreeDatabase100,
    TreeDatabase500,
    TreeDatabase1000,
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


def main_function():
    for _ in range(iteration_count):
        for database in databases:
            for param in params_list:
                run_tests(database([x for x in enumerate(Person.mock_people(param))]), param)


if __name__ == '__main__':
    random.seed(1918)
    sys.setrecursionlimit(100000)
    threading.stack_size(70000000)
    thread = threading.Thread(target=main_function)
    thread.start()
