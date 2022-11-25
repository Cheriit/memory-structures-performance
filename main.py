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


def run_test(test: Test, databases, size=None) -> None:
    print(f'Running {str(test)} test.')
    duration = test.run(f'out/{str(test)}.csv', databases, size)
    print(f'Test took: {str(duration)} seconds')


def run_tests(param_size=None):
    databases: list[Database] = [ListDatabase[Person]([]), DictionaryDatabase[Person]([]), TreeDatabase[Person]([])]
    run_test(CreateTest(), databases, param_size)
    run_test(ReadTest(), databases)
    run_test(ReadRangeTest(), databases)
    run_test(UpdateTest(), databases)
    run_test(MixtureTest(), databases)
    run_test(DeleteTest(), databases)
    run_test(AppendTest(), databases)


if __name__ == '__main__':
    for param in params_list:
        run_tests(param)
