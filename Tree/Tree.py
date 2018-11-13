from Queue.ArrayQueue import ArrayQueue

class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        """
        노드의 총 개수
        :return:
        """
        left = self.left.size() if self.left else 0
        right = self.right.size() if self.right else 0
        return left + right + 1

    def depth(self):
        """
        노드의 depth (height)
        :return:
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0

        if left_depth >= right_depth:
            return left_depth + 1
        elif left_depth < right_depth:
            return right_depth + 1

    def inorder(self):
        """
        [DFS]
        중위 순회
        left node -> 자신 -> right node
        :return:
        """
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        """
        [DFS]
        전위 순회
        자신 -> left node -> right node
        :return:
        """
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        """
        [DFS]
        후위 순회
        left node -> right node -> 자신
        :return:
        """
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inroder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.posrorder()
        else:
            return []

    def bfs(self):
        """
        [BFS]
        넓이 우선 탐색
        (Queue를 사용함)
        :return:
        """
        q = ArrayQueue()
        traversal = []
        if self.root:
            q.enqueue(self.root)

        while not q.isEmpty():
            node = q.dequeue()
            traversal.append(node)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return traversal

