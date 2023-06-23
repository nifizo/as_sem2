import random

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def insert(self, key):
        priority = random.random()  # Генеруємо випадковий пріоритет для нового вузла
        self.root = self._insert(self.root, key, priority)

    def _insert(self, node, key, priority):
        if node is None:
            return TreapNode(key, priority)
        if key < node.key:
            node.left = self._insert(node.left, key, priority)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, priority)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                if node.left.priority > node.right.priority:
                    node = self._rotate_right(node)
                    node.right = self._delete(node.right, key)
                else:
                    node = self._rotate_left(node)
                    node.left = self._delete(node.left, key)
        return node

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


treap = Treap()
treap.insert(5)
treap.insert(10)
treap.insert(3)

print(treap.search(5))
print(treap.search(8))

treap.delete(5)
print(treap.search(5))
