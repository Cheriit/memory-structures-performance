class Node:
    __slots__ = ('left', 'right', 'key', 'value')
    def __init__(self, key, value, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value


def insert(node, key, value):
    if node is None:
        return Node(key, value)
    if key < node.key:
        node.left = insert(node.left, key, value)
    else:
        node.right = insert(node.right, key, value)

    return node


def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, root.value)
        inorder(root.right)


def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


def update(root, key, new_value):
    if root is None:
        return root
    if root.key == key:
        root.value = new_value
        return root
    if root.key < key:
        return update(root.right, key, new_value)
    return update(root.left, key, new_value)
