from tests import Test, AppendTest, CreateTest, ReadTest, ReadRangeTest, UpdateTest, MixtureTest, DeleteTest
from databases import Database, ListDatabase, DictionaryDatabase, TreeDatabase
from data import Person


def run_test(test: Test, databases) -> None:
    print(f'Running {str(test)} test.')
    duration = test.run(f'out/{str(test)}.csv', databases)
    print(f'Test took: {str(duration)} seconds')


def run_tests():
    databases: list[Database] = [ListDatabase[Person]([]), DictionaryDatabase[Person]([]), TreeDatabase[Person]([])]
    run_test(CreateTest(), databases)
    run_test(ReadTest(), databases)
    run_test(ReadRangeTest(), databases)
    run_test(UpdateTest(), databases)
    run_test(MixtureTest(), databases)
    run_test(DeleteTest(), databases)
    run_test(AppendTest(), databases)


if __name__ == '__main__':
    run_tests()
