# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree

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

    def search(self, val):
        if self.data == val:
            return True

        # value might be in left sub tree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        # value might be in right sub tree
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        min = self.data
        if self.left:
            min = self.left.find_min()
        return min

    def find_max(self):
        max = self.data
        if self.right:
            max = self.right.find_max()
        return max

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum += self.data
        if self.right:
            sum += self.right.calculate_sum()
        return sum

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

            # deleting using the max value from left
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

            # deleting using the min value from right
            
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    root = build_tree([17, 4, 9, 1, 18, 20, 23, 34])
    root = root.delete(17)
    print(f"In Order Traversal: {root.in_order_traversal()}")
    root = build_tree([17, 4, 9, 1, 18, 20, 23, 34])
    root = root.delete(1)
    print(f"In Order Traversal: {root.in_order_traversal()}")
    root = build_tree([17, 4, 9, 1, 18, 20, 23, 34])
    root = root.delete(20)
    print(f"In Order Traversal: {root.in_order_traversal()}")
    # root = build_tree([1, 4, 9, 17, 18, 20, 23, 34])
    # root = root.delete(1)
    # print(f"In Order Traversal: {root.in_order_traversal()}")
