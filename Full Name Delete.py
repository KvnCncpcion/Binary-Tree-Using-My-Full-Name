class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            minimum_val = self.right.get_minimum()
            self.data = minimum_val
            self.right = self.right.delete(minimum_val)

        return self

    def get_minimum(self):
        if self.left is None:
            return self.data
        return self.left.get_minimum()

    def get_maximum(self):
        if self.right is None:
            return self.data
        return self.right.get_maximum()


def build_tree(elements):
    print("This is my full name:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    full_name = ["K", "E", "V", "I", "N", "J", "O", "S", "E", "P", "H", "G", "C", "O", "N", "C", "E", "P", "C", "I",
                 "O", "N"]
    full_name_tree = build_tree(full_name)

    full_name_tree.delete("K")
    print("\nThis is the result after K is deleted:", full_name_tree.in_order_traversal())

    full_name_tree.delete("C")
    print("\nThis is the result after C is deleted:", full_name_tree.in_order_traversal())