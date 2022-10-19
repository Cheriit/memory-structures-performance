class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def insert(self, key, value):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, value)
                else:
                    self.left.insert(key, value)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, value)
                else:
                    self.right.insert(key, value)
            else:
                self.key = key
                self.value = value

    def search(self, key, found=None):
        found = []
        if self.left:
            self.left.search(key, found)
        if self.key == key:
            found.append(self.value)
        if self.right:
            self.right.search(key)
        return found

    def update(self, key, value):
        if self.left:
            self.left.update(key, value)
        if self.key == key:
            self.value = value
            return
        if self.right:
            self.right.update(key, value)
