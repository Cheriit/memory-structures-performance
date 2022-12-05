from tests import Test, AppendTest, CreateTest, ReadTest, ReadRangeTest, UpdateTest, MixtureTest, DeleteTest
from databases import Database, ListDatabase, DictionaryDatabase, TreeDatabase
from data import Person

params_list: list[int] = [
    20001,
    30001,
    40001,
    50001,
    60001,
    70001,
    80001,
    90001,
    100001
]
databases: list[Database] = [
    ListDatabase[Person]([]),
    DictionaryDatabase[Person]([]),
    TreeDatabase[Person]([])
]


def run_test(test: Test, test_database) -> None:
    print(f'Running {str(test)} test.')
    duration = test.run(f'out/{str(test)}.csv', test_database)
    print(f'Test took: {str(duration)} seconds')


def init_run(init_database, size=None) -> None:
    for counter in range(1, size):
        init_database.add(counter, Person.mock_person())


def run_tests(run_database: Database, param_size: int = None):
    init_run(run_database, param_size)
    run_test(CreateTest(), run_database)
    run_test(ReadTest(), run_database)
    run_test(ReadRangeTest(), run_database)
    run_test(UpdateTest(), run_database)
    run_test(MixtureTest(), run_database)
    run_test(DeleteTest(), run_database)
    run_test(AppendTest(), run_database)


if __name__ == '__main__':
    for database in databases:
        for param in params_list:
            run_tests(database, param)
