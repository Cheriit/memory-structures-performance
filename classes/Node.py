class Node:
    def __init__(self, key, value, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value

    def insert(self, key, value, left=None, right=None):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, value, left, right)
                else:
                    self.left.insert(key, value, left, right)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, value, left, right)
                else:
                    self.right.insert(key, value, left, right)

    def search(self, key, found=None):
        if found is None:
            found = []
        if self.left:
            self.left.search(key, found)
        if self.key == key:
            found.append([self.key, self.value])
        if self.right:
            self.right.search(key, found)
        return found

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, self.value)
        if self.right:
            self.right.inorder()

    def inorder_string(self):
        if self.left:
            self.left.inorder_string()
        print("key: {}, value: {}".format(self.key, self.value))
        if self.right:
            self.right.inorder_string()

    def update(self, key, value):
        if self.key > key and self.left:
            self.left.update(key, value)
        if self.key == key:
            self.value = value
            return
        if self.key < key and self.right:
            self.right.update(key, value)

    def delete(self, key, prev, root):
        if self.key > key and self.left:
            self.left.delete(key, self, root)
        if self.key == key:
            temp_right = None
            temp_left = None
            if self.right:
                temp_right = Node(self.right.key, self.right.value, self.right.left, self.right.right)
            if self.left:
                temp_left = Node(self.left.key, self.left.value, self.left.left, self.left.right)
            if prev.left.key == key:
                prev.left = None
            elif prev.right.key == key:
                prev.right = None
            if temp_right:
                root.add(temp_right.key, temp_right.value, temp_right.left, temp_right.right)
            if temp_left:
                root.add(temp_left.key, temp_left.value, temp_left.left, temp_left.right)
        if self.key < key and self.right:
            self.right.delete(key, self, root)
