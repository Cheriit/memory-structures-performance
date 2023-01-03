from databases import Database
from typing import TypeVar, Generic
from classes.Node import insert, deleteNode, update, search

T = TypeVar('T')


class TreeDatabase(Generic[T], Database[T]):
    """
     Class that handles memory operation on the T-Tree structured "database".
    """
    __slots__ = ('size', 'root')
    def __init__(self, values: list[tuple[int, T]]) -> None:
        self.size = 0
        self.root = None
        for value in values:
            # self.root = insert(self.root, value[0], value[1])
            self.add(value[0], value[1])
        print(self.size)

    def check(self):
        if depth(self.root.left) - depth(self.root.right) > 1:
            self.root = rotation_right(self.root)
        elif depth(self.root.right) - depth(self.root.left) > 1:
            self.root = rotation_left(self.root)

    def add(self, key: int, value: T) -> bool:
        """Class method that adds value to the structure. In case of the already existing key, it returns false."""
        if search(self.root, key) is not None:
            return False
        self.root = insert(self.root, key, value)
        self.size += 1
        self.check()

    def get(self, key: int) -> T:
        """Class method that returns value under the specific key."""
        return search(self.root, key)

    def get_range(self, key_from: int, key_to: int) -> list[T]:
        """Class method that returns values under the keys in the defined range."""
        result = []
        for key in range(key_from, key_to+1):
            temp = search(self.root, key)
            if temp is not None:
                result += [temp.key, temp.value]
        return result

    def update(self, key: int, new_value: T) -> bool:
        """Class method that updates (overwrites) entry in database. In case of non-existing key value it returns
        false."""
        if search(self.root, key) is None:
            return False
        self.root = update(self.root, key, new_value)

    def delete(self, key: int) -> bool:
        """Class method that deletes entry under the specific key. In case of non-existing key value, it returns
        false."""
        if search(self.root, key) is None:
            return False
        self.root = deleteNode(self.root, key)
        self.size -= 1

    def __str__(self):
        return "TreeDatabase"

    def get_size(self):
        return self.size


def depth(node):
    if node is None:
        return 0
    else:
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        if left_depth > right_depth:
            return left_depth+1
        else:
            return right_depth+1


def rotation_right(node):
    y = node.left
    t = y.right

    y.right = node
    node.left = t

    return y


def rotation_left(node):
    y = node.right
    t = y.left

    y.left = node
    node.right = t

    return y
