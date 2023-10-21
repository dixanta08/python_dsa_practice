class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
                pass
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements =[]

        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self,val):
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



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    root = build_tree([50,4,4,4,7,23,36,145,34,1,2,3,4,5,6,7])
    print(root.in_order_traversal())
    print(root.search(7))