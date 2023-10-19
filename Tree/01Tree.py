class TreeNode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.child.append( child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        level_prefix = "  " * self.get_level() + "|--" if self.parent else ""
        print(level_prefix + self.data)
        if self.child:
            for child in self.child:
                child.print_tree()



    # def print_tree(self,level =0):
    #     level_string = "  "*level
    #     print(level_string + self.data)
    #     if self.child:
    #         level +=1
    #         for child in self.child:
    #             child.print_tree(level)
    #     level -= 1

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Victus"))
    laptop.add_child(TreeNode("Surface"))

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("Oppo"))
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Apple"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass