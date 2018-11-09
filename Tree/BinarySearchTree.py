class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        elif key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        else:
            raise KeyError("같은 키는 삽입할 수 없습니다.")

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inroder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinarySearchTree:
    """
    이진 탐색 트리
    """
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def lookup(self, key):
        if self.root:
            return self.root.loockup(key)
        else:
            return None, None

    def remove(self, key):
        """
        TODO
        :param key:
        :return:
        """
        pass