class Node:
    __slots__ = ('left', 'right', 'key_from', 'key_to', 'values')

    def __init__(self, key, value, node_size=1000, left=None, right=None):
        self.left = left
        self.right = right
        self.key_from = key // node_size * node_size
        self.key_to = key // node_size * node_size + node_size - 1
        self.values = {key: value}


def insert(node, key, value):
    if node is None:
        return Node(key, value)
    if key < node.key_from:
        node.left = insert(node.left, key, value)
    elif key > node.key_to:
        node.right = insert(node.right, key, value)
    else:
        node.values[key] = value

    return node


def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    minVal = min(current.values)
    return minVal, current.values[minVal]


def deleteNode(root, key, deleted=False):
    if root is None:
        return root, deleted
    if isinstance(root, tuple):
        r = root[0]
    else:
        r = root
    if (r.key_from <= key <= r.key_to) and (len(r.values) > 0):
        if key in r.values:
            del r.values[key]
            deleted = True
            if len(r.values) == 0:
                tmp = deleteNode(r, r.key_from)
                if tmp is not None:
                    r = tmp[0]
    else:
        if key < r.key_from:
            tmp = deleteNode(r.left, key)
            if tmp is not None:
                r.left = tmp[0]
        elif key > r.key_to:
            tmp = deleteNode(r.right, key)
            if tmp is not None:
                r.right = tmp[0]
        else:
            if r.left is None:
                temp = r.right
                r = None
                return temp, deleted
            elif r.right is None:
                temp = r.left
                r = None
                return temp, deleted

            temp = minValueNode(r.right)
            r.key = temp[0]
            r.right = deleteNode(r.right, temp[0])[0]
    return r, deleted


def inorder(root):
    if root is not None:
        inorder(root.left)
        for x in root.values:
            print(x, root.values[x])
        inorder(root.right)


def search(root, key):
    if root is None:
        return root
    if root.key_from <= key <= root.key_to:
        if key in root.values:
            return root
    if root.key_from > key:
        return search(root.left, key)
    return search(root.right, key)


def update(root, key, new_value):
    if root is None:
        return root
    if root.key_from <= key <= root.key_to:
        if key in root.values:
            root.values[key] = new_value
            return root
    if root.key_to < key:
        return update(root.right, key, new_value)
    return update(root.left, key, new_value)
