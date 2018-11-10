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
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            if nChildren == 0:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                else: # root 노드일 경우
                    self.root = None
            elif nChildren == 1:
                if node.left:
                    child = node.left
                elif node.right:
                    child = node.right

                if parent:
                    if parent.left == node:
                        parent.left = child
                    elif parent.right == node:
                        parent.right = child
                else:
                    self.root = child
            else: # 자식이 2명 이상일 경우
                parent = node
                successor = node.right # 노드보다 큰 값 중 하나 큰 값을 찾음. -> successor

                while successor.left: # successor를 찾음
                    parent = successor
                    successor = successor.left

                node.key = successor.key
                node.data = successor.data

                if parent.left == successor:
                    parent.left = successor.right
                elif parent.right == successor:
                    parent.right = successor.right

            return True

        else:
            return False


