class BPlusMinusTree:
    def __init__(self, order):
        self.order = order
        self.root = BPlusMinusNode(order)

    def insert(self, value):
        if self.root.is_full():
            old_root = self.root
            self.root = BPlusMinusNode(self.order)
            self.root.children.append(old_root)
            self.root.split_child(0)
        self.root.insert_non_full(value)

    def search(self, value):
        return self.root.search(value)


class BPlusMinusNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0

    def is_full(self):
        return len(self.keys) == (2 * self.order) - 1

    def insert_non_full(self, value):
        index = len(self.keys) - 1
        if self.is_leaf():
            self.insert_key(value)
        else:
            while index >= 0 and value < self.keys[index]:
                index -= 1
            index += 1
            if self.children[index].is_full():
                self.split_child(index)
                if value > self.keys[index]:
                    index += 1
            self.children[index].insert_non_full(value)

    def insert_key(self, value):
        index = len(self.keys) - 1
        while index >= 0 and value < self.keys[index]:
            index -= 1
        self.keys.insert(index + 1, value)

    def split_child(self, index):
        child = self.children[index]
        new_node = BPlusMinusNode(self.order)
        mid_index = self.order - 1
        mid_value = child.keys[mid_index]
        self.insert_key(mid_value)
        self.children.insert(index + 1, new_node)
        new_node.keys = child.keys[mid_index + 1:]
        child.keys = child.keys[:mid_index + 1]
        if not child.is_leaf():
            new_node.children = child.children[mid_index + 1:]
            child.children = child.children[:mid_index + 1]

    def search(self, value):
        index = 0
        while index < len(self.keys) and value > self.keys[index]:
            index += 1
        if index < len(self.keys) and value == self.keys[index]:
            return True
        elif self.is_leaf():
            return False
        else:
            return self.children[index].search(value)



